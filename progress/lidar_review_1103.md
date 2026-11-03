# LiDAR detail review (D1-D18), Hansen Dam, 2026-11-03

Headless draft from the data in this folder, following `course-build-lidar-review` and playbook 20/20a. Answers per hole are in
`course_photos/decisions.csv` (324 per-hole rows + 18 course-level rows, `hole = all`); the in-person captures are in
`course_photos/visit_list.md`. Nothing was changed in the GKD, SVG or heightmap. `course.json` has `visit: none`; the visit
list says what a visit would close. Skill rule: D7 and D13 must be closed before anything is playable; the rest may sit on
defaults until the visit.

Survey: USGS 3DEP `CA_LosAngeles_1_B23`, QL1 2023-24, 21.7 pts/m2 (course.json `lidar`), no vegetation classes. Note the
skill text still lists Hansen Dam under the 2018 QL2 survey; this course was rebuilt on the QL1 survey (README) and the QL1
column applies.

## Counts (per-hole rows, 18 x 18)

| decided_by | confidence | rows | points |
|---|---|---|---|
| data | high (settled) | 85 | D3 where no cells over 35 deg (13 holes), D8 (16), D11 (18), D12 (18), D13 (16), D17 (4) |
| data | medium/low (drafted) | 167 | D1, D3 on 5 holes, D4, D5, D7, D8 on 4/18, D10, D13 on 5/17, D15, D16, D17 (14), D18 |
| default | | 72 | D2, D6, D9, D14 on every hole |

## What the QL1 data settled outright

- **D8 green outline vs pad**: all 18 SVG outlines sit on their LiDAR pad (16 at 98-100% of the outline on the connected
  flat under 7%, 18 at 88%, 4 on a 4.4% tilted green with no flat). No green-mesh offset to fix. The shift fit was
  ill-posed on these flat pads (best shift always hit the 3 m search edge) and was not used.
- **D11 water**: one pond (hole 16). LiDAR level Unity y 80.59 (elev 287.6 m); 72% of the 3,005 m2 OSM outline reads within
  0.3 m of it, the rest is the treed peninsula and the margins (to 82.0). No low cells outside the outline. The GKD penalty
  area follows the outline within 0.77 m mean (one vertex 7.6 m off at the N tip), no DZ.
- **D12 creeks**: none cross a hole. The OSM intermittent drain beside the 11 Black tee leaves no channel in the heightmap.
  Big Tujunga culverts, the spillway, Lopez Creek, the spreading grounds and Middle Lake are all outside the 80 m corridors.
- **D16 layer order (SVG side)**: zero bunker-in-green, tee-in-green, tee-in-bunker, water-under-turf and zero tees
  straddling the fairway edge on all 18 holes. The Unity clip-order, vertex-paint and z-fight scans still need the PC.
- **D17 decks**: every one of the 72 GKD tees is inside a Tee shape; 49 sit on mapped OSM boxes, each with a LiDAR deck
  (two-deck boxes on 2 Black, 5 White/Blue). The 23 card-placed tees are on drawn 9x7 pads, see open questions.
- **D3**: 13 holes have no cell over 35 deg within 60 m of the line, so there is no rock question on them.

## Registration shifts (D13)

| pair | shift | note |
|---|---|---|
| OSM cart paths (cartpaths.csv) vs satellite | +1.0 m E, 0.0 m N | brightness 138.6 vs 133.3 at zero; weak signal under canopy |
| OSM bunker outlines (course.svg) vs satellite sand | +1.0 m E, 0.0 m N | 132.5 vs 131.5 at zero; per-bunker fits mostly +0.5 m E |
| GKD tee y vs heightmap | mean -0.01 m | max 1.05 m: 5 Yellow at (883, 2481) sits 1.05 m below the heightmap (card-placed pad on a 12% slope); 17 White +0.37 m |
| GKD tee y vs 0.5 m surface | mean -0.009 m (72 tees) | |
| SVG green centroid vs GKD green centre | 0.2-3.5 m | the GKD centre is the OSM pin node, not the centroid; not a shift |
| OSM vs LiDAR (horizontal) | not measurable | bunker depressions on the 1.66 m grid are 0.1-0.6 m deep and blurred; green pads are flat |

