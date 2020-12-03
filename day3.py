import functools


def make_matrix(filename):
    with open(filename, 'r') as file_handle:
        return list(l.strip() for l in file_handle)


def traverse(*deltas, origin=(0,0)):
    x, y = origin
    yield (x, y)
    while True:
        for xd, yd in deltas:
            if xd:
                for _ in range(xd):
                    x += 1
            elif yd:
                for _ in range(yd):
                    y += 1
            else:
                raise ValueError((xd, yd))
        yield (x, y)


def print_matrix(matrix, visits):
    col_map = {
        ('.', False): '.',
        ('#', False): '#',
        ('.', True): 'O',
        ('#', True): 'X',
    }
    for row_index, row in enumerate(matrix):
        for col_index, col in enumerate(row):
            print(col_map[(col, (col_index, row_index) in visits)], end='')
        print()


def trees_hit(matrix, visits):
    return sum(1 for x, y in visits if matrix[y][x] == '#')

def visit(matrix, delta):
    visited_coordinates = set()
    xd, yd = delta
    for x, y in traverse((xd, None), (None, yd)):
        if y >= len(matrix):
            break
        visited_coordinates.add((x % len(matrix[y]), y))
    return visited_coordinates


matrix = make_matrix('day3.input')


visited_coordinates = visit(matrix, (3, 1))
# print(visited_coordinates)
# print_matrix(matrix, visited_coordinates)
print(trees_hit(matrix, visited_coordinates))

for delta in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
    visited_coordinates = visit(matrix, delta)
    print(delta, '->', trees_hit(matrix, visited_coordinates))

trees_array = [trees_hit(matrix, visit(matrix, delta)) for delta in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))]
print(functools.reduce(lambda x, y: x * y, trees_array))
