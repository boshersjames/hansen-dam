# Hansen Dam: in-person visit list (from the LiDAR review, 2026-11-03)

Written from `course_photos/decisions.csv` before any visit. Captures follow `course-build-site-visit` (tee boxes, tee surrounds, hillsides, bunkers, greens, water, trees within 35 m, props, boundary, once-per-course). `course.json` has `visit: none`; this list is what a visit would close. Walk in hole order; two photos per spot 10 s apart, landscape, eye height, a landmark in frame.

What the QL1 data already settles (no capture needed): green outlines on their pads (D8), the pond level and extent (D11), no creeks (D12), registration (D13), layer order in the SVG (D16), which mapped boxes carry a LiDAR deck (D17). What only the visit answers: cover colour and soil share (D1), rock vs scrub (D3), grass in sand (D6), collars (D9), props under 1 m (D14), species (D18), which colour plays which deck (D17), and a phone LAS per green (D7).

## Course-level, once

- Skyline from the highest tee: 11 Black (elev 322 m on the dam toe) toward the course and the San Gabriels; also from 4 tee (NW hill) and 18 tee (Sheldon Pit south). Pass: skyline fit under 10 px (D15).
- Sand colour: white card in the sand in the same light, once (D6/look). Also the card against a cart path for concrete.
- Clubhouse: each side, doors, cart staging, the starter hut, the range tee line (OSM: roof at (1712, 1724), parking (1740, 1667), range (1773, 1855)). Practice greens by 10 tee and the clubhouse (five, kept) (D14).
- A pin flag and a tee marker up close; the scorecard; the entrance drive off Glenoaks Blvd.
- Hansen Dam embankment face from 10/11/12: one eye-level photo for cover class (grass vs riprap vs scrub) (D1/D3).
- Sheldon Pit quarry edge south of the 18 tees: one photo across it for the fence line and cover (D1/D15).
- Toilets/shelters OSM lists: (1024, 2161) between 2 green and 6 tee, (1289, 2488) shelter and (1247, 2531) toilets by the campground west of 4/5, (3238, 1822) north of 13. Photo each with a landmark (D14).
- Rangefinder log on every tee: hole, tee, target, reading, plays-like, pin. The card runs long; do not move tees to match it.

## Hole 1

**Tee boxes (D17, signs, markers)**
- Every box: down the line from the back with markers, across the deck edge/bank, note which colour is on which deck. Confirm: White on 10% ground, no LiDAR flat: the real tee is elsewhere

**Tee surrounds and props (D14)**
- Hole sign square-on from 3 m, tee markers, bins, benches, ball washers, ropes at every box (D14). OSM candidates to confirm: building=yes at (1689, 1696); building=yes at (1343, 1720); building=roof at (1712, 1724); building=yes at (1727, 1714)

**Bunkers (D4, D5, D6)**
- bunker_18(csv 26,greenside,226 m2) at (1356, 1799): heightmap depth 0.29 m vs plan 1.42 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).
- bunker_20(csv 24,greenside,176 m2) at (1353, 1752): heightmap depth 0.43 m vs plan 1.25 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).

**Green (D7, D8, D9, D10)**
- LAS scan of the green plus 3 m of collar (lanes 1.5 m apart). Slope report: mean 2.28%, p90 3.48%, 1/4 pins fail. Photo of the collar from the fringe and low along the edge toward each bunker (D7, D8, D9).

**Trees within 35 m (D18)**
- 15 LiDAR trees within 35 m of a tee or the green (11 over 16 m; draft pine 9, eucalyptus 2, broadleaf 4): one photo each from the tee side with scale, close enough for species; note dead/missing. 2 shrubs at/over 3 m near the tees/green: tree or shrub? (D18)

## Hole 2

**Tee boxes (D17, signs, markers)**
- Every box: down the line from the back with markers, across the deck edge/bank, note which colour is on which deck. All four colours on mapped boxes with a LiDAR deck.

**Tee surrounds and props (D14)**
- Hole sign square-on from 3 m, tee markers, bins, benches, ball washers, ropes at every box (D14). OSM candidates to confirm: building=yes at (1343, 1720); building=yes at (1024, 2161); building=industrial at (1279, 1684); building=yes at (1349, 1683)

