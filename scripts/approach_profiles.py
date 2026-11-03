"""Tee-to-green centreline profiles every 2 m: raw LiDAR ground (class 2, median within 1 m), the 0.5 m surface and the
2049 heightmap (1.66 m per sample, what the rough and in-between terrain use). Route = back tee, then the interior
vertices of the OSM golf=hole line, then the green centre.
Writes checks/hole_elevations.csv (tee-to-green change per hole, LiDAR vs heightmap), checks/approach_grade.csv (grade over
the last 75 m vs the rest, and how far each layer departs from the ground there), checks/profile_hole_NN.csv and
checks/approach_profiles.png. Usage: python3 scripts/approach_profiles.py GROUND.npz (x, n, z arrays of class 2 points)."""
import sys, json, csv, numpy as np, xml.etree.ElementTree as ET
from scipy.spatial import cKDTree
from scipy.ndimage import map_coordinates
from pyproj import Transformer
c = json.load(open("course.json")); S, Y0, TH = c["size"], c["y_offset"], c["terrain_height"]
g = np.load(sys.argv[1]); gx, gz, gy = g["x"], g["n"], g["z"]
tree = cKDTree(np.c_[gx, gz])
hm = np.fromfile("heightmap_2049.raw", "<u2").reshape(2049, 2049).astype(float) / 65535 * TH + Y0   # row 0 = south
s = np.load("surfaces/surface_05m.npz"); sh = s["h"].astype(float); sx0, sz0, sr = float(s["x0"]), float(s["z0"]), float(s["res"])
t = Transformer.from_crs("EPSG:4326", "EPSG:%d" % c["epsg"], always_xy=True)
r = ET.parse("map.osm").getroot(); nodes = {}
for nd in r.iter("node"):
    e, n = t.transform(float(nd.get("lon")), float(nd.get("lat"))); nodes[nd.get("id")] = (e - c["sw_e"], n - c["sw_n"])
lines = {}
for w in r.findall("way"):
    tg = {q.get("k"): q.get("v") for q in w.findall("tag")}
    if tg.get("golf") == "hole" and tg.get("ref", "").isdigit():
        lines[int(tg["ref"])] = [nodes[q.get("ref")] for q in w.findall("nd") if q.get("ref") in nodes]
greens = {int(h["hole"]): (float(h["green_x"]), float(h["green_z"])) for h in csv.DictReader(open("holes.csv"))}
tees = {}
for row in csv.DictReader(open("tees.csv")):
    if row["box"] == "1": tees[int(row["hole"])] = (float(row["x"]), float(row["z"]))

def lidar(px, pz):
    out = np.full(len(px), np.nan)
    for i, nb in enumerate(tree.query_ball_point(np.c_[px, pz], 1.0)):
        if len(nb) >= 3: out[i] = np.median(gy[nb])
    return out
def hmap(px, pz): return map_coordinates(hm, [pz / S * 2048, px / S * 2048], order=1)
def surf(px, pz):
    rr, cc = (pz - sz0) / sr, (px - sx0) / sr
    v = map_coordinates(sh, [rr, cc], order=1, cval=0); z0 = map_coordinates(sh, [rr, cc], order=0, cval=0)
    return np.where((v > 0) & (z0 > 0), v / 100 + Y0, np.nan)

