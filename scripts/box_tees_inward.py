"""Tees on a mapped tee box but less than 1.5 m inside its edge move to the nearest spot 1.6 m inside (svg_check rule).
Usage: python scripts/box_tees_inward.py HansenDam.GKD"""
import json, math, sys, xml.etree.ElementTree as ET
from pyproj import Transformer
from shapely.geometry import Polygon, Point
from shapely.ops import nearest_points
gkd = sys.argv[1]; c = json.load(open("course.json"))
t = Transformer.from_crs("EPSG:4326", "EPSG:%d" % c["epsg"], always_xy=True)
r = ET.parse("map.osm").getroot(); nodes = {}
for n in r.iter("node"):
    e, nn = t.transform(float(n.get("lon")), float(n.get("lat"))); nodes[n.get("id")] = (e - c["sw_e"], nn - c["sw_n"])
boxes = [Polygon([nodes[q.get("ref")] for q in w.findall("nd")]) for w in r.iter("way")
         if any(q.get("k") == "golf" and q.get("v") == "tee" for q in w.findall("tag"))]
d = json.load(open(gkd, encoding="utf-8-sig"))
for h in d["Holes"]:
    T = {x["TeeType"]: x for x in h["Tees"]}; g = T["GreenCenterPoint"]["Position"]
    nxt = [T[k]["Position"] for k in ("AimPoint1", "AimPoint2") if T[k]["Enabled"] and T[k]["Position"]] + [g]
    for name in ("Black", "Blue", "White", "Yellow"):
        p = T[name]["Position"]
        if not p: continue
        P = Point(p["x"], p["z"])
        for b in boxes:
            if b.buffer(-1.0).contains(P) and not b.buffer(-1.5).contains(P):
                inner = b.buffer(-1.6)
                if inner.is_empty: break
                q = nearest_points(inner, P)[0]; p.update(x=round(q.x, 3), z=round(q.y, 3))
                pts = [p] + (nxt[:-1] if h["Par"] > 3 else []) + [g]
                T[name]["Distance"] = round(sum(math.hypot(u["x"] - v["x"], u["z"] - v["z"]) for u, v in zip(pts, pts[1:])), 3)
                print("hole %d %s moved %.1f m in from the box edge (%d yds)" % (h["HoleNumber"], name, P.distance(q), round(T[name]["Distance"] / 0.9144)))
                break
json.dump(d, open(gkd, "w"), separators=(",", ":"))