**Bunkers (D4, D5, D6)**
- bunker_9(csv 4,greenside,159 m2) at (1022, 2106): heightmap depth 0.26 m vs plan 1.20 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).
- bunker_10(csv 5,greenside,145 m2) at (1063, 2107): heightmap depth 0.34 m vs plan 1.15 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).
- bunker_15(csv 1,fairway,169 m2) at (1201, 1919): satellite sand runs 33 m2 outside the OSM outline / best shift 1.6 m. Photo from the fairway side showing the sand line (D4).
- bunker_15(csv 1,fairway,169 m2) at (1201, 1919): heightmap depth 0.34 m vs plan 0.52 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).
- bunker_16(csv 0,fairway,248 m2) at (1149, 1916): satellite shows sand on only 40% of the OSM outline. Photo from the fairway side and across the floor: does it exist, is it sand or grassed over (D4).
- bunker_16(csv 0,fairway,248 m2) at (1149, 1916): heightmap depth 0.32 m vs plan 0.63 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).

**Green (D7, D8, D9, D10)**
- LAS scan of the green plus 3 m of collar (lanes 1.5 m apart). Slope report: mean 3.29%, p90 5.03%, 3/4 pins fail - steep >3%. Photo of the collar from the fringe and low along the edge toward each bunker (D7, D8, D9).

**Trees within 35 m (D18)**
- 13 LiDAR trees within 35 m of a tee or the green (8 over 16 m; draft pine 6, broadleaf 6, eucalyptus 1): one photo each from the tee side with scale, close enough for species; note dead/missing. 0 shrubs at/over 3 m near the tees/green: tree or shrub? (D18)

## Hole 3

**Tee boxes (D17, signs, markers)**
- Every box: down the line from the back with markers, across the deck edge/bank, note which colour is on which deck. Confirm: Black card-placed: which deck?

**Tee surrounds and props (D14)**
- Hole sign square-on from 3 m, tee markers, bins, benches, ball washers, ropes at every box (D14). OSM candidates to confirm: amenity=waste_basket at (970, 2078); amenity=shelter at (965, 2041); amenity=waste_basket at (964, 2043); building=yes at (1024, 2161)

**Hillsides and steep ground (D1, D2, D3)**
- Bank/slope left of the line around Unity (777, 2315): 962 m2 over 15 deg. One eye-level photo across it, one along the toe where scrub meets turf (D1, D2, D3).
- Steep cells over 35 deg near Unity (742, 2356), 14 m2: photo framing the face to settle rock vs scrub and its colour (D3).

**Bunkers (D4, D5, D6)**
- bunker_4(csv 10,greenside,46 m2) at (767, 2383): satellite shows sand on only 1% of the OSM outline. Photo from the fairway side and across the floor: does it exist, is it sand or grassed over (D4).
- bunker_4(csv 10,greenside,46 m2) at (767, 2383): heightmap depth -0.31 m vs plan 0.82 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).
- bunker_5(csv 9,greenside,136 m2) at (802, 2360): heightmap depth 0.31 m vs plan 1.12 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).
- bunker_7(csv 7,fairway,256 m2) at (866, 2247): heightmap depth 0.32 m vs plan 0.64 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).

**Green (D7, D8, D9, D10)**
- LAS scan of the green plus 3 m of collar (lanes 1.5 m apart). Slope report: mean 3.07%, p90 4.21%, 1/4 pins fail - steep >3%. Photo of the collar from the fringe and low along the edge toward each bunker (D7, D8, D9).
- Bank behind/beside the green (rise 1.1 m, surround slope up to 20.3%): photo of the bank with scale (D10).

**Trees within 35 m (D18)**
- 19 LiDAR trees within 35 m of a tee or the green (7 over 16 m; draft pine 3, broadleaf 14, eucalyptus 2): one photo each from the tee side with scale, close enough for species; note dead/missing. 2 shrubs at/over 3 m near the tees/green: tree or shrub? (D18)

## Hole 4

**Tee boxes (D17, signs, markers)**
- Every box: down the line from the back with markers, across the deck edge/bank, note which colour is on which deck. Confirm: Yellow on 4% ground, no LiDAR flat: the real tee is elsewhere

**Tee surrounds and props (D14)**
- Hole sign square-on from 3 m, tee markers, bins, benches, ball washers, ropes at every box (D14). OSM candidates to confirm: building=house at (724, 2601); building=retail at (712, 2310)

**Hillsides and steep ground (D1, D2, D3)**
- Bank/slope left of the line around Unity (749, 2496): 3553 m2 over 15 deg. One eye-level photo across it, one along the toe where scrub meets turf (D1, D2, D3).
- Steep cells over 35 deg near Unity (756, 2541), 427 m2: photo framing the face to settle rock vs scrub and its colour (D3).

