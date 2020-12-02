import itertools

numbers = [int(line.strip()) for line in open('day1.input')]

for x, y in itertools.combinations(numbers, 2):
    if x + y == 2020:
        print(x * y)

for x, y, z in itertools.combinations(numbers, 3):
    if x + y + z == 2020:
        print(x * y * z)
