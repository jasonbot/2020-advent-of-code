import collections
import copy

grid = [list(l.strip()) for l in open('day11.input')]


def neighbors(grid, row, col):
    for yd in range(-1, 2):
        for xd in range(-1, 2):
            if (yd, xd) != (0, 0):
                # print(row, col, row + yd, col + xd)
                try:
                    yield grid[row + yd][col + xd]
                except IndexError:
                    pass
    # print("--")


def visit(grid):
    delta = {}

    for row_num, row in enumerate(grid):
        for col_num, col in enumerate(row):
            ct = collections.Counter(neighbors(grid, row_num, col_num))
            # print(ct)
            if col == 'L' and ct.get('#', 0) == 0:
                delta[(row_num, col_num)] = '#'
            elif col == '#' and ct.get('#', 0) > 3:
                delta[(row_num, col_num)] = 'L'
    
    return delta


def apply_deltas(grid, deltas):
    new_grid = copy.deepcopy(grid)

    for (row, col), value in deltas.items():
        new_grid[row][col] = value
    
    return new_grid


def stabilize(grid):
    deltas = {None: None}
    day = 0

    while deltas:
        deltas = visit(grid)
        print("Day", day, ":", len(deltas))
        grid = apply_deltas(grid, deltas)
        day += 1
    
    ct = 0
    for row in grid:
        for col in row:
            if col == '#':
                ct += 1

    return day, ct

print(stabilize(grid))
