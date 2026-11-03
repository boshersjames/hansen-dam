"""A card-placed tee whose 9 x 7 m pad would touch a mapped tee box (OPCD drops merged tee shapes, leaving rough:
Hansen Dam 17 White) slides along the line of play, away from the box, until the pad is 1.5 m clear of every box.
Run after fix_box_tees.py and before teepads.py.  Usage: python scripts/clear_pads.py HansenDam.GKD"""
import json, math, sys, xml.etree.ElementTree as ET
from pyproj import Transformer
from shapely.geometry import Polygon, Point
from shapely.ops import unary_union
gkd = sys.argv[1]; c = json.load(open("course.json"))
t = Transformer.from_crs("EPSG:4326", "EPSG:%d" % c["epsg"], always_xy=True)
r = ET.parse("map.osm").getroot(); nodes = {}
for n in r.iter("node"):
    e, nn = t.transform(float(n.get("lon")), float(n.get("lat"))); nodes[n.get("id")] = (e - c["sw_e"], nn - c["sw_n"])
boxes = unary_union([Polygon([nodes[q.get("ref")] for q in w.findall("nd")]) for w in r.iter("way")
                     if any(q.get("k") == "golf" and q.get("v") == "tee" for q in w.findall("tag"))])
d = json.load(open(gkd, encoding="utf-8-sig"))
def pad(x, z, a):
    return Polygon([(x + dx * math.cos(a) - dz * math.sin(a), z + dx * math.sin(a) + dz * math.cos(a)) for dx, dz in ((-4.5, -3.5), (4.5, -3.5), (4.5, 3.5), (-4.5, 3.5))])
for h in d["Holes"]:
    T = {x["TeeType"]: x for x in h["Tees"]}; g = T["GreenCenterPoint"]["Position"]
    for name in ("Black", "Blue", "White", "Yellow"):
        p = T[name]["Position"]
        if not p or boxes.buffer(-1.0).contains(Point(p["x"], p["z"])):
            continue                                     # sits on a mapped box: no pad
        nxt = [T[k]["Position"] for k in ("AimPoint1", "AimPoint2") if T[k]["Enabled"] and T[k]["Position"]] + [g]
        a = math.atan2(nxt[0]["z"] - p["z"], nxt[0]["x"] - p["x"])
        if pad(p["x"], p["z"], a).distance(boxes) >= 1.5:
            continue
        box_ahead = boxes.distance(Point(p["x"] + 6 * math.cos(a), p["z"] + 6 * math.sin(a))) < boxes.distance(Point(p["x"] - 6 * math.cos(a), p["z"] - 6 * math.sin(a)))
        step = -0.5 if box_ahead else 0.5               # slide away from the box
        for k in range(1, 61):
            x, z = p["x"] + k * step * math.cos(a), p["z"] + k * step * math.sin(a)
            if pad(x, z, a).distance(boxes) >= 1.5:
                p.update(x=round(x, 3), z=round(z, 3))
                pts = [p] + ([q for q in nxt[:-1]] if h["Par"] > 3 else []) + [g]
                T[name]["Distance"] = round(sum(math.hypot(u["x"] - v["x"], u["z"] - v["z"]) for u, v in zip(pts, pts[1:])), 3)
                print("hole %d %s pad cleared off the mapped box: moved %.1f m, now %d yds" % (h["HoleNumber"], name, abs(k * step), round(T[name]["Distance"] / 0.9144)))
                break
json.dump(d, open(gkd, "w"), separators=(",", ":"))
