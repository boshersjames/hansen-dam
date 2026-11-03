# Flyover gate (data pass)

Inputs: GKD `HansenDam.GKD`, signs `progress/hole_signs.json`, trees `trees.csv`, greens `course.svg`, heightmap `heightmap_2049.raw`, pin index 0.

Pass = yaw and pitch under 5 deg in every 1 s window, opening camera clear of crowns with the sign in frame and unhidden, terrain clearance 5 m+, crown clearance 1.5 m+ on the whole path, no part of the green cut off ahead or to the side in the end frame (the part under the camera is reported, not failed), pin in frame and not behind a crown.

| Hole | s | yaw/1s | pitch/1s | end pitch (target) | end h / short (used) | terrain min (after rise) | crown min (tree, frame), lift rise/flight | first: crown / sight / in frame | green: in / under cam / cut off (pull-back to fit) | pin | result | opening move |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 19.5 | 0.6 | 4.5 | -27.4 (-27.4) | 16.2 / 29.5 | 16.1 | 2.7 (850, f58), 0.0 / 0.0 | 5.1 / 4.9 / yes | 100% / 0 / 0 (0 m) | in, sight 12.4 | **OK** |  |
| 2 | 24.0 | 0.0 | 4.5 | -28.9 (-28.9) | 13.4 / 22.5 | 13.3 | -0.9 (542, f66), 0.0 / 0.0 | 5.0 / 4.7 / yes | 99% / 1 / 0 (0 m) | in, sight 12.4 | **FAIL** | opening NOT fixed within 6 m (crown 5.0 m, sign sightline 4.7 m, sign in frame True, rise -0.9 m from crown of tree 542) |
| 3 | 20.3 | 1.1 | 4.5 | -28.8 (-28.8) | 16.7 / 28.5 | 16.1 | 0.6 (872, f56), 0.0 / 0.0 | 2.7 / 1.8 / yes | 100% / 0 / 0 (0 m) | in, sight 6.6 | **FAIL** | opening NOT fixed within 6 m (crown 2.7 m, sign sightline 1.8 m, sign in frame True, rise 0.6 m from crown of tree 872) |
| 4 | 12.7 | 4.5 | 3.4 | -18.6 (-18.6) | 16.3 / 40.5 | 16.3 | 2.6 (1585, f44), 0.0 / 0.0 | 2.9 / 2.8 / yes | 100% / 0 / 0 (0 m) | in, sight 4.7 | **OK** |  |
| 5 | 21.4 | 1.8 | 4.5 | -29.3 (-29.3) | 13.3 / 22.5 | 13.2 | 9.6 (1758, f56), 0.0 / 0.0 | 9.6 / 9.7 / yes | 100% / 0 / 0 (0 m) | in, sight 10.0 | **OK** |  |
| 6 | 26.3 | 0.8 | 4.5 | -29.2 (-29.2) | 12.9 / 22.0 | 12.8 | 1.8 (1093, f56), 0.0 / 0.0 | 3.8 / 3.7 / yes | 100% / 0 / 0 (0 m) | in, sight 16.5 | **OK** |  |
| 7 | 12.7 | 4.5 | 4.5 | -13.5 (-13.5) | 16.7 / 78.5 | 16.7 | 11.1 (1789, f252), 0.0 / 0.0 | 17.7 / 17.8 / yes | 72% / 0 / 22 (8 m) | in, sight 10.4 | **FAIL** |  |
| 8 | 19.8 | 0.4 | 4.5 | -29.8 (-29.8) | 14.5 / 24.5 | 14.4 | 1.7 (735, f64), 0.0 / 0.0 | 6.0 / 4.6 / yes | 100% / 0 / 0 (0 m) | in, sight 12.3 | **OK** |  |
| 9 | 22.1 | 0.2 | 4.5 | -28.4 (-28.4) | 12.8 / 21.5 | 12.8 | -2.8 (34, f90), 0.0 / 0.3 | 7.1 / 7.3 / yes | 100% / 0 / 0 (0 m) | in, sight 11.6 | **FAIL** | opening NOT fixed within 6 m (crown 7.1 m, sign sightline 7.3 m, sign in frame True, rise -2.8 m from crown of tree 34) |
| 10 | 17.0 | 1.9 | 4.5 | -27.6 (-27.6) | 15.5 / 23.5 | 15.2 | 4.3 (1555, f40), 0.0 / 0.0 | 4.4 / 4.6 / yes | 100% / 0 / 0 (0 m) | in, sight 14.2 | **OK** |  |
| 11 | 18.3 | 0.5 | 4.5 | -31.2 (-31.2) | 12.2 / 20.0 | 12.0 | 3.6 (870, f64), 0.0 / 0.0 | 7.8 / 4.7 / yes | 100% / 0 / 0 (0 m) | in, sight 10.4 | **OK** |  |
| 12 | 25.2 | 0.3 | 4.5 | -28.5 (-28.5) | 16.2 / 28.5 | 16.2 | 6.8 (1666, f0), 0.0 / 0.0 | 6.8 / 7.0 / yes | 96% / 3 / 0 (0 m) | in, sight 10.5 | **OK** |  |
| 13 | 21.4 | 1.0 | 4.5 | -29.4 (-29.4) | 14.1 / 24.0 | 14.1 | 4.3 (1801, f46), 0.0 / 0.0 | 4.8 / 4.7 / yes | 96% / 3 / 0 (0 m) | in, sight 13.8 | **OK** |  |
| 14 | 24.1 | 1.1 | 4.5 | -26.9 (-26.9) | 16.2 / 30.5 | 16.2 | 4.0 (1932, f0), 0.0 / 0.0 | 4.0 / 4.2 / yes | 100% / 0 / 0 (0 m) | in, sight 8.3 | **OK** |  |
| 15 | 12.7 | 4.5 | 4.4 | -12.4 (-12.4) | 16.0 / 75.5 | 16.0 | 1.6 (967, f60), 0.0 / 0.0 | 3.3 / 2.8 / yes | 84% / 0 / 12 (8 m) | in, sight 12.2 | **FAIL** | opening moved 2.8 m (back 4.5 -> 6.5, side 1.6 -> 3.6): rise through crown of tree 967 (0.5 m) |
| 16 | 18.8 | 4.5 | 4.5 | -29.3 (-29.3) | 13.6 / 23.0 | 13.5 | 3.4 (1311, f46), 0.0 / 0.0 | 3.7 / 3.7 / yes | 100% / 0 / 0 (0 m) | in, sight 10.6 | **OK** |  |
| 17 | 12.7 | 4.5 | 4.0 | -10.4 (-10.4) | 16.1 / 88.5 | 16.1 | 4.9 (1636, f46), 0.0 / 0.0 | 5.2 / 4.6 / yes | 79% / 0 / 18 (10 m) | in, sight 5.7 | **FAIL** |  |
| 18 | 21.5 | 2.0 | 4.5 | -28.9 (-28.9) | 14.7 / 25.0 | 14.7 | 2.4 (729, f58), 0.0 / 0.0 | 5.0 / 4.3 / yes | 100% / 0 / 0 (0 m) | in, sight 14.2 | **OK** |  |

End spot: 12 m short of the pin, 8 m over the ground (v4 default 12 / 8), pulled back per hole until the green fits (--end-fit).

Failed holes: 2, 3, 7, 9, 15, 17

Poster frames (first / rise / mid / approach / end) per hole are in flyover_gate.json; shots for the PC render in flyover_shots.json (8758 frames).
