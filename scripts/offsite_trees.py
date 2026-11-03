"""LiDAR trees outside the course: the neighbourhood, the boundary roads and the dam slopes, out to 300 m past the mapped
golf course boundary (or the GKD out-of-bounds line when OSM's boundary is not the course). Same detector as coursekit
trees (1 m canopy height peaks, crown radius from 16 rays), then:
- roofs dropped: the survey has no building class, so a peak is a roof when its canopy is smooth (low local roughness
  of the height grid) or it sits on an OSM building; peaks on roof edges and cars are dropped by the satellite colour
  (grey/tan, green share < 0.35, unless taller than 10 m); poles and wires are dropped by a minimum crown radius;
- anything inside the course boundary, or within 3 m of a trees.csv tree, is left to trees.csv (kept untouched).
Writes offsite_trees.csv (trees.csv columns; run scripts/tree_species.py offsite_trees.csv for species) and
offsite_trees_on_satellite.png. Usage: python3 scripts/offsite_trees.py [grids.npz with dtm, h to skip the LiDAR pass]"""
import sys, csv, numpy as np
from scipy import ndimage
from scipy.spatial import cKDTree
sys.path.insert(0, "../.."); import coursekit as ck
c = ck.load_cfg(); S = int(c["size"]); yo = c["y_offset"]; MARGIN, MIN_H, MIN_R = 300, 3.0, 1.5
if len(sys.argv) > 1:
    g = np.load(sys.argv[1]); dtm, h = g["dtm"], g["h"]
else:
    dtm, h = ck.ground_and_heights(c)
exclude, course = ck.osm_masks(c)
course = ck.course_if_valid(c, course)
if course is None:                       # Hansen: the OSM golf_course area is another facility, so use the GKD OB line
    import json, glob
    from PIL import Image, ImageDraw
    oob = json.load(open(glob.glob("*.GKD")[0]))["pOOB"]["coords"]
    im = Image.new("L", (S, S), 0); ImageDraw.Draw(im).polygon([(q["x"], q["z"]) for q in oob], fill=1)
    course = np.asarray(im) > 0                                         # row = z (south first), like the other grids
zone = ndimage.distance_transform_edt(~course) <= MARGIN
zone &= ~course
# roof test: a roof is a few planes, a canopy is lumpy. Roughness = mean |h - local 3x3 mean| over a 5 m window.
rough = ndimage.uniform_filter(np.abs(h - ndimage.uniform_filter(h, 3)), 5)
tall = h >= 2.0
roof = tall & (rough < 0.35)
roof = ndimage.binary_opening(roof, iterations=1)
lab, nl = ndimage.label(roof); size = ndimage.sum(roof, lab, np.arange(1, nl + 1))
roof = np.isin(lab, 1 + np.flatnonzero(size >= 25))                  # house-sized smooth patches only
roof = ndimage.binary_dilation(roof, iterations=2)
blds = ck.osm_layers(c).get("building") if hasattr(ck, "osm_layers") else None
if blds is not None: roof |= ndimage.binary_dilation(blds, iterations=1)
hs = ndimage.gaussian_filter(h, 1.0)
peaks = (hs == ndimage.maximum_filter(hs, size=5)) & (hs >= MIN_H) & zone & ~roof
py, px = np.nonzero(peaks)
order = np.argsort(-hs[py, px]); py, px = py[order], px[order]
taken, kept = np.zeros((S, S), bool), []
dirs = [(np.cos(t), np.sin(t)) for t in np.linspace(0, 2 * np.pi, 16, endpoint=False)]
for yy, xx in zip(py, px):
    if taken[yy, xx]: continue
    hh, radii = hs[yy, xx], []
    for dx, dy in dirs:
        r = 1
        while r < 15:
            sx, sy = int(round(xx + dx * r)), int(round(yy + dy * r))
            if not (0 <= sx < S and 0 <= sy < S) or hs[sy, sx] < 0.5 * hh: break
            r += 1
        radii.append(r)
    rad = float(np.median(radii))
    rr = max(1, int(round(rad * 0.8)))
    Y, X = np.ogrid[max(0, yy - rr):min(S, yy + rr + 1), max(0, xx - rr):min(S, xx + rr + 1)]
    taken[max(0, yy - rr):min(S, yy + rr + 1), max(0, xx - rr):min(S, xx + rr + 1)] |= (X - xx) ** 2 + (Y - yy) ** 2 <= rr * rr
    if rad >= MIN_R: kept.append((xx, yy, hh, rad))
gs = ck.green_share(c)
n1 = len(kept); kept = [k for k in kept if gs[k[1], k[0]] >= 0.35 or k[2] >= 10]
print("Satellite colour dropped %d grey/tan peaks (roof edges, cars)" % (n1 - len(kept)))
n0 = len(kept)
ct = np.array([(float(r["x"]), float(r["z"])) for r in csv.DictReader(open("trees.csv"))])
d, _ = cKDTree(ct).query(np.array([(k[0] + .5, k[1] + .5) for k in kept]))
kept = [k for k, dd in zip(kept, d) if dd > 3.0]
print("%d offsite trees (%d dropped as already in trees.csv), roofs masked %.1f ha" % (len(kept), n0 - len(kept), roof[zone].sum() / 1e4))
with open("offsite_trees.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["id", "x", "z", "y", "height_m", "crown_radius_m"])
    for i, (xx, yy, hh, rad) in enumerate(kept):
        w.writerow([i, "%.2f" % (xx + .5), "%.2f" % (yy + .5), "%.2f" % (dtm[yy, xx] - yo), "%.1f" % hh, "%.1f" % rad])
ov = np.zeros((S, S, 4), np.float32); ov[roof & zone] = (1, 0, 0, .35); ov[course & ~ndimage.binary_erosion(course, iterations=3)] = (1, 1, 0, .9)
ck.preview(c, ov, np.array([(k[0] + .5, k[1] + .5) for k in kept]).reshape(-1, 2), "%d offsite trees; red = roofs masked; yellow = course boundary" % len(kept), "offsite_trees_on_satellite.png")
