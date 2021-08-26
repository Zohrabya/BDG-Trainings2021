#!usr/bin/env python3

points = []
i, j = 0, 0
coordinate_x = input("Enter the x part of the coordinate: ")
while coordinate_x != '':
    points.append([])
    points[i].append(int(coordinate_x))
    coordinate_y = int(input("Enter the y part of the coordinate: "))
    points[i].append(coordinate_y)
    coordinate_x = input("Enter the x part of the coordinate: (blank to quit): ")
    i += 1

distances = []

for k in range(0, len(points)-1):
    dist = ((points[k + 1][0] - points[k][0]) ** 2 + (points[k + 1][1] - points[k][1]) ** 2) ** (1 / 2)
    distances.append(dist)
dist = ((points[len(points) - 1][0] - points[0][0]) ** 2 + (points[len(points) - 1][1] - points[0][1]) ** 2) ** (1 / 2)
distances.append(dist)

print("The perimeter of that polygon is:", sum(distances))