**Bunkers (D4, D5, D6)**
- bunker_0(csv 14,greenside,266 m2) at (815, 2585): heightmap depth 0.62 m vs plan 1.50 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).
- bunker_1(csv 13,greenside,168 m2) at (779, 2566): satellite sand runs 58 m2 outside the OSM outline / best shift 1.0 m. Photo from the fairway side showing the sand line (D4).
- bunker_1(csv 13,greenside,168 m2) at (779, 2566): heightmap depth 0.63 m vs plan 1.23 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).
- bunker_2(csv 12,greenside,95 m2) at (772, 2547): heightmap depth 0.68 m vs plan 0.98 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).
- bunker_3(csv 11,greenside,332 m2) at (810, 2540): heightmap depth 1.17 m vs plan 1.50 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).

**Green (D7, D8, D9, D10)**
- LAS scan of the green plus 3 m of collar (lanes 1.5 m apart). Slope report: mean 4.39%, p90 6.82%, 4/4 pins fail - steep >3%. Photo of the collar from the fringe and low along the edge toward each bunker (D7, D8, D9).
- Bank behind/beside the green (rise 1.09 m, surround slope up to 22.2%): photo of the bank with scale (D10).

**Trees within 35 m (D18)**
- 26 LiDAR trees within 35 m of a tee or the green (5 over 16 m; draft pine 6, eucalyptus 3, palm 1, broadleaf 16): one photo each from the tee side with scale, close enough for species; note dead/missing. 20 shrubs at/over 3 m near the tees/green: tree or shrub? (D18)

## Hole 5

**Tee boxes (D17, signs, markers)**
- Every box: down the line from the back with markers, across the deck edge/bank, note which colour is on which deck. Confirm: Yellow on 12% ground, no LiDAR flat: the real tee is elsewhere

**Tee surrounds and props (D14)**
- Hole sign square-on from 3 m, tee markers, bins, benches, ball washers, ropes at every box (D14).

**Hillsides and steep ground (D1, D2, D3)**
- Bank/slope left of the line around Unity (890, 2543): 2588 m2 over 15 deg. One eye-level photo across it, one along the toe where scrub meets turf (D1, D2, D3).

**Bunkers (D4, D5, D6)**
- bunker_6(csv 8,greenside,249 m2) at (1075, 2256): satellite shows sand on only 21% of the OSM outline. Photo from the fairway side and across the floor: does it exist, is it sand or grassed over (D4).
- bunker_6(csv 8,greenside,249 m2) at (1075, 2256): heightmap depth 0.67 m vs plan 1.50 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).
- bunker_8(csv 6,greenside,146 m2) at (1035, 2244): satellite sand runs 52 m2 outside the OSM outline / best shift 1.0 m. Photo from the fairway side showing the sand line (D4).
- bunker_8(csv 6,greenside,146 m2) at (1035, 2244): heightmap depth 0.13 m vs plan 1.15 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).

**Green (D7, D8, D9, D10)**
- LAS scan of the green plus 3 m of collar (lanes 1.5 m apart). Slope report: mean 2.75%, p90 4.11%, 1/4 pins fail. Photo of the collar from the fringe and low along the edge toward each bunker (D7, D8, D9).

**Trees within 35 m (D18)**
- 7 LiDAR trees within 35 m of a tee or the green (6 over 16 m; draft eucalyptus 4, broadleaf 3): one photo each from the tee side with scale, close enough for species; note dead/missing. 0 shrubs at/over 3 m near the tees/green: tree or shrub? (D18)

## Hole 6

**Tee boxes (D17, signs, markers)**
- Every box: down the line from the back with markers, across the deck edge/bank, note which colour is on which deck. Confirm: White on 6% ground, no LiDAR flat: the real tee is elsewhere; Yellow card-placed: which deck?

**Tee surrounds and props (D14)**
- Hole sign square-on from 3 m, tee markers, bins, benches, ball washers, ropes at every box (D14). OSM candidates to confirm: building=yes at (1024, 2161)

**Hillsides and steep ground (D1, D2, D3)**
- Bank/slope right of the line around Unity (1329, 2049): 1326 m2 over 15 deg. One eye-level photo across it, one along the toe where scrub meets turf (D1, D2, D3).

**Bunkers (D4, D5, D6)**
- bunker_12(csv 29,greenside,223 m2) at (1476, 1960): heightmap depth 0.31 m vs plan 1.41 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).

**Green (D7, D8, D9, D10)**
- LAS scan of the green plus 3 m of collar (lanes 1.5 m apart). Slope report: mean 3.33%, p90 4.31%, 3/4 pins fail - steep >3%. Photo of the collar from the fringe and low along the edge toward each bunker (D7, D8, D9).

**Trees within 35 m (D18)**
- 15 LiDAR trees within 35 m of a tee or the green (5 over 16 m; draft pine 4, broadleaf 8, eucalyptus 3): one photo each from the tee side with scale, close enough for species; note dead/missing. 1 shrubs at/over 3 m near the tees/green: tree or shrub? (D18)

