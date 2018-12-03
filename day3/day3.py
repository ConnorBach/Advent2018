import sys
from collections import Counter

l = list(sys.stdin)

grid = [[0 for i in range(2000)] for _ in range(2000)]
gridID = [[[] for i in range(2000)] for _ in range(2000)]

sizex = 0
sizey = 0

ansID = -1
ids = []

idSize = {}

for line in l:
    line = line.strip()
    parse = line.split()
    curID = parse[0]
    curID = curID[1:]

    loc = parse[2]
    loc = loc.split(',')
    locx = int(loc[0])
    locy = loc[1]
    locy = int(locy[:-1])

    size = parse[3]
    size = size.split('x')
    sizex = int(size[0])
    sizey = int(size[1])

    idSize[int(curID)] = sizex * sizey

    for i in range(sizex):
        for j in range(sizey):
            grid[locx+i][locy+j] += 1
            gridID[locx+i][locy+j].append(curID)

ans = 0
ids = []
for i in range(2000):
    for j in range(2000):
        if grid[i][j] >= 2:
            ans += 1
        if len(gridID[i][j]) == 1:
            ids.append(gridID[i][j][0])

idMap = {}
for i in ids:
    if i in idMap:
        idMap[i] += 1
    else:
        idMap[i] = 1

ans = ''
for key, val in idMap.items():
    if val == idSize[int(key)]:
        print('match: ', key, val, idSize[int(key)])
        print(key)
