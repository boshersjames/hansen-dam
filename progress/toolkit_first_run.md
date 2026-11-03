# First headless toolkit run (2026-11-03)

Run from the course folder, course-build at 02dcbcb Skills: additive Tools section in all 23 (exact toolkit commands, rule keys, and 'no tool yet' gaps); no existing text changed.

## doctor.py

```
ok   course.json                            /home/user/hansen-dam/course.json
ok   paths.toolkit                          /home/user/course-build
ok   heightmap size                         8396802 bytes (= 2049^2 x 2)
ok   gkd parses                             Hansen Dam Golf Course: 18 holes, 18 enabled
ok   svg greens match gkd                   23 outlines, 18 of 18 enabled holes matched
ok   paths.satellite                        /home/user/hansen-dam/satellite.jpg
ok   paths.trees_csv                        /home/user/hansen-dam/trees.csv
WARN paths.signs                            missing (/home/user/hansen-dam/progress/hole_signs.json)
WARN paths.photos_root                      missing (/home/user/hansen-dam/course_photos)
ok   python numpy                           
ok   python scipy                           
ok   python matplotlib                      
ok   python PIL                             
ok   python pyproj                          
ok   python laspy                           
ok   python pillow_heif                     
ok   tool git                               
ok   tool git-lfs                           
ok   tool ffmpeg                            
ok   tool yt-dlp                            
info unity_project                          C:/GSP/HansenDam_Project not on this machine
info automation latest run                  none here

0 FAIL, 2 WARN
[exit 0]
```

## gkd_tools.py check

```
25 checks, 0 failing
[exit 0]
```

## green_report.py --smooth 0.6

```
# Green report (hansen_dam, surface: course heightmap order 3, low-pass sigma 0.6 m)

Rules: pin area <= 1.7 deg over 17 points, pins >= 3 m from the edge, >= 4 valid areas >= 3 m apart; internal slope 1-3%.

| hole | area m2 | relief m | slope mean/p90 % | >3% | pins fail | pin angles | usable % | areas | flag | pass |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 666 | 0.66 | 2.3 / 3.5 | 18 | 1/4 | Thu:1.4 Fri:1.9 Sat:1.5 Sun:1.5 | 64 | 48 |  | FAIL |
| 2 | 528 | 0.97 | 3.3 / 5.0 | 54 | 3/4 | Thu:2.0 Fri:1.9 Sat:1.9 Sun:1.3 | 43 | 26 | steep >3% | FAIL |
| 3 | 719 | 0.74 | 3.1 / 4.2 | 51 | 1/4 | Thu:1.7 Fri:1.6 Sat:1.9 Sun:1.4 | 61 | 48 | steep >3% | FAIL |
| 4 | 661 | 1.77 | 4.4 / 6.8 | 85 | 4/4 | Thu:4.7 Fri:3.4 Sat:4.0 Sun:3.6 | 12 | 12 | steep >3% | FAIL |
| 5 | 512 | 0.66 | 2.8 / 4.1 | 40 | 1/4 | Thu:1.2 Fri:1.3 Sat:2.1 Sun:0.8 | 51 | 31 |  | FAIL |
| 6 | 498 | 0.91 | 3.3 / 4.3 | 65 | 3/4 | Thu:1.6 Fri:1.8 Sat:2.5 Sun:2.3 | 28 | 19 | steep >3% | FAIL |
| 7 | 559 | 0.63 | 2.4 / 3.4 | 17 | 0/4 | Thu:1.5 Fri:1.6 Sat:1.5 Sun:0.9 | 77 | 45 |  | PASS |
| 8 | 501 | 0.47 | 1.8 / 3.3 | 14 | 0/4 | Thu:0.9 Fri:0.7 Sat:1.2 Sun:0.6 | 73 | 38 |  | PASS |
| 9 | 532 | 0.78 | 3.1 / 3.7 | 64 | 3/4 | Thu:1.7 Fri:2.2 Sat:1.8 Sun:1.8 | 29 | 25 | steep >3% | FAIL |
| 10 | 446 | 0.59 | 2.2 / 3.6 | 18 | 0/4 | Thu:1.4 Fri:1.4 Sat:1.4 Sun:0.6 | 80 | 35 |  | PASS |
| 11 | 471 | 0.74 | 3.0 / 3.7 | 52 | 1/4 | Thu:1.7 Fri:1.6 Sat:1.4 Sun:1.9 | 46 | 25 |  | FAIL |
| 12 | 625 | 0.66 | 1.9 / 2.5 | 2 | 0/4 | Thu:1.2 Fri:1.5 Sat:1.1 Sun:1.1 | 92 | 59 |  | PASS |
| 13 | 612 | 0.46 | 1.8 / 2.5 | 6 | 0/4 | Thu:1.4 Fri:1.2 Sat:1.2 Sun:1.2 | 92 | 54 |  | PASS |
| 14 | 718 | 0.66 | 2.3 / 3.1 | 13 | 0/4 | Thu:1.3 Fri:1.7 Sat:1.2 Sun:0.9 | 75 | 59 |  | PASS |
| 15 | 560 | 0.49 | 1.8 / 3.4 | 16 | 0/4 | Thu:0.4 Fri:0.7 Sat:0.6 Sun:1.5 | 71 | 37 |  | PASS |
| 16 | 489 | 0.45 | 1.9 / 2.8 | 8 | 0/4 | Thu:1.6 Fri:1.0 Sat:1.0 Sun:0.9 | 86 | 41 |  | PASS |
| 17 | 778 | 0.28 | 1.0 / 1.6 | 2 | 0/4 | Thu:0.6 Fri:1.0 Sat:0.6 Sun:0.7 | 98 | 76 |  | PASS |
| 18 | 638 | 1.32 | 5.1 / 7.0 | 84 | 4/4 | Thu:3.0 Fri:2.4 Sat:3.1 Sun:2.0 | 13 | 10 | steep >3% | FAIL |
wrote progress/green_report
[exit 0]
```