## Hole 7

**Tee boxes (D17, signs, markers)**
- Every box: down the line from the back with markers, across the deck edge/bank, note which colour is on which deck. All four colours on mapped boxes with a LiDAR deck.

**Tee surrounds and props (D14)**
- Hole sign square-on from 3 m, tee markers, bins, benches, ball washers, ropes at every box (D14).

**Hillsides and steep ground (D1, D2, D3)**
- Bank/slope right of the line around Unity (1495, 2010): 719 m2 over 15 deg. One eye-level photo across it, one along the toe where scrub meets turf (D1, D2, D3).

**Bunkers (D4, D5, D6)**
- bunker_14(csv 28,greenside,178 m2) at (1619, 1943): satellite shows sand on only 16% of the OSM outline. Photo from the fairway side and across the floor: does it exist, is it sand or grassed over (D4).
- bunker_14(csv 28,greenside,178 m2) at (1619, 1943): heightmap depth -0.07 m vs plan 1.26 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).
- bunker_17(csv 27,greenside,130 m2) at (1593, 1918): satellite sand runs 50 m2 outside the OSM outline / best shift 2.2 m. Photo from the fairway side showing the sand line (D4).
- bunker_17(csv 27,greenside,130 m2) at (1593, 1918): heightmap depth 0.08 m vs plan 1.10 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).

**Green (D7, D8, D9, D10)**
- LAS scan of the green plus 3 m of collar (lanes 1.5 m apart). Slope report: mean 2.38%, p90 3.39%, 0/4 pins fail. Photo of the collar from the fringe and low along the edge toward each bunker (D7, D8, D9).

**Trees within 35 m (D18)**
- 7 LiDAR trees within 35 m of a tee or the green (4 over 16 m; draft pine 3, eucalyptus 1, broadleaf 2, palm 1): one photo each from the tee side with scale, close enough for species; note dead/missing. 1 shrubs at/over 3 m near the tees/green: tree or shrub? (D18)

## Hole 8

**Tee boxes (D17, signs, markers)**
- Every box: down the line from the back with markers, across the deck edge/bank, note which colour is on which deck. Confirm: Black card-placed: which deck?; Yellow card-placed: which deck?

**Tee surrounds and props (D14)**
- Hole sign square-on from 3 m, tee markers, bins, benches, ball washers, ropes at every box (D14). OSM candidates to confirm: building=yes at (1679, 1825)

**Bunkers (D4, D5, D6)**
- bunker_11(csv 3,greenside,116 m2) at (1282, 1971): heightmap depth 0.21 m vs plan 1.05 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).
- bunker_13(csv 2,greenside,270 m2) at (1256, 1946): satellite shows sand on only 41% of the OSM outline. Photo from the fairway side and across the floor: does it exist, is it sand or grassed over (D4).
- bunker_13(csv 2,greenside,270 m2) at (1256, 1946): heightmap depth 0.63 m vs plan 1.50 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).

**Green (D7, D8, D9, D10)**
- LAS scan of the green plus 3 m of collar (lanes 1.5 m apart). Slope report: mean 1.82%, p90 3.3%, 0/4 pins fail. Photo of the collar from the fringe and low along the edge toward each bunker (D7, D8, D9).

**Trees within 35 m (D18)**
- 8 LiDAR trees within 35 m of a tee or the green (3 over 16 m; draft eucalyptus 2, palm 2, broadleaf 4): one photo each from the tee side with scale, close enough for species; note dead/missing. 0 shrubs at/over 3 m near the tees/green: tree or shrub? (D18)

## Hole 9

**Tee boxes (D17, signs, markers)**
- Every box: down the line from the back with markers, across the deck edge/bank, note which colour is on which deck. Confirm: White card-placed: which deck?; Yellow card-placed: which deck?

**Tee surrounds and props (D14)**
- Hole sign square-on from 3 m, tee markers, bins, benches, ball washers, ropes at every box (D14). OSM candidates to confirm: building=yes at (1689, 1696); building=roof at (1712, 1724); building=yes at (1732, 1738); building=yes at (1727, 1714)

**Hillsides and steep ground (D1, D2, D3)**
- Bank/slope left of the line around Unity (1334, 1902): 513 m2 over 15 deg. One eye-level photo across it, one along the toe where scrub meets turf (D1, D2, D3).

**Bunkers (D4, D5, D6)**
- bunker_19(csv 25,greenside,155 m2) at (1646, 1766): heightmap depth 0.19 m vs plan 1.18 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).

