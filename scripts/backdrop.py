"""Backdrop terrain for the horizon (BoJa: the dam embankment and the foothills behind it are very important).
USGS 3DEP 1/3 arc-second DEM (about 10 m), read straight from the public COG, resampled to a 36 km square (18 km each way) in the
course frame, centred on the course square. Writes backdrop/backdrop_2049.raw (16-bit, Windows byte order,
rows = north) and backdrop/backdrop.json with the Unity placement. The course terrain sits in the middle; lower the
backdrop under the 3.4 km course square (or punch a hole) so it never pokes through."""
import json, os, numpy as np, rasterio
from rasterio.windows import from_bounds
from scipy.ndimage import map_coordinates
from pyproj import Transformer
from PIL import Image
c = json.load(open("course.json")); SIZE = 36000.0; RES = 2049
cx, cz = c["sw_e"] + c["size"] / 2, c["sw_n"] + c["size"] / 2
sw_e, sw_n = cx - SIZE / 2, cz - SIZE / 2
url = "/vsicurl/https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/13/TIFF/current/n35w119/USGS_13_n35w119.tif"
to_ll = Transformer.from_crs("EPSG:%d" % c["epsg"], "EPSG:4269", always_xy=True)
corners = [to_ll.transform(sw_e + a, sw_n + b) for a in (0, SIZE) for b in (0, SIZE)]
lo0, lo1 = min(p[0] for p in corners) - 0.01, max(p[0] for p in corners) + 0.01
la0, la1 = min(p[1] for p in corners) - 0.01, max(p[1] for p in corners) + 0.01
with rasterio.open(url) as ds:
    w = from_bounds(lo0, la0, lo1, la1, ds.transform); a = ds.read(1, window=w).astype(np.float64); tr = ds.window_transform(w)
e = sw_e + np.linspace(0, SIZE, RES); nn = sw_n + np.linspace(0, SIZE, RES)
E, N = np.meshgrid(e, nn)                                   # row 0 = south
lon, lat = to_ll.transform(E, N)
col = (lon - tr.c) / tr.a - 0.5; row = (lat - tr.f) / tr.e - 0.5
z = map_coordinates(a, [row, col], order=1, mode="nearest")
base = float(np.floor(z.min())); top = float(np.ceil(z.max() - base) + 1)
os.makedirs("backdrop", exist_ok=True)
(np.clip((z - base) / top, 0, 1) * 65535).astype("<u2").tofile("backdrop/backdrop_2049.raw")
info = {"source": "USGS 3DEP 1/3 arc-second DEM (USGS_13_n35w119)", "size_m": SIZE, "resolution": RES, "m_per_sample": SIZE / (RES - 1),
        "sw_e": sw_e, "sw_n": sw_n, "elev_min": base, "height_m": top,
        "unity_position": {"x": -(SIZE - c["size"]) / 2, "y": base - c["y_offset"], "z": -(SIZE - c["size"]) / 2},
        "unity_size": {"x": SIZE, "y": top, "z": SIZE}, "byte_order": "Windows", "rows": "south first (row 0 = south edge)"}
json.dump(info, open("backdrop/backdrop.json", "w"), indent=2)
gy, gx = np.gradient(z, SIZE / (RES - 1)); sl = np.arctan(np.hypot(gx, gy)); asp = np.arctan2(-gx, gy)
hs = np.sin(np.radians(40)) * np.cos(sl) + np.cos(np.radians(40)) * np.sin(sl) * np.cos(np.radians(315) - asp)
img = Image.fromarray((np.clip(hs, 0, 1) * 255).astype(np.uint8)[::-1]).convert("RGB")
from PIL import ImageDraw
k = RES / SIZE; q0 = (SIZE - c["size"]) / 2 * k; q1 = q0 + c["size"] * k
ImageDraw.Draw(img).rectangle((q0, q0, q1, q1), outline=(255, 0, 0), width=3)
img.save("backdrop/backdrop_hillshade.png")
print(json.dumps(info, indent=1))