## flyover_gate.py --end-fit --no-plots

```
no signs file at /home/user/hansen-dam/progress/hole_signs.json: provisional sign spots from the back tees
hole  1: 487 frames  19.5 s (x1.00) yaw/1s 0.59 pitch/1s 4.50 | end pitch -27.4 (pin -27.4) h 16.2 m, 29.5 m short | terrain 16.1 m crown 2.7 m (tree 850, lift 0.0/0.0) | first: crown 5.1 sight 4.9 in-frame True | green 100% (cut off 0, pull-back 0.0) pin True sight 12.4 -> OK
hole  2: 599 frames  24.0 s (x1.00) yaw/1s 0.01 pitch/1s 4.50 | end pitch -28.9 (pin -28.9) h 13.4 m, 22.5 m short | terrain 13.3 m crown -0.9 m (tree 542, lift 0.0/0.0) | first: crown 5.0 sight 4.7 in-frame True | green 99% (cut off 0, pull-back 0.0) pin True sight 12.4 -> FAIL  [opening NOT fixed within 6 m (crown 5.0 m, sign sightline 4.7 m, sign in frame True, rise -0.9 m from crown of tree 542)]
hole  3: 507 frames  20.3 s (x1.00) yaw/1s 1.07 pitch/1s 4.50 | end pitch -28.8 (pin -28.8) h 16.7 m, 28.5 m short | terrain 16.1 m crown 0.6 m (tree 872, lift 0.0/0.0) | first: crown 2.7 sight 1.8 in-frame True | green 100% (cut off 0, pull-back 0.0) pin True sight 6.6 -> FAIL  [opening NOT fixed within 6 m (crown 2.7 m, sign sightline 1.8 m, sign in frame True, rise 0.6 m from crown of tree 872)]
hole  4: 317 frames  12.7 s (x1.00) yaw/1s 4.50 pitch/1s 3.36 | end pitch -18.6 (pin -18.6) h 16.3 m, 40.5 m short | terrain 16.3 m crown 2.6 m (tree 1585, lift 0.0/0.0) | first: crown 2.9 sight 2.8 in-frame True | green 100% (cut off 0, pull-back 0.0) pin True sight 4.7 -> OK
hole  5: 535 frames  21.4 s (x1.00) yaw/1s 1.79 pitch/1s 4.50 | end pitch -29.3 (pin -29.3) h 13.3 m, 22.5 m short | terrain 13.2 m crown 9.6 m (tree 1758, lift 0.0/0.0) | first: crown 9.6 sight 9.7 in-frame True | green 100% (cut off 0, pull-back 0.0) pin True sight 10.0 -> OK
hole  6: 658 frames  26.3 s (x1.00) yaw/1s 0.81 pitch/1s 4.50 | end pitch -29.2 (pin -29.2) h 12.9 m, 22.0 m short | terrain 12.8 m crown 1.8 m (tree 1093, lift 0.0/0.0) | first: crown 3.8 sight 3.7 in-frame True | green 100% (cut off 0, pull-back 0.0) pin True sight 16.5 -> OK
hole  7: 317 frames  12.7 s (x1.00) yaw/1s 4.50 pitch/1s 4.50 | end pitch -13.5 (pin -13.5) h 16.7 m, 78.5 m short | terrain 16.7 m crown 11.1 m (tree 1789, lift 0.0/0.0) | first: crown 17.7 sight 17.8 in-frame True | green 72% (cut off 22, pull-back 8.5) pin True sight 10.4 -> FAIL
hole  8: 495 frames  19.8 s (x1.00) yaw/1s 0.44 pitch/1s 4.50 | end pitch -29.8 (pin -29.8) h 14.5 m, 24.5 m short | terrain 14.4 m crown 1.7 m (tree 735, lift 0.0/0.0) | first: crown 6.0 sight 4.6 in-frame True | green 100% (cut off 0, pull-back 0.0) pin True sight 12.3 -> OK
hole  9: 552 frames  22.1 s (x1.00) yaw/1s 0.24 pitch/1s 4.50 | end pitch -28.4 (pin -28.4) h 12.8 m, 21.5 m short | terrain 12.8 m crown -2.8 m (tree 34, lift 0.0/0.3) | first: crown 7.1 sight 7.3 in-frame True | green 100% (cut off 0, pull-back 0.0) pin True sight 11.6 -> FAIL  [opening NOT fixed within 6 m (crown 7.1 m, sign sightline 7.3 m, sign in frame True, rise -2.8 m from crown of tree 34)]
hole 10: 426 frames  17.0 s (x1.00) yaw/1s 1.92 pitch/1s 4.50 | end pitch -27.6 (pin -27.6) h 15.5 m, 23.5 m short | terrain 15.2 m crown 4.3 m (tree 1555, lift 0.0/0.0) | first: crown 4.4 sight 4.6 in-frame True | green 100% (cut off 0, pull-back 0.0) pin True sight 14.2 -> OK
hole 11: 457 frames  18.3 s (x1.00) yaw/1s 0.47 pitch/1s 4.50 | end pitch -31.2 (pin -31.2) h 12.2 m, 20.0 m short | terrain 12.0 m crown 3.6 m (tree 870, lift 0.0/0.0) | first: crown 7.8 sight 4.7 in-frame True | green 100% (cut off 0, pull-back 0.0) pin True sight 10.4 -> OK
hole 12: 631 frames  25.2 s (x1.00) yaw/1s 0.34 pitch/1s 4.50 | end pitch -28.5 (pin -28.5) h 16.2 m, 28.5 m short | terrain 16.2 m crown 6.8 m (tree 1666, lift 0.0/0.0) | first: crown 6.8 sight 7.0 in-frame True | green 96% (cut off 0, pull-back 0.0) pin True sight 10.5 -> OK
hole 13: 535 frames  21.4 s (x1.00) yaw/1s 1.03 pitch/1s 4.50 | end pitch -29.4 (pin -29.4) h 14.1 m, 24.0 m short | terrain 14.1 m crown 4.3 m (tree 1801, lift 0.0/0.0) | first: crown 4.8 sight 4.7 in-frame True | green 96% (cut off 0, pull-back 0.0) pin True sight 13.8 -> OK
hole 14: 602 frames  24.1 s (x1.00) yaw/1s 1.15 pitch/1s 4.50 | end pitch -26.9 (pin -26.9) h 16.2 m, 30.5 m short | terrain 16.2 m crown 4.0 m (tree 1932, lift 0.0/0.0) | first: crown 4.0 sight 4.2 in-frame True | green 100% (cut off 0, pull-back 0.0) pin True sight 8.3 -> OK
hole 15: 317 frames  12.7 s (x1.00) yaw/1s 4.50 pitch/1s 4.43 | end pitch -12.4 (pin -12.4) h 16.0 m, 75.5 m short | terrain 16.0 m crown 1.6 m (tree 967, lift 0.0/0.0) | first: crown 3.3 sight 2.8 in-frame True | green 84% (cut off 12, pull-back 8.0) pin True sight 12.2 -> FAIL  [opening moved 2.8 m (back 4.5 -> 6.5, side 1.6 -> 3.6): rise through crown of tree 967 (0.5 m)]
hole 16: 469 frames  18.8 s (x1.00) yaw/1s 4.50 pitch/1s 4.50 | end pitch -29.3 (pin -29.3) h 13.6 m, 23.0 m short | terrain 13.5 m crown 3.4 m (tree 1311, lift 0.0/0.0) | first: crown 3.7 sight 3.7 in-frame True | green 100% (cut off 0, pull-back 0.0) pin True sight 10.6 -> OK
hole 17: 317 frames  12.7 s (x1.00) yaw/1s 4.50 pitch/1s 4.03 | end pitch -10.4 (pin -10.4) h 16.1 m, 88.5 m short | terrain 16.1 m crown 4.9 m (tree 1636, lift 0.0/0.0) | first: crown 5.2 sight 4.6 in-frame True | green 79% (cut off 18, pull-back 10.0) pin True sight 5.7 -> FAIL
hole 18: 537 frames  21.5 s (x1.00) yaw/1s 1.97 pitch/1s 4.50 | end pitch -28.9 (pin -28.9) h 14.7 m, 25.0 m short | terrain 14.7 m crown 2.4 m (tree 729, lift 0.0/0.0) | first: crown 5.0 sight 4.3 in-frame True | green 100% (cut off 0, pull-back 0.0) pin True sight 14.2 -> OK
Failed holes: 2, 3, 7, 9, 15, 17

Poster frames (first / rise / mid / approach / end) per hole are in flyover_gate.json; shots for the PC render in flyover_shots.json (8758 frames).
[exit 1]
```