summary, grades, prof = [], [], {}
for h in range(1, 19):
    pts = [tees[h]] + lines[h][1:-1] + [greens[h]]
    # drop interior vertices that sit behind the tee or past the green
    P = np.array(pts); seg = np.hypot(*np.diff(P, axis=0).T); L = np.r_[0, np.cumsum(seg)]
    d = np.arange(0, L[-1], 2.0); d = np.r_[d, L[-1]]
    px, pz = np.interp(d, L, P[:, 0]), np.interp(d, L, P[:, 1])
    ld, hd, sd = lidar(px, pz), hmap(px, pz), surf(px, pz)
    prof[h] = (d, ld, hd, sd)
    with open("checks/profile_hole_%02d.csv" % h, "w", newline="") as f:
        wr = csv.writer(f); wr.writerow(["dist_m", "x", "z", "lidar_elev_m", "heightmap_elev_m", "surface05_elev_m"])
        for row in zip(d, px, pz, ld, hd, sd): wr.writerow(["%.1f" % row[0], "%.2f" % row[1], "%.2f" % row[2]] + ["" if np.isnan(v) else "%.2f" % v for v in row[3:]])
    def at(a, k):                                   # mean over ~4 m at the end so a single bad sample can't decide it
        a = a[:3] if k == 0 else a[-3:]; return np.nanmean(a)
    tl, gl, th_, gh = at(ld, 0), at(ld, -1), at(hd, 0), at(hd, -1)
    summary.append((h, L[-1], tl, gl, gl - tl, th_, gh, gh - th_))
    # approach: last 75 m vs the rest; also the 55-75 m window BoJa named
    a = d >= L[-1] - 75; b = d <= L[-1] - 75
    def grade(sel, arr):
        ok = sel & np.isfinite(arr)
        return np.polyfit(d[ok], arr[ok], 1)[0] * 100 if ok.sum() > 3 else np.nan
    dev_h = np.nanmax(np.abs(hd[a] - ld[a])); dev_s = np.nanmax(np.abs(sd[a] - ld[a])) if np.isfinite(sd[a]).any() else np.nan
    # lost grade = how much of the height gained/lost over the approach the layer fails to show
    rise = lambda arr: np.nanmean(arr[a][-3:]) - np.nanmean(arr[a][:3])
    grades.append((h, grade(b, ld), grade(a, ld), grade(a, hd), grade(a, sd), rise(ld), rise(hd), rise(sd), dev_h, dev_s))

with open("checks/hole_elevations.csv", "w", newline="") as f:
    wr = csv.writer(f); wr.writerow(["hole", "route_m", "tee_elev_m", "green_elev_m", "lidar_change_m", "lidar_change_ft",
                                     "heightmap_tee_m", "heightmap_green_m", "heightmap_change_m", "difference_pct"])
    for h, L_, tl, gl, dl, th_, gh, dh in summary:
        pct = (dh - dl) / abs(dl) * 100 if abs(dl) > 0.5 else np.nan
        wr.writerow([h, "%.0f" % L_, "%.2f" % tl, "%.2f" % gl, "%+.2f" % dl, "%+.1f" % (dl * 3.2808), "%.2f" % th_, "%.2f" % gh, "%+.2f" % dh, "" if np.isnan(pct) else "%+.1f" % pct])
with open("checks/approach_grade.csv", "w", newline="") as f:
    wr = csv.writer(f); wr.writerow(["hole", "lidar_grade_before_pct", "lidar_grade_last75_pct", "heightmap_grade_last75_pct", "surface05_grade_last75_pct",
                                     "lidar_rise_last75_m", "heightmap_rise_last75_m", "surface05_rise_last75_m", "heightmap_max_dev_m", "surface05_max_dev_m"])
    for row in grades: wr.writerow([row[0]] + ["" if np.isnan(v) else "%+.2f" % v if i < 7 else "%.2f" % v for i, v in enumerate(row[1:])])
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
fig, ax = plt.subplots(6, 3, figsize=(15, 20))
for h, a in zip(range(1, 19), ax.flat):
    d, ld, hd, sd = prof[h]
    a.plot(d, ld, "k.", ms=2, label="LiDAR ground"); a.plot(d, hd, "r-", lw=1, label="heightmap"); a.plot(d, sd, "b-", lw=1, label="0.5 m surface")
    a.axvspan(d[-1] - 75, d[-1], color="y", alpha=.15); a.set_title("Hole %d" % h); a.set_xlabel("m from back tee"); a.set_ylabel("elev m")
ax.flat[0].legend(fontsize=7); fig.tight_layout(); fig.savefig("checks/approach_profiles.png", dpi=80)
for row in summary: print("hole %2d  %4.0f m  lidar %+6.2f m  heightmap %+6.2f m" % (row[0], row[1], row[4], row[7]))
for row in grades: print("hole %2d  before %+5.1f%%  last75 lidar %+5.1f%% hm %+5.1f%% s05 %+5.1f%%  rise lidar %+5.2f hm %+5.2f s05 %+5.2f  maxdev hm %.2f s05 %.2f" % row)
