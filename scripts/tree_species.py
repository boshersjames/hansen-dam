"""Tag each tree in trees.csv with a species group from its LiDAR crown shape and satellite colour.
palm: tall, small crown on a bare trunk (returns bunched in the top of the tree); pine: tall, narrow crown, returns
spread down the tree, dark green; eucalyptus: very tall or grey-green, open crown; broadleaf (sycamore, coast live oak...):
the rest. A rough estimate (no species ground truth): check in the flyover. Adds species, confidence columns."""
import csv, json, numpy as np, colorsys
from PIL import Image
c = json.load(open("course.json")); S = int(c["size"])
import sys
FN = sys.argv[1] if len(sys.argv) > 1 else "trees.csv"   # also used for offsite_trees.csv
rows = list(csv.DictReader(open(FN)))
d = np.load("points.npz"); x, n, z, cl = d["x"], d["n"], d["z"], d["c"]
keep = cl != 2; x, n, z = x[keep], n[keep], z[keep]
# index non-ground points by 4 m cell
cs = 4.0; key = (n // cs).astype(np.int64) * 10000 + (x // cs).astype(np.int64)
o = np.argsort(key); key, x, n, z = key[o], x[o], n[o], z[o]
sat = np.asarray(Image.open("satellite.jpg").convert("RGB")); P = sat.shape[0] / S
y_off = c["y_offset"]; counts = {}
for r in rows:
    tx, tz, ty, h, rad = float(r["x"]), float(r["z"]), float(r["y"]) + y_off, float(r["height_m"]), float(r["crown_radius_m"])
    rr = max(1.5, 0.7 * rad)
    ks = [(int((tz + dz) // cs)) * 10000 + int((tx + dx) // cs) for dz in np.arange(-rr, rr + cs, cs) for dx in np.arange(-rr, rr + cs, cs)]
    sel = []
    for k in set(ks):
        a, b = np.searchsorted(key, k), np.searchsorted(key, k, side="right")
        if b > a:
            m = np.hypot(x[a:b] - tx, n[a:b] - tz) <= rr
            sel.append(z[a:b][m] - ty)
    hz = np.concatenate(sel) if sel else np.array([])
    hz = hz[(hz > 2) & (hz < h + 2)]
    top = (hz > 0.7 * h).mean() if len(hz) > 10 else np.nan
    mid = ((hz > 0.3 * h) & (hz <= 0.7 * h)).mean() if len(hz) > 10 else np.nan
    px, py = int(tx * P), int((S - tz) * P); q = max(2, int(0.6 * rad * P))
    rgb = sat[max(0, py - q):py + q, max(0, px - q):px + q].reshape(-1, 3).mean(0) / 255
    hh, ss, vv = colorsys.rgb_to_hsv(*rgb)
    slender = h / (2 * rad)
    if h >= 9 and rad <= 4 and top >= 0.6 and mid <= 0.25:
        sp, conf = "palm", "high" if top >= 0.75 and slender >= 2 else "medium"
    elif h >= 10 and slender >= 1.3 and mid >= 0.25 and vv < 0.5:   # flyover: tall pines line most holes
        sp, conf = "pine", "medium" if slender >= 1.6 else "low"
    elif h >= 20 or (h >= 12 and ss < 0.22):                         # eucalyptus mostly on the north holes
        sp, conf = "eucalyptus", "medium" if h >= 20 else "low"
    else:
        sp, conf = "broadleaf", "medium"
    r["species"], r["species_confidence"] = sp, conf
    r["top_share"], r["mid_share"] = "%.2f" % top, "%.2f" % mid
    counts[sp] = counts.get(sp, 0) + 1
with open(FN, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print(counts)
