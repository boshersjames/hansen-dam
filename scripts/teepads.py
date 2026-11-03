"""Every GKD tee sits on a flat Tee pad in course.svg: tees not >=1.0 m inside a mapped box get a 9 x 7 m pad
(long side along the line of play) with a 2 m first cut of rough cut out of any fairway around it."""
import re, json, math
from shapely.geometry import Polygon, Point, MultiPolygon
from shapely.ops import unary_union
S=json.load(open("course.json"))["size"]; svg=open("course.svg").read()
svg=re.sub(r'<path id="tee_card_\d+"[^>]*/>\n','',svg)          # earlier 8 x 6 pads
def block(label):
    i=svg.find('inkscape:label="%s"'%label); return i, svg.find("</g>",i)
def layer(label):
    i,j=block(label); out=[]
    for d in re.findall(r' d="([^"]+)"',svg[i:j]):
        rings=[]
        for sp in re.split(r"(?=M )",d.strip()):
            n=[float(v) for v in re.findall(r"-?\d+\.?\d*",sp)]; pts=[(n[k],S-n[k+1]) for k in range(0,len(n)-1,2)]
            if len(pts)>2: rings.append(Polygon(pts).buffer(0))
        if rings:
            rings.sort(key=lambda p:-p.area); g=rings[0]
            for r in rings[1:]: g=g.symmetric_difference(r)
            out.append(g)
    return unary_union(out)
def paths(geom,pid,col):
    gs=list(geom.geoms) if isinstance(geom,MultiPolygon) else [geom]; out=[]
    for k,g in enumerate(gs):
        if g.is_empty or g.area<1: continue
        loops=[]
        for ring in [g.exterior]+list(g.interiors):
            loops.append("M "+" L ".join("%.3f,%.3f"%(x,S-y) for x,y in list(ring.coords)[:-1])+" Z")
        out.append('<path id="%s_%d" style="fill:%s;fill-opacity:1;fill-rule:evenodd;stroke:none" d="%s"/>'%(pid,k,col," ".join(loops)))
    return "\n".join(out)
tee=layer("Tee"); d=json.load(open("HansenDam.GKD")); pads=[]; log=[]
for h in d["Holes"]:
    T={t["TeeType"]:t for t in h["Tees"]}; gc=T["GreenCenterPoint"]["Position"]
    for name in ("Black","Blue","White","Yellow"):
        p=T[name]["Position"]
        if not p or tee.buffer(-1.0).contains(Point(p["x"],p["z"])): continue
        nxt=[T[a]["Position"] for a in ("AimPoint1","AimPoint2") if T[a]["Enabled"] and T[a]["Position"]]+[gc]
        q=nxt[0]; a=math.atan2(q["z"]-p["z"],q["x"]-p["x"])
        pads.append(Polygon([(p["x"]+dx*math.cos(a)-dz*math.sin(a),p["z"]+dx*math.sin(a)+dz*math.cos(a)) for dx,dz in ((-4.5,-3.5),(4.5,-3.5),(4.5,3.5),(-4.5,3.5))]))
        log.append("%d %s"%(h["HoleNumber"],name))
pad=unary_union(pads); cut=pad.buffer(2,join_style=2)
fair0=layer("Fairway")
inner=[p.buffer(3.5,join_style=2) for p in pads if p.buffer(2,join_style=2).intersection(fair0).area/p.buffer(2,join_style=2).area>=0.5]
# pads mostly in fairway get a closed fairway ring round the first cut
fair=unary_union([fair0]+inner).difference(cut)
rough=unary_union([layer("Rough"),cut.difference(pad)]); tee2=unary_union([tee,pad])
greens=layer("Green"); bunk=layer("Bunker")
for lab,pid,col,geom in (("Fairway","fairway","#43E561",fair),("Rough","rough","#278438",rough),("Tee","tee","#A0E5B8",tee2.difference(unary_union([greens,bunk])))):
    i,j=block(lab); k=svg.find(">",i)+1
    svg=svg[:k]+"\n"+paths(geom,pid,col)+"\n"+svg[j:]
open("course.svg","w").write(svg)
print(len(pads),"pads:",", ".join(log))