OSM is within about 1 m east of the satellite; the satellite and heightmap share the EPSG:6340 frame in course.json
(no copied constant). No scan or photo GPS exists yet.

## What the data could not do (said so in the rows)

- **D4/D5 to QL1 precision**: `surfaces/surface_05m.npz` covers greens + 6 m, fairways + 5 m and tees + 3 m, not bunkers
  (coverage 0-77% per bunker, 2 of 44 over 90%). The 1.66 m heightmap under-reads bunkers like QL2: greenside median
  rim-to-floor 0.32 m (35 bunkers), fairway 0.19 m (9), max 1.17 m (4 bunker_3). bunkers.csv plan depths (0.8-1.5 m
  greenside) are therefore defaults, not measured. Fix: rebuild the 0.5 m surface with bunkers + 3 m in the mask
  (`scripts/surfaces_05m.py`), which needs `points.npz` (1.9 GB, not in git).
- **D14 roof blocks**: the heightmap is bare earth; roofs need `points.npz`. OSM positions are listed per hole as candidates.
- **D1 cover masks**: `terrain_masks/*.mask` (coursekit) were not read (binary format); D1 shares are satellite tone + slope.
- The satellite date is not recorded in course.json; D2 and D4 confidence depends on it.

## Odd things found

- **Bunkers with little sand in the satellite** (D4): 14 of 44 OSM bunkers show sand on under 50% of the outline:
  12 bunker_32 (0%), 17 bunker_42 (0%), 3 bunker_4 (1%), 10 bunker_21 (2%), 11 bunker_23 (7%), 7 bunker_14 (16%),
  10 bunker_22 (19%), 5 bunker_6 (21%), 18 bunker_40 (23%), 11 bunker_24 (31%), 16 bunker_37 (33%), 11 bunker_25 (36%),
  2 bunker_16 (40%), 8 bunker_13 (41%). Some are shaded or grassed over, some may not exist any more (Tierra 16 case).
- **Card-placed tees on sloping ground** (D17): 9 of the 23 drawn pads sit on ground over 4% with no LiDAR flat under
  them: 1 White (10%), 4 Yellow (4%), 5 Yellow (12%), 6 White (6%), 11 Black (6%, on the dam toe, 7 m fall in 30 m),
  13 White (5%), 16 Yellow (8%), 17 Yellow (5%), 18 Yellow (6%). The real tee for those colours is on a mapped box or an
  unmapped deck. the 17 White tee shape (63 m2) reads 19% local slope and 1.8 m height range: check that box.
- **Greens over 3%** (green_report.py, D7): 2 (3.3%), 3 (3.1%), 4 (4.4%, relief 1.77 m), 6 (3.3%), 9 (3.1%), 18 (5.1%)
  flagged steep; 4 and 18 fail all four pins, 2/6/9 fail three. Pins also fail on 1, 3, 5, 11 (one each). 9 greens FAIL the
  report (1, 2, 3, 4, 5, 6, 9, 11, 18); 9 PASS. Pins must move to the usable areas before the gate; no green is smoothed below the LiDAR.
- **Flyover gate** (toolkit_first_run.md): 2, 3, 9 fail because the opening is not clear within 6 m (trees 542, 872, 34 on
  the tee line; 9 shows a negative rise through the crown, a likely tree-vs-shrub or crown-radius misread, D18); 7, 15, 17
  (par 3s) fail on green visibility (72-84%) because the path is short. gate_report: 6 holes FAIL, 12 PASS, pin warnings on 9.
- **Sheldon Pit**: a 37 m deep quarry (OSM landuse=quarry) directly south of the 18 back tees, inside the LiDAR square. It
  gives the 2,921 m2 of cells over 35 deg on 18 and 5,694 m2 over 15 deg. Real ground: keep it, fence it, do not fill it.
- **Dam embankment**: the 11 tees sit at the dam toe (Black at elev 322 m, the highest tee); 6,259 m2 over 15 deg left of
  the 11 line, 350 m2 over 35 deg with 24 pale cells (spillway side). Skyline north of 10-12.
- **NW hill above 4/5**: 3,553 m2 over 15 deg left of the 4 line, 427 m2 over 35 deg with 84 shrub hits: scrub, no pale rock.
- **Hole 4 green** is 1.1 m below the bank behind it (D10), as is 3; **hole 10** has a 3.2 m rise behind the green with 26%
  surround slope; these are the only banks worth a photo check against the LiDAR.
