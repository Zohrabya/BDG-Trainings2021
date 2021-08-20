#!usr/bin/env python3

points = []
i, j = 0, 0
coordinate_x = input()
while coordinate_x != '':
    points.append([])
    points[i].append(int(coordinate_x))
    coordinate_y = int(input())
    points[i].append(coordinate_y)
    coordinate_x = input()
    i += 1

print(points)

distances = []


def calculate_perimeter (*list):
    for k in range(0, len(list)-1):
        dist = ((list[k + 1][0] - list[k][0]) ** 2 + (list[k + 1][1] - list[k][1]) ** 2) ** (1 / 2)
        distances.append(dist)
    dist = ((list[len(list) - 1][0] - list[0][0]) ** 2 + (list[len(list) - 1][1] - list[0][1]) ** 2) ** (1 / 2)
    distances.append(dist)
    poly_perimeter = sum(distances)
    return poly_perimeter


print(calculate_perimeter(*points))