**Green (D7, D8, D9, D10)**
- LAS scan of the green plus 3 m of collar (lanes 1.5 m apart). Slope report: mean 3.15%, p90 3.73%, 3/4 pins fail - steep >3%. Photo of the collar from the fringe and low along the edge toward each bunker (D7, D8, D9).

**Trees within 35 m (D18)**
- 19 LiDAR trees within 35 m of a tee or the green (8 over 16 m; draft pine 4, eucalyptus 3, broadleaf 12): one photo each from the tee side with scale, close enough for species; note dead/missing. 1 shrubs at/over 3 m near the tees/green: tree or shrub? (D18)

## Hole 10

**Tee boxes (D17, signs, markers)**
- Every box: down the line from the back with markers, across the deck edge/bank, note which colour is on which deck. All four colours on mapped boxes with a LiDAR deck.

**Tee surrounds and props (D14)**
- Hole sign square-on from 3 m, tee markers, bins, benches, ball washers, ropes at every box (D14). OSM candidates to confirm: building=yes at (1732, 1738); building=yes at (1727, 1714); building=roof at (1712, 1724); amenity=parking at (1740, 1667)

**Hillsides and steep ground (D1, D2, D3)**
- Bank/slope left of the line around Unity (1943, 1851): 656 m2 over 15 deg. One eye-level photo across it, one along the toe where scrub meets turf (D1, D2, D3).

**Bunkers (D4, D5, D6)**
- bunker_21(csv 23,fairway,32 m2) at (1769, 1731): satellite shows sand on only 2% of the OSM outline. Photo from the fairway side and across the floor: does it exist, is it sand or grassed over (D4).
- bunker_21(csv 23,fairway,32 m2) at (1769, 1731): heightmap depth -0.00 m vs plan 0.40 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).
- bunker_22(csv 22,fairway,110 m2) at (1831, 1695): satellite shows sand on only 19% of the OSM outline. Photo from the fairway side and across the floor: does it exist, is it sand or grassed over (D4).
- bunker_22(csv 22,fairway,110 m2) at (1831, 1695): heightmap depth 0.19 m vs plan 0.44 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).

**Green (D7, D8, D9, D10)**
- LAS scan of the green plus 3 m of collar (lanes 1.5 m apart). Slope report: mean 2.19%, p90 3.6%, 0/4 pins fail. Photo of the collar from the fringe and low along the edge toward each bunker (D7, D8, D9).
- Bank behind/beside the green (rise 3.18 m, surround slope up to 26.4%): photo of the bank with scale (D10).

**Trees within 35 m (D18)**
- 13 LiDAR trees within 35 m of a tee or the green (5 over 16 m; draft pine 5, broadleaf 8): one photo each from the tee side with scale, close enough for species; note dead/missing. 1 shrubs at/over 3 m near the tees/green: tree or shrub? (D18)

## Hole 11

**Tee boxes (D17, signs, markers)**
- Every box: down the line from the back with markers, across the deck edge/bank, note which colour is on which deck. Confirm: Black on 6% ground, no LiDAR flat: the real tee is elsewhere

**Tee surrounds and props (D14)**
- Hole sign square-on from 3 m, tee markers, bins, benches, ball washers, ropes at every box (D14). OSM candidates to confirm: building=yes at (2098, 1940); amenity=drinking_water at (2144, 1905); building=industrial at (2147, 1921); amenity=parking at (1831, 1638)

**Hillsides and steep ground (D1, D2, D3)**
- Bank/slope left of the line around Unity (2094, 1878): 6259 m2 over 15 deg. One eye-level photo across it, one along the toe where scrub meets turf (D1, D2, D3).
- Steep cells over 35 deg near Unity (2133, 1884), 350 m2: photo framing the face to settle rock vs scrub and its colour (D3).

**Bunkers (D4, D5, D6)**
- bunker_23(csv 21,fairway,98 m2) at (1950, 1669): satellite shows sand on only 7% of the OSM outline. Photo from the fairway side and across the floor: does it exist, is it sand or grassed over (D4).
- bunker_23(csv 21,fairway,98 m2) at (1950, 1669): heightmap depth 0.10 m vs plan 0.42 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).
- bunker_24(csv 20,fairway,82 m2) at (1983, 1663): satellite shows sand on only 31% of the OSM outline. Photo from the fairway side and across the floor: does it exist, is it sand or grassed over (D4).
- bunker_24(csv 20,fairway,82 m2) at (1983, 1663): heightmap depth -0.07 m vs plan 0.40 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).
- bunker_25(csv 19,greenside,150 m2) at (1915, 1658): satellite shows sand on only 36% of the OSM outline. Photo from the fairway side and across the floor: does it exist, is it sand or grassed over (D4).
- bunker_25(csv 19,greenside,150 m2) at (1915, 1658): heightmap depth 0.30 m vs plan 1.17 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).
- bunker_27(csv 18,greenside,88 m2) at (1943, 1633): heightmap depth -0.04 m vs plan 0.96 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).
- bunker_30(csv 17,greenside,202 m2) at (1903, 1609): heightmap depth 0.45 m vs plan 1.34 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).

