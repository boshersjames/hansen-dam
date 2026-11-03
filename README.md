# Hansen Dam Golf Course (GSPro build)

Hansen Dam Golf Course, 10400 Glenoaks Blvd, Pacoima (Los Angeles). City of LA municipal 18 holes, par 72, just south of the Hansen Dam embankment. Built with `coursekit.py`. One of the five courses for the OPCD licensed-designer server.

## Frame
- 3400 m square (the course runs 2.5 km east-west, too long for 2000 m), centred on James's pin 34.258618830, -118.390880038. EPSG:6340, SW corner in `course.json`.
- Unity x = metres east, z = metres north, y = elevation - 207 m.
- `heightmap_2049.raw`: 2049 x 2049, 16-bit, Windows byte order. Unity Terrain 3400 x 191 x 3400 (1.66 m per sample). Ground 207.1 to 396.5 m (the high ground is the hills in the NW corner and the dam; the course itself is fairly flat).

## LiDAR
USGS 3DEP `CA_LosAngeles_1_B23` (QL1, 2023-24), 21.7 points/m2, 250.6 M points, noise removed. The survey has no vegetation classes (1 = unclassified, 2 = ground, 9 water, 17 bridge), so trees come from height above ground plus the satellite colour check.

    python ../../coursekit.py lidar --ept CA_LosAngeles_1_B23

`points.npz` (1.9 GB) is not in git.

## Satellite
`satellite.jpg`: NAIP via imagery.nationalmap.gov, 8192 px (0.42 m/px), fetched on the Mac. In Unity: Max Size 8192, Terrain Size 3400.

## Holes
`map.osm` from James (OSM export, 2026-10-28; kept in the project files, not in git because of LFS): 18 hole lines with correct refs and pars, 44 tees, 24 greens, 45 bunkers, 16 fairways, 1 water hazard, range, 19 cart paths (9.5 km, `cartpaths.csv`).
`holes.csv` / `tees.csv`: OSM hole lengths match the black tees within a few percent on every hole.
The mapped golf_course boundary only holds 44% of the holes, so the tree filter ignores it.

## Scorecard (`scorecard.csv`)
Par 4 5 4 3 4 5 3 4 4 | 4 4 5 4 5 3 4 3 4 = 72. Women's par 74 (9 and 13 are par 5).
Black 6801 (72.1/124), Blue 6419 (70.5/120), White 6001 (68.4/116), Yellow 5435 (65.7/109). Women from Black 78.9/135.

## Trees
`trees.csv`: 1,444 LiDAR trees (>= 3 m) near the holes, after the OSM and satellite filters (577 grey/tan crowns dropped). A few sit in the yards east of the back holes; trim in Unity if they show.

## Course drawing (`course.svg`, draft)
`python ../../coursekit.py svg`: greens, tees, 44 bunkers and the pond from OSM, 12.4 ha of OSM fairway plus 3.2 ha traced from the photo, rough = 60 m round the hole lines. Natural water away from the holes (spreading grounds, Tujunga Wash channel, park lake) is left out. Preview `course_svg_preview.png` (project files).

## Tierra lessons applied (James: "bunkers must not play like fairways")
- **Collar:** the SVG puts a 1.5 m ring of fairway-grass round every green so balls just off the green roll out instead of being grabbed by rough. Uphill banks (ground rising > 0.25 m per m away from the green) keep rough; the LiDAR shows none at Hansen Dam (max 0.18 m rise across the collar), so the collar goes all the way round.
- **Bunkers:** every OSM bunker is its own Bunker-layer shape (never merged into fairway). In the OPCD/Unity build keep them shallow with flat floors so balls settle (Lower Terrain Under Meshes 1 m like Tierra, not deeper), bunker material = Sand Raked Dirt Lip Thin with the sand physics material, and test a ball into a greenside and a fairway bunker before publishing: it should stop in the sand and need loft to get out.

