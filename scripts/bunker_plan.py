"""Deeper bunker plan (BoJa Hansen review 10/29: "missing a lot is ... bunker depth").
Greenside: 0.8-1.5 m by size, steep face toward the green, raised lip 0.2-0.4 m. Fairway: 0.4-0.7 m, lip 0.1 m.
Flat floor over the inner 60 % of the bunker in both. Rewrites bunkers.csv from the existing one (positions, kind, face)."""
import csv, numpy as np
rows = list(csv.DictReader(open("bunkers.csv")))
lerp = lambda a, lo, hi, v0, v1: round(float(v0 + (v1 - v0) * np.clip((a - lo) / (hi - lo), 0, 1)), 2)
out = []
for r in rows:
    a = float(r["area_m2"])
    if r["kind"] == "greenside":
        depth, lip, face = lerp(a, 40, 250, 0.8, 1.5), lerp(a, 40, 250, 0.2, 0.4), 55
    else:
        depth, lip, face = lerp(a, 80, 300, 0.4, 0.7), 0.1, 35
    r.update(depth_m=depth, lip_height_m=lip, face_slope_deg=face, floor_fraction=0.6)
    out.append(r)
keys = list(rows[0].keys())
for k in ("lip_height_m", "face_slope_deg", "floor_fraction"):
    if k not in keys: keys.append(k)
with open("bunkers.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=keys); w.writeheader(); w.writerows(out)
for kind in ("greenside", "fairway"):
    ds = [float(r["depth_m"]) for r in out if r["kind"] == kind]
    if ds: print(kind, len(ds), "bunkers, depth %.2f-%.2f m" % (min(ds), max(ds)))