**Green (D7, D8, D9, D10)**
- LAS scan of the green plus 3 m of collar (lanes 1.5 m apart). Slope report: mean 2.95%, p90 3.72%, 1/4 pins fail. Photo of the collar from the fringe and low along the edge toward each bunker (D7, D8, D9).

**Trees within 35 m (D18)**
- 18 LiDAR trees within 35 m of a tee or the green (5 over 16 m; draft pine 8, broadleaf 10): one photo each from the tee side with scale, close enough for species; note dead/missing. 3 shrubs at/over 3 m near the tees/green: tree or shrub? (D18)

## Hole 12

**Tee boxes (D17, signs, markers)**
- Every box: down the line from the back with markers, across the deck edge/bank, note which colour is on which deck. Confirm: Black card-placed: which deck?; Blue card-placed: which deck?; Yellow card-placed: which deck?

**Tee surrounds and props (D14)**
- Hole sign square-on from 3 m, tee markers, bins, benches, ball washers, ropes at every box (D14).

**Hillsides and steep ground (D1, D2, D3)**
- Bank/slope right of the line around Unity (2486, 1566): 912 m2 over 15 deg. One eye-level photo across it, one along the toe where scrub meets turf (D1, D2, D3).

**Bunkers (D4, D5, D6)**
- bunker_28(csv 42,greenside,259 m2) at (2657, 1621): satellite sand runs 94 m2 outside the OSM outline / best shift 3.6 m. Photo from the fairway side showing the sand line (D4).
- bunker_28(csv 42,greenside,259 m2) at (2657, 1621): heightmap depth 0.24 m vs plan 1.50 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).
- bunker_31(csv 40,greenside,75 m2) at (2645, 1589): heightmap depth 0.20 m vs plan 0.92 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).
- bunker_32(csv 38,fairway,206 m2) at (2463, 1577): satellite shows sand on only 0% of the OSM outline. Photo from the fairway side and across the floor: does it exist, is it sand or grassed over (D4).
- bunker_32(csv 38,fairway,206 m2) at (2463, 1577): heightmap depth 0.03 m vs plan 0.57 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).
- bunker_33(csv 39,greenside,172 m2) at (2679, 1578): heightmap depth 0.38 m vs plan 1.24 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).

**Green (D7, D8, D9, D10)**
- LAS scan of the green plus 3 m of collar (lanes 1.5 m apart). Slope report: mean 1.89%, p90 2.52%, 0/4 pins fail. Photo of the collar from the fringe and low along the edge toward each bunker (D7, D8, D9).

**Trees within 35 m (D18)**
- 12 LiDAR trees within 35 m of a tee or the green (4 over 16 m; draft pine 3, palm 1, eucalyptus 1, broadleaf 7): one photo each from the tee side with scale, close enough for species; note dead/missing. 0 shrubs at/over 3 m near the tees/green: tree or shrub? (D18)

## Hole 13

**Tee boxes (D17, signs, markers)**
- Every box: down the line from the back with markers, across the deck edge/bank, note which colour is on which deck. Confirm: White on 5% ground, no LiDAR flat: the real tee is elsewhere; Yellow card-placed: which deck?

**Tee surrounds and props (D14)**
- Hole sign square-on from 3 m, tee markers, bins, benches, ball washers, ropes at every box (D14). OSM candidates to confirm: building=yes at (2791, 1536); amenity=drinking_water at (3207, 1608)

**Bunkers (D4, D5, D6)**
- bunker_26(csv 43,greenside,206 m2) at (3124, 1656): heightmap depth 0.62 m vs plan 1.35 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).
- bunker_29(csv 41,greenside,184 m2) at (3131, 1616): heightmap depth 0.28 m vs plan 1.28 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).

**Green (D7, D8, D9, D10)**
- LAS scan of the green plus 3 m of collar (lanes 1.5 m apart). Slope report: mean 1.84%, p90 2.45%, 0/4 pins fail. Photo of the collar from the fringe and low along the edge toward each bunker (D7, D8, D9).

**Trees within 35 m (D18)**
- 13 LiDAR trees within 35 m of a tee or the green (0 over 16 m; draft broadleaf 13): one photo each from the tee side with scale, close enough for species; note dead/missing. 4 shrubs at/over 3 m near the tees/green: tree or shrub? (D18)