## gate_report.py

```
# Gate report: hansen_dam (18 holes)

Sources: flyover, lidar-proxy. Missing: Unity CourseGreenChecks (checks/greens_all18.csv): run Course Checks > Greens on the PC.

GKD checks: all pass

| hole | source | step cm | lip cm | col dy | tiers | crown m | pins fail | usable % | areas | fall dir | flyover | result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | lidar-proxy+flyover | - | - | - | - | - | 3 | 43 | 26 | - | FAIL | **FAIL** flyover warn: pins(lidar) |
| 3 | lidar-proxy+flyover | - | - | - | - | - | 1 | 61 | 48 | - | FAIL | **FAIL** flyover warn: pins(lidar) |
| 7 | lidar-proxy+flyover | - | - | - | - | - | 0 | 77 | 45 | - | FAIL | **FAIL** flyover |
| 9 | lidar-proxy+flyover | - | - | - | - | - | 3 | 29 | 25 | - | FAIL | **FAIL** flyover warn: pins(lidar) |
| 15 | lidar-proxy+flyover | - | - | - | - | - | 0 | 71 | 37 | - | FAIL | **FAIL** flyover |
| 17 | lidar-proxy+flyover | - | - | - | - | - | 0 | 98 | 76 | - | FAIL | **FAIL** flyover |
| 1 | lidar-proxy+flyover | - | - | - | - | - | 1 | 64 | 48 | - | PASS | PASS warn: pins(lidar) |
| 4 | lidar-proxy+flyover | - | - | - | - | - | 4 | 12 | 12 | - | PASS | PASS warn: pins(lidar) |
| 5 | lidar-proxy+flyover | - | - | - | - | - | 1 | 51 | 31 | - | PASS | PASS warn: pins(lidar) |
| 6 | lidar-proxy+flyover | - | - | - | - | - | 3 | 28 | 19 | - | PASS | PASS warn: pins(lidar) |
| 8 | lidar-proxy+flyover | - | - | - | - | - | 0 | 73 | 38 | - | PASS | PASS |
| 10 | lidar-proxy+flyover | - | - | - | - | - | 0 | 80 | 35 | - | PASS | PASS |
| 11 | lidar-proxy+flyover | - | - | - | - | - | 1 | 46 | 25 | - | PASS | PASS warn: pins(lidar) |
| 12 | lidar-proxy+flyover | - | - | - | - | - | 0 | 92 | 59 | - | PASS | PASS |
| 13 | lidar-proxy+flyover | - | - | - | - | - | 0 | 92 | 54 | - | PASS | PASS |
| 14 | lidar-proxy+flyover | - | - | - | - | - | 0 | 75 | 59 | - | PASS | PASS |
| 16 | lidar-proxy+flyover | - | - | - | - | - | 0 | 86 | 41 | - | PASS | PASS |
| 18 | lidar-proxy+flyover | - | - | - | - | - | 4 | 13 | 10 | - | PASS | PASS warn: pins(lidar) |
wrote progress/gate_report
[exit 1]
```