## BoJa feedback checklist pass (10/28; second pass adds: all 2,021 LiDAR trees kept with no satellite colour drop, traced fairways smoothed with smooth_fairways.py, 23 tee pads drawn under the card-placed tees, par 3s aim at the green, altitude 993 ft, Parkland keyword, Designer field "jboshers" (BoJa's choice for every course; the architect, Ray Goates 1964, is credited in the approved CourseInfo description), see /mnt/project-files/course-build/BOJA_FEEDBACK_CHECKLIST.md)
- Collars now 3 m at the sides and 5 m behind each green (along the hole line); rough on uphill banks (none found). Deep rough kept 6 m off greens.
- `checks/green_slopes.csv`: plane tilt and 95th-percentile local slope inside each green from LiDAR ground points. Over 3% tilt: hole 2 (3.0), 4 (4.3), 6 (3.3), 18 (5.3), plus one practice green. Review these in the flyover; flatten in the green mesh if they play too steep.
- `bunkers.csv` (from the shared surrounds.py, size constant set from course.json): depth by size, flat floor, steep face toward its green, for all bunkers; no fairway/rough/deep overlaps sand; 2 m rough lip. Collars redone after fairway smoothing; 472 m2 of collar dropped on uphill banks.
- `HansenDam.GKD` (`coursekit.py card --line-tees --ob`, template Moorpark): four colours on their own spots on every hole (never stacked); 49 of 72 sit on mapped OSM tee boxes, 23 are placed on the hole line at the card yardage (`checks/tee_colours.csv`). Black on 3 (404) and 11 (340) are behind the mapped start and need a look. Totals: Black 6786, Blue 6418, White 6016, Yellow 5461 yds vs card 6801/6419/6001/5435.
- Draft OB: one boundary (527 points), 16 interior OB patches in brush/trees between holes so big misses don't land on another hole, 1 pond hazard (no drop zones yet). Thin slivers dropped. All tees, aims and pins in bounds. Preview `ob_preview.jpg` (project files).
- `checks/cross_hole_spots.csv`: places where two hole lines run within 45 m (4/5, 6/7 tee, 14/15 tee).
- Tee pads (order matters): `scripts/fix_box_tees.py HansenDam.GKD heightmap_2049.raw` puts tees near a mapped box onto the box 1.2 m inside its edge; `scripts/clear_pads.py HansenDam.GKD` slides any card-placed tee whose pad would touch a mapped box until it is 1.5 m clear (OPCD drops tee shapes merged with a box: 17 White); `scripts/pads_off_fairway_edge.py HansenDam.GKD course.svg` slides pads that straddle the fairway edge or sit within 2 m of a cart path (cartpaths.csv) until clear, `scripts/box_tees_inward.py` keeps box tees 1.5 m inside the box, and `scripts/teepads.py` then draws a flat 9 x 7 m pad (long side along the line of play) with a 2 m first cut for every tee not 1 m inside a box. 18 pads, none touching a mapped box, all 72 tees 1 m+ inside a Tee shape.
- Still for the PC build: bunker depth and sand material, greens stimp ~10 Normal, moderate fairway firmness, cart path colour and 4 cm lift, tree LOD/billboards and canopy colliders, terrain backdrop past the 3.4 km square, own Unity project C:\GSP\HansenDam_Project.

## Shape and realism pass (BoJa review 10/29: "missing a lot is slope, bunker depth and overall realism")
- `surfaces/`: 0.5 m bare-earth surface from the raw LiDAR ground points over greens + 6 m, fairways + 5 m and tees + 3 m (see surfaces/README.md). Conform the playing-surface meshes to it.
- `bunkers.csv` (scripts/bunker_plan.py): 35 greenside bunkers 0.8-1.5 m deep by size, face toward the green at 55 deg, raised lip 0.2-0.4 m; 9 fairway bunkers 0.4-0.64 m, 35 deg face, 0.1 m lip; flat floor over the inner 60 %.
- `trees.csv` species column (scripts/tree_species.py, LiDAR return profile + crown shape + photo colour, guided by the flyover): palm 76 (16 along hole 16; Mexican fan palms on 12, 15, 16 and the clubhouse), pine 311, eucalyptus 255, broadleaf 1,351 (sycamore, coast live oak). Estimate only, with a confidence column.
- Hole 16 pond: the OSM outline already follows both lobes and the treed peninsula on the satellite (0.30 ha); GKD hazard is a penalty area (innerOOB false, no drop zone, GSPro flag-line/lateral drops). Water colour from BoJa's aerial: #669E7D (teal green).
- Hole 11 plays the right-hand green (1909, 1630). The unused left green (OSM 375791471, 1963, 1650) is re-layered as fairway in course.svg. The greens at 1847,1695 and 1875,1686 (with a bunker, beside the parking and the 10th tee), 1690,1655 and the two at 1731 by the clubhouse are practice greens: kept.
- `backdrop/`: 36 km square far terrain (USGS 3DEP 1/3 arc-second, 17.6 m per sample) centred on the course for the horizon: San Gabriels N/NE, Verdugos SE, Santa Monica Mountains S, the dam. Placement in backdrop/backdrop.json. Script: scripts/backdrop.py.

## Off-course trees (10/29)

`offsite_trees.csv`: 1,958 LiDAR trees outside the course, out to 300 m past the GKD out-of-bounds line (the OSM golf_course area is another facility) or to the frame edge, for the neighbourhood the PC builds from OSM (east of 13-17 along Wentworth St, the houses west of 1-5, the dam slope). Same columns as `trees.csv`, including species (palm 111, pine 147, eucalyptus 210, broadleaf 1,490). `trees.csv` is untouched; anything within 3 m of a course tree is left out so nothing doubles. Roofs are masked from LiDAR smoothness and OSM buildings, and roof-edge/car peaks by the satellite colour. Made by `scripts/offsite_trees.py` then `scripts/tree_species.py offsite_trees.csv`; preview `offsite_trees_on_satellite.png`.