## Hole 14

**Tee boxes (D17, signs, markers)**
- Every box: down the line from the back with markers, across the deck edge/bank, note which colour is on which deck. All four colours on mapped boxes with a LiDAR deck.

**Tee surrounds and props (D14)**
- Hole sign square-on from 3 m, tee markers, bins, benches, ball washers, ropes at every box (D14). OSM candidates to confirm: building=yes at (2791, 1536); amenity=drinking_water at (3207, 1608); building=house at (3260, 1551); building=house at (3266, 1555)

**Bunkers (D4, D5, D6)**
- bunker_35(csv 36,greenside,48 m2) at (2799, 1520): heightmap depth 0.32 m vs plan 0.83 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).
- bunker_36(csv 35,greenside,45 m2) at (2807, 1518): satellite sand runs 33 m2 outside the OSM outline / best shift 1.6 m. Photo from the fairway side showing the sand line (D4).
- bunker_36(csv 35,greenside,45 m2) at (2807, 1518): heightmap depth 0.42 m vs plan 0.82 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).
- bunker_39(csv 33,greenside,41 m2) at (2807, 1502): heightmap depth 0.43 m vs plan 0.80 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).

**Green (D7, D8, D9, D10)**
- LAS scan of the green plus 3 m of collar (lanes 1.5 m apart). Slope report: mean 2.32%, p90 3.11%, 0/4 pins fail. Photo of the collar from the fringe and low along the edge toward each bunker (D7, D8, D9).

**Trees within 35 m (D18)**
- 20 LiDAR trees within 35 m of a tee or the green (8 over 16 m; draft pine 7, palm 1, broadleaf 12): one photo each from the tee side with scale, close enough for species; note dead/missing. 0 shrubs at/over 3 m near the tees/green: tree or shrub? (D18)

## Hole 15

**Tee boxes (D17, signs, markers)**
- Every box: down the line from the back with markers, across the deck edge/bank, note which colour is on which deck. Confirm: Black card-placed: which deck?; Yellow card-placed: which deck?

**Tee surrounds and props (D14)**
- Hole sign square-on from 3 m, tee markers, bins, benches, ball washers, ropes at every box (D14). OSM candidates to confirm: building=yes at (2791, 1536)

**Bunkers (D4, D5, D6)**
- bunker_43(csv 30,greenside,229 m2) at (2812, 1373): satellite sand runs 22 m2 outside the OSM outline / best shift 1.6 m. Photo from the fairway side showing the sand line (D4).
- bunker_43(csv 30,greenside,229 m2) at (2812, 1373): heightmap depth 0.36 m vs plan 1.43 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).

**Green (D7, D8, D9, D10)**
- LAS scan of the green plus 3 m of collar (lanes 1.5 m apart). Slope report: mean 1.78%, p90 3.36%, 0/4 pins fail. Photo of the collar from the fringe and low along the edge toward each bunker (D7, D8, D9).

**Trees within 35 m (D18)**
- 18 LiDAR trees within 35 m of a tee or the green (7 over 16 m; draft palm 4, broadleaf 12, pine 2): one photo each from the tee side with scale, close enough for species; note dead/missing. 1 shrubs at/over 3 m near the tees/green: tree or shrub? (D18)

## Hole 16

**Tee boxes (D17, signs, markers)**
- Every box: down the line from the back with markers, across the deck edge/bank, note which colour is on which deck. Confirm: Black card-placed: which deck?; White card-placed: which deck?; Yellow on 8% ground, no LiDAR flat: the real tee is elsewhere

**Tee surrounds and props (D14)**
- Hole sign square-on from 3 m, tee markers, bins, benches, ball washers, ropes at every box (D14).

**Hillsides and steep ground (D1, D2, D3)**
- Bank/slope left of the line around Unity (2719, 1376): 3861 m2 over 15 deg. One eye-level photo across it, one along the toe where scrub meets turf (D1, D2, D3).
- Steep cells over 35 deg near Unity (2760, 1285), 1943 m2: photo framing the face to settle rock vs scrub and its colour (D3).

**Bunkers (D4, D5, D6)**
- bunker_34(csv 37,greenside,146 m2) at (2586, 1553): heightmap depth 0.46 m vs plan 1.15 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).
- bunker_37(csv 34,greenside,104 m2) at (2569, 1517): satellite shows sand on only 33% of the OSM outline. Photo from the fairway side and across the floor: does it exist, is it sand or grassed over (D4).
- bunker_37(csv 34,greenside,104 m2) at (2569, 1517): heightmap depth 0.35 m vs plan 1.01 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).