- **Hole 2 Yellow** GKD 459 yd vs card 436 (tee_colours.csv); **8 White** 362 vs 355; **16 White** 326 vs 318.
- 11 White and Blue mapped boxes are small (65 and 49 m2) and show no 40 m2 deck in the 0.15 m histogram.

## Holes with open questions (beyond the defaults every hole carries)

| hole | open |
|---|---|
| 1 | White tee on 10% ground; green pins 1/4; 15 trees within 35 m, 11 over 16 m |
| 2 | green 3.3% (3 pins fail); fairway bunker_16 40% sand, bunker_15 sand 33 m2 outside; flyover opening (tree 542); Yellow 459 vs 436 |
| 3 | green 3.1%; bunker_4 (46 m2) shows no sand and reads above its rim (gone?); bank 1.1 m behind; Black 404 card-placed behind the box; flyover opening (tree 872) |
| 4 | green 4.4%, all pins fail; NW hill scrub/rock left; four bunkers; Yellow on sloping pad; bank 1.1 m behind |
| 5 | Yellow pad on 12% ground and 1.05 m below the heightmap; bunker_6 21% sand; green 2.8%, 1 pin |
| 6 | green 3.3% (3 pins); White and Yellow card-placed; bank right 1,326 m2 over 15 deg |
| 7 | bunker_14 16% sand; corridor 53% tan (dry); flyover green 72% |
| 8 | bunker_13 41% sand with 84 m2 outside; green drops 1.6 m behind |
| 9 | green 3.1% (3 pins); flyover crown of tree 34; White/Yellow card-placed |
| 10 | both fairway bunkers near no sand (2%, 19%); 3.2 m rise behind the green; clubhouse/range props |
| 11 | Black on the dam toe; bunkers 23/24/25 little sand; dam face cover; drain at the tee |
| 12 | fairway bunker_32 0% sand; bunker_28 sand 94 m2 outside; three card-placed tees |
| 13 | White pad on 5% ground; Wentworth St houses east; 13 broadleaf trees under 16 m |
| 14 | three small greenside bunkers (41-48 m2), 60-75% sand; Yellow pad 11.7% p90 |
| 15 | Black card-placed; flyover green 84% |
| 16 | pond extent on the peninsula side; bunker_37 33% sand; Yellow on 8% ground; bank cuts over 35 deg |
| 17 | bunker_42 0% sand; White box 19% slope; flyover green 79% |
| 18 | green 5.1%, all pins fail; Sheldon Pit; fairway bunker_40 23% sand with 80 m2 outside; Yellow pad 6% |

## Ranked risks for a first build

1. **Bunker depth and face are unmeasured** (D5): every plan depth is a default and the heightmap reads 0.1-0.6 m. Build to the
   rule depths once and leave them (as the skill says), but 14 bunkers may not even exist as sand (D4). Fix first: rebuild
   `surfaces/` with bunkers from `points.npz`, then the sand mask against the satellite per bunker.
2. **Seven steep greens** (2, 3, 4, 6, 9, 18 plus 11 at 2.95%): 4 and 18 have no legal pin. Pins must move to the usable
   areas; the surfaces stay LiDAR until a scan. D7 is a must-close point.
3. **Nine tee colours on invented pads on sloping ground** (D17): 1 W, 4 Y, 5 Y, 6 W, 11 Bk, 13 W, 16 Y, 17 Y, 18 Y. These
   will read as cut shelves in a hillside (the Tierra 4 "crater"). Park them on the nearest mapped box until the visit.
4. **Hillside cover on 4, 11, 18 and the dam** (D1/D3): 15% of the 11 corridor and 13% of the 4 and 18 corridors are over
   15 deg; the satellite shows no pale rock, so scrub on soil by default, but colour and soil share need a photo. The Tierra
   misread #1.
5. **Trees on the tee line and tree-vs-shrub** (D18): flyover openings fail on 2, 3, 9 through crowns; 7,491 LiDAR shrubs
   with 0 vegetation classes in the survey; species are guesses. Nudge, never delete, and photograph every tree within 35 m.
6. Registration is clean (D13) and nothing here needs a shift, but the satellite date is unrecorded; record it in course.json.
