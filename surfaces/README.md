# 0.5 m bare-earth surfaces (Hansen Dam)
`surface_05m.npz` (numpy): `h` uint16 = Unity y in centimetres (y = elevation - 207 m), 0 = outside the mask;
cell (row r, col c) centre at Unity x = x0 + 0.5 c, z = z0 + 0.5 r (rows run south to north); `res` = 0.5.
Mask = greens + 6 m, fairways + 5 m, tees + 3 m (from course.svg). Built from 37.6 M LiDAR ground points
(2023 QL1, about 11 ground points per m2), 99.2 % of cells have their own points, light 0.3 m smoothing only.
Conform the green, collar, fairway and tee meshes to this, not to the 1.66 m heightmap.
Read in C#: np.load in Python -> `python -c "import numpy as np; d=np.load('surface_05m.npz'); d['h'].tofile('h.raw')"`
gives the same data as `surface_05m_5046x2664.raw` (included: 5046 wide x 2664 tall, little-endian uint16, row 0 = south).  Script: ../scripts/surfaces_05m.py
