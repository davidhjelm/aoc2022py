f = open("inputs/d08", "r")

grid = []

for iy, y in enumerate(f.readlines()):
    for x in y.strip("\n"):
        if len(grid) < iy + 1:
            grid.append([])
        grid[iy].append(int(x))

height = len(grid)
width = len(grid[0])


def get_score(y, x):
    t_height = int(grid[y][x])
    score = []
    # up
    yy = y - 1
    s = 0
    while yy >= 0:
        s += 1
        if int(grid[yy][x]) >= t_height:
            break
        yy -= 1
    score.append(s)
    # right
    xx = x + 1
    s = 0
    while xx < width:
        s += 1
        if int(grid[y][xx]) >= t_height:
            break
        xx += 1
    score.append(s)
    # down
    yy = y + 1
    s = 0
    while yy < height:
        s += 1
        if int(grid[yy][x]) >= t_height:
            break
        yy += 1
    score.append(s)
    # left
    xx = x - 1
    s = 0
    while xx >= 0:
        s += 1
        if int(grid[y][xx]) >= t_height:
            break
        xx -= 1
    score.append(s)

    return score[0] * score[1] * score[2] * score[3]


max = 0
for iy, y in enumerate(grid):
    if iy == 0 or iy == height - 1:
        continue
    for ix, x in enumerate(grid[iy]):
        if ix == 0 or ix == width - 1:
            continue
        s = get_score(iy, ix)
        if s > max:
            max = s

print(max)
