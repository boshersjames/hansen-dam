"""0.5 m bare-earth surfaces from the raw LiDAR ground points (class 2), for the PC to conform the green, collar and
fairway meshes to (the 2049 heightmap is 1.66 m per sample and smooths the shaping away).
Writes surfaces/surface_05m.npz: h = uint16 Unity y in cm (y = elevation - y_offset; 0 = no data),
x0, z0 = Unity coords of cell (0,0) centre, res = 0.5, rows = z (south first), cols = x; mask = greens + 6 m and
fairways + 5 m. Also surfaces/surface_05m_hillshade.png and surfaces/README.md."""
import json, re, numpy as np
from scipy import ndimage
from shapely.geometry import Polygon
from shapely.ops import unary_union
from PIL import Image, ImageDraw
c = json.load(open("course.json")); S = c["size"]; R = 0.5
svg = open("course.svg").read()
def layer(label):
    i = svg.index('inkscape:label="%s"' % label); j = svg.index('</g>', i); out = []
    for d in re.findall(r' d="([^"]+)"', svg[i:j]):
        rings = []
        for sp in re.split(r"(?=M )", d.strip()):
            n = [float(v) for v in re.findall(r"-?\d+\.?\d*", sp)]; pts = [(n[k], S - n[k + 1]) for k in range(0, len(n) - 1, 2)]
            if len(pts) > 2: rings.append(Polygon(pts).buffer(0))
        if rings:
            rings.sort(key=lambda p: -p.area); g = rings[0]
            for r in rings[1:]: g = g.symmetric_difference(r)
            out.append(g)
    return unary_union(out)
area = unary_union([layer("Green").buffer(6), layer("Fairway").buffer(5), layer("Tee").buffer(3)])
x0, z0, x1, z1 = [round(v) for v in area.bounds]; x0 -= 2; z0 -= 2; x1 += 2; z1 += 2
W, H = int((x1 - x0) / R), int((z1 - z0) / R)
im = Image.new("L", (W, H), 0); dr = ImageDraw.Draw(im)
for g in (area.geoms if hasattr(area, "geoms") else [area]):
    dr.polygon([((x - x0) / R, (z - z0) / R) for x, z in g.exterior.coords], fill=255)
    for hole in g.interiors: dr.polygon([((x - x0) / R, (z - z0) / R) for x, z in hole.coords], fill=0)
mask = np.asarray(im) > 0                             # rows = z from z0 upward
d = np.load("points.npz"); x, n, z, cl = d["x"], d["n"], d["z"], d["c"]
g = (cl == 2) & (x >= x0) & (x < x1) & (n >= z0) & (n < z1)
ix = ((x[g] - x0) / R).astype(np.int64); iz = ((n[g] - z0) / R).astype(np.int64); zz = z[g].astype(np.float64)
flat = iz * W + ix
cnt = np.bincount(flat, minlength=W * H); tot = np.bincount(flat, weights=zz, minlength=W * H)
dem = np.where(cnt > 0, tot / np.maximum(cnt, 1), np.nan).reshape(H, W)
print("ground points %d, cells with data in the mask %.1f%%" % (g.sum(), 100 * np.isfinite(dem[mask]).mean()))
hole = ~np.isfinite(dem)                               # fill empty cells from neighbours, then a light 0.5 m smooth
idx = ndimage.distance_transform_edt(hole, return_distances=False, return_indices=True)
dem = dem[tuple(idx)]
w = ndimage.gaussian_filter(np.where(hole, 0.0, 1.0), 1.0)
dem_s = ndimage.gaussian_filter(np.where(hole, 0.0, dem), 1.0) / np.maximum(w, 1e-6)
dem = np.where(w > 0.05, dem_s, dem)
dem = ndimage.gaussian_filter(dem, 0.6)
y = dem - c["y_offset"]
h = np.where(mask, np.clip(np.round(y * 100), 1, 65535), 0).astype(np.uint16)
np.savez_compressed("surfaces/surface_05m.npz", h=h, x0=x0 + R / 2, z0=z0 + R / 2, res=R, y_offset=c["y_offset"])
gy, gx = np.gradient(dem, R); slope = np.arctan(np.hypot(gx, gy)); asp = np.arctan2(-gx, gy)
hs = np.sin(np.radians(45)) * np.cos(slope) + np.cos(np.radians(45)) * np.sin(slope) * np.cos(np.radians(315) - asp)
img = np.where(mask, np.clip(hs, 0, 1) * 255, 40).astype(np.uint8)[::-1]
Image.fromarray(img).save("surfaces/surface_05m_hillshade.png")
print("grid %d x %d at 0.5 m, x %d..%d z %d..%d, y %.2f..%.2f" % (W, H, x0, x1, z0, z1, y[mask].min(), y[mask].max()))
