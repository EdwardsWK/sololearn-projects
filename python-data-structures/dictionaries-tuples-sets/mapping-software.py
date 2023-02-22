"""Mapping Software

    You are working on a mapping software. The map is stored as a list of points, where
    each item is represented as a tuple, containing the X and Y coordinates of the point.
    You need to calculate and output the distance to the closest point from the point (0, 0).
"""

import math

points = [
    (12, 55),
    (880, 123),
    (64, 64),
    (190, 1024),
    (77, 33),
    (42, 11),
    (0, 90)
]

distance = list(range(len(points)))
z = 0

for (x,y) in points:
    distance[z] = math.sqrt((x ** 2) + (y ** 2))
    z += 1

print(min(distance))
