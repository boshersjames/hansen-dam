# HansenDam GSPro course

Real course rebuilt for GSPro (Unity 2018.2.8f1, OPCD). Toolkit: `../course-build` (the course-build repo). Read its
`README.md` once, then the skill for the element you are working on in `../course-build/skills/`. All thresholds come from
`../course-build/rules/*.json`; this course's overrides are in `course.json` under `rule_overrides`.

## Where things are
- `course.json`: frame, paths, GKD fields, tee slot map, overrides. Every script reads paths from here.
- Unity project: `C:\GSP\HansenDam_Project`. Editor tools in `Assets\Editor\` are copies from `../course-build\unity\shared\`; sync with
  `../course-build\automation\Run-CourseAutomation.ps1 -SyncTools`.
- Automation output: `C:\GSP\HansenDam_Project\AutomationOutput\latest.txt` then that folder's `summary.md` and `shots\`.
- Never change `C:\GSProV1\Core\GSP\Courses\` without backing up the GKD first.

## Driving Unity
- Unity closed: `../course-build\automation\Run-CourseAutomation.ps1 -Config automation\HansenDam.json [-Steps "a,b"]`.
- Unity open: `../course-build\automation\Send-UnityCommand.ps1 <ping|run|shots|invoke|describe|menu|save|refresh>`.

## Process
Follow `course-build-gates`: one hole, one edit, photo pair each; control hole before/after on course-wide passes; back up
scene, terrain and GKD before every change. Run the LiDAR review (D1-D18) before the first gate and record answers in
`course_photos/decisions.csv`.

## Cost discipline
Measure with tools, not eyes. Colour: `colour_match.py`. Green edges: the edge survey. Pins: the pin-area test. Read the
summary a tool writes; open a render only when a number says something is wrong.

## This course
Split out of the moorpark repo (branch `claude/project-thread-f78r3v`, `courses/hansen_dam`). `README.md` has the full data history.
- Frame: 3400 m square centred on 34.258619, -118.390880 (EPSG:6340, SW 370241.16 E, 3790006.81 N), y = elevation - 207 m,
  Unity Terrain 3400 x 191 x 3400 (1.66 m per sample). Ground 207.1 to 396.5 m (hills NW and the dam; the course is flat).
- Survey: USGS 3DEP `CA_LosAngeles_1_B23` (QL1, 2023-24), 21.7 pts/m2, no vegetation classes. Satellite NAIP 8192 px (0.42 m/px).
- `course.json` carries coursekit's keys (`size`, `sw_e`, `sw_n`, `y_offset`, `epsg`, `terrain_height`, `gkd`) beside the
  toolkit's (`frame`, `paths`, `lidar`, `holes`, `gps`); keep both in step. `paths.gkd` is `HansenDam.GKD` at the repo root.
- Open questions: greens over 3% tilt on 2, 4, 6, 18 (checks/green_slopes.csv); Black tees on 3 and 11 sit behind the mapped
  start; the 16 interior OB patches and the hole 16 pond (penalty area, no drop zone) need BoJa's look.
- `points.npz` (1.9 GB) is not in git: `python ../moorpark/coursekit.py lidar --ept CA_LosAngeles_1_B23` rebuilds it.
