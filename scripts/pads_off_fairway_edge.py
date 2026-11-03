"""A pad must stay 2 m clear of cart paths (cartpaths.csv, path ~2.5 m wide) and never straddle the fairway edge (OPCD fills tee-shaped notches with fairway). Card-placed tees whose
pad + 2 m ring is partly in fairway (2-50 %) slide sideways, away from the fairway, up to 8 m until clear.
Pads mostly in fairway are enclosed by teepads.py instead. Run after clear_pads.py, before teepads.py.
Usage: python scripts/pads_off_fairway_edge.py HansenDam.GKD course.svg"""
import json, math, re, sys, xml.etree.ElementTree as ET
from pyproj import Transformer
from shapely.geometry import Polygon, Point
from shapely.ops import unary_union
gkd, svgp = sys.argv[1], sys.argv[2]; c = json.load(open("course.json")); S = c["size"]
s = open(svgp).read()
def layer(label):
    i = s.index('inkscape:label="%s"' % label); j = s.index('</g>', i); out = []
    for d in re.findall(r' d="([^"]+)"', s[i:j]):
        rings = []
        for sp in re.split(r"(?=M )", d.strip()):
            n = [float(v) for v in re.findall(r"-?\d+\.?\d*", sp)]; pts = [(n[k], S - n[k + 1]) for k in range(0, len(n) - 1, 2)]
            if len(pts) > 2: rings.append(Polygon(pts).buffer(0))
        if rings:
            rings.sort(key=lambda p: -p.area); g = rings[0]
            for r in rings[1:]: g = g.symmetric_difference(r)
            out.append(g)
    return unary_union(out)
fw = layer("Fairway")
t = Transformer.from_crs("EPSG:4326", "EPSG:%d" % c["epsg"], always_xy=True)
r = ET.parse("map.osm").getroot(); nodes = {}
for n in r.iter("node"):
    e, nn = t.transform(float(n.get("lon")), float(n.get("lat"))); nodes[n.get("id")] = (e - c["sw_e"], nn - c["sw_n"])
boxes = unary_union([Polygon([nodes[q.get("ref")] for q in w.findall("nd")]) for w in r.iter("way")
                     if any(q.get("k") == "golf" and q.get("v") == "tee" for q in w.findall("tag"))])
def ring(x, z, a):
    return Polygon([(x + dx * math.cos(a) - dz * math.sin(a), z + dx * math.sin(a) + dz * math.cos(a)) for dx, dz in ((-6.5, -5.5), (6.5, -5.5), (6.5, 5.5), (-6.5, 5.5))])
import csv
from shapely.geometry import LineString
segs = {}
for row in csv.DictReader(open("cartpaths.csv")):
    segs.setdefault(row["segment"], []).append((float(row["x"]), float(row["z"])))
paths = unary_union([LineString(v) for v in segs.values() if len(v) > 1]).buffer(1.25)
def pad(x, z, a):
    return Polygon([(x + dx * math.cos(a) - dz * math.sin(a), z + dx * math.sin(a) + dz * math.cos(a)) for dx, dz in ((-4.5, -3.5), (4.5, -3.5), (4.5, 3.5), (-4.5, 3.5))])
def ok(x, z, a):
    R2 = ring(x, z, a)
    fr = R2.intersection(fw).area / R2.area
    return (fr <= 0.02 or fr >= 0.6) and R2.buffer(-2).distance(boxes) >= 1.5 and pad(x, z, a).distance(paths) >= 2.0
d = json.load(open(gkd, encoding="utf-8-sig"))
for h in d["Holes"]:
    T = {x["TeeType"]: x for x in h["Tees"]}; g = T["GreenCenterPoint"]["Position"]
    for name in ("Black", "Blue", "White", "Yellow"):
        p = T[name]["Position"]
        if not p or boxes.buffer(-1.0).contains(Point(p["x"], p["z"])):
            continue
        nxt = [T[k]["Position"] for k in ("AimPoint1", "AimPoint2") if T[k]["Enabled"] and T[k]["Position"]] + [g]
        a = math.atan2(nxt[0]["z"] - p["z"], nxt[0]["x"] - p["x"])
        R = ring(p["x"], p["z"], a); f = R.intersection(fw).area / R.area
        on_path = pad(p["x"], p["z"], a).distance(paths) < 2.0
        if not (0.02 < f < 0.5 or (on_path and f < 0.5)):
            continue
        best = None
        for side in (1, -1):                              # sideways, then along the line of play
            for k in range(1, 81):
                for ux, uz in ((-math.sin(a), math.cos(a)), (math.cos(a), math.sin(a))):
                    off = side * k * 0.25; x, z = p["x"] + off * ux, p["z"] + off * uz
                    if ok(x, z, a) and (best is None or abs(off) < abs(best[0])): best = (off, x, z)
                if best: break
        if best:
            off, x, z = best; p.update(x=round(x, 3), z=round(z, 3))
            pts = [p] + (nxt[:-1] if h["Par"] > 3 else []) + [g]
            T[name]["Distance"] = round(sum(math.hypot(u["x"] - v["x"], u["z"] - v["z"]) for u, v in zip(pts, pts[1:])), 3)
            print("hole %d %s pad moved %.1f m clear of the fairway edge / cart path (%d yds)" % (h["HoleNumber"], name, abs(off), round(T[name]["Distance"] / 0.9144)))
        else:
            print("hole %d %s pad still straddles the fairway edge (%.0f%%): fix by hand" % (h["HoleNumber"], name, 100 * f))
json.dump(d, open(gkd, "w"), separators=(",", ":"))
