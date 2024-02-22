import math


path1 = input()
path2 = input()

with open(path1) as f:
    my_line = f.readline()
    x1, y1 = int(my_line[0]), int(my_line[2])
    radius = int(f.readline(2))

with open(path2) as f:
    for line in f:
        x2, y2 = int(line[0]), int(line[2])
        d = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

        if d > radius:
            print(2)
        elif d < radius:
            print(1)
        else:
            print(0)
