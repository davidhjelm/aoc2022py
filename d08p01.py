f = open("inputs/d08", "r")

test_grid = """30373
25512
65332
33549
35390"""

grid = []

for iy, y in enumerate(f.readlines()):
    for x in y.strip("\n"):
        if len(grid) < iy + 1:
            grid.append([])
        grid[iy].append(int(x))

height = len(grid)
width = len(grid[0])


def is_visible(y, x):
    visible_dirs = 4
    t_height = int(grid[y][x])
    # up
    yy = y - 1
    while yy >= 0:
        if int(grid[yy][x]) >= t_height:
            visible_dirs -= 1
            break
        yy -= 1
    # right
    xx = x + 1
    while xx < width:
        if int(grid[y][xx]) >= t_height:
            visible_dirs -= 1
            break
        xx += 1
    # down
    yy = y + 1
    while yy < height:
        if int(grid[yy][x]) >= t_height:
            visible_dirs -= 1
            break
        yy += 1
    # left
    xx = x - 1
    while xx >= 0:
        if int(grid[y][xx]) >= t_height:
            visible_dirs -= 1
            break
        xx -= 1

    if visible_dirs == 0:
        return False
    else:
        return True


not_visible_count = 0
for iy, y in enumerate(grid):
    if iy == 0 or iy == height - 1:
        continue
    for ix, x in enumerate(grid[iy]):
        if ix == 0 or ix == width - 1:
            continue
        if not is_visible(iy, ix):
            not_visible_count += 1

total = sum([len(x) for x in grid])
print(total - not_visible_count)
