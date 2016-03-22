#!/usr/bin/env python3.5

import fileinput

points = {}
counts = {}

for line in fileinput.input():
    try:
        data = line.split(":")

        colours = int(data[1])
        x = float(data[3])
        y = float(data[5])
        z = float(data[4])

        point = (colours,x,y)

        if point in points:
            points[point] += z
            counts[point] += 1
        else:
            points[point] = z
            counts[point] = 1
    except ValueError:
        pass

keys = sorted(points.keys())

for point in keys:
    print(point[0], point[1], point[2], points[point] / counts[point])