**Green (D7, D8, D9, D10)**
- LAS scan of the green plus 3 m of collar (lanes 1.5 m apart). Slope report: mean 1.89%, p90 2.75%, 0/4 pins fail. Photo of the collar from the fringe and low along the edge toward each bunker (D7, D8, D9).

**Water (D11)**
- Pond: photo along each bank from a path corner and across the pond; LiDAR level elev 287.6 m. The 2023-24 LiDAR reads ground on 28% of the OSM outline (peninsula and margins): confirm the water reaches the mapped edge (D11).

**Trees within 35 m (D18)**
- 13 LiDAR trees within 35 m of a tee or the green (6 over 16 m; draft palm 1, pine 2, broadleaf 10): one photo each from the tee side with scale, close enough for species; note dead/missing. 0 shrubs at/over 3 m near the tees/green: tree or shrub? (D18)

## Hole 17

**Tee boxes (D17, signs, markers)**
- Every box: down the line from the back with markers, across the deck edge/bank, note which colour is on which deck. Confirm: Yellow on 5% ground, no LiDAR flat: the real tee is elsewhere

**Tee surrounds and props (D14)**
- Hole sign square-on from 3 m, tee markers, bins, benches, ball washers, ropes at every box (D14).

**Bunkers (D4, D5, D6)**
- bunker_41(csv 32,greenside,281 m2) at (2499, 1405): satellite sand runs 34 m2 outside the OSM outline / best shift 2.1 m. Photo from the fairway side showing the sand line (D4).
- bunker_41(csv 32,greenside,281 m2) at (2499, 1405): heightmap depth 0.17 m vs plan 1.50 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).
- bunker_42(csv 31,greenside,109 m2) at (2448, 1377): satellite shows sand on only 0% of the OSM outline. Photo from the fairway side and across the floor: does it exist, is it sand or grassed over (D4).
- bunker_42(csv 31,greenside,109 m2) at (2448, 1377): heightmap depth 0.07 m vs plan 1.03 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).

**Green (D7, D8, D9, D10)**
- LAS scan of the green plus 3 m of collar (lanes 1.5 m apart). Slope report: mean 1.03%, p90 1.57%, 0/4 pins fail. Photo of the collar from the fringe and low along the edge toward each bunker (D7, D8, D9).

**Trees within 35 m (D18)**
- 9 LiDAR trees within 35 m of a tee or the green (3 over 16 m; draft pine 2, palm 1, broadleaf 6): one photo each from the tee side with scale, close enough for species; note dead/missing. 0 shrubs at/over 3 m near the tees/green: tree or shrub? (D18)

## Hole 18

**Tee boxes (D17, signs, markers)**
- Every box: down the line from the back with markers, across the deck edge/bank, note which colour is on which deck. Confirm: Yellow on 6% ground, no LiDAR flat: the real tee is elsewhere

**Tee surrounds and props (D14)**
- Hole sign square-on from 3 m, tee markers, bins, benches, ball washers, ropes at every box (D14).

**Hillsides and steep ground (D1, D2, D3)**
- Bank/slope left of the line around Unity (2356, 1334): 5694 m2 over 15 deg. One eye-level photo across it, one along the toe where scrub meets turf (D1, D2, D3).
- Steep cells over 35 deg near Unity (2379, 1301), 2921 m2: photo framing the face to settle rock vs scrub and its colour (D3).

**Bunkers (D4, D5, D6)**
- bunker_38(csv 16,greenside,212 m2) at (2168, 1508): heightmap depth 0.39 m vs plan 1.37 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).
- bunker_40(csv 15,fairway,167 m2) at (2285, 1440): satellite shows sand on only 23% of the OSM outline. Photo from the fairway side and across the floor: does it exist, is it sand or grassed over (D4).
- bunker_40(csv 15,fairway,167 m2) at (2285, 1440): heightmap depth 0.19 m vs plan 0.52 m. Photo from the fairway side with the face against the lip, one from the green side, one across the floor for grass (D5, D6).

**Green (D7, D8, D9, D10)**
- LAS scan of the green plus 3 m of collar (lanes 1.5 m apart). Slope report: mean 5.07%, p90 6.96%, 4/4 pins fail - steep >3%. Photo of the collar from the fringe and low along the edge toward each bunker (D7, D8, D9).

**Trees within 35 m (D18)**
- 21 LiDAR trees within 35 m of a tee or the green (11 over 16 m; draft pine 6, palm 3, broadleaf 10, eucalyptus 2): one photo each from the tee side with scale, close enough for species; note dead/missing. 4 shrubs at/over 3 m near the tees/green: tree or shrub? (D18)

