import itertools

jolts = [0] + sorted(int(x.strip()) for x in open('day10.input') if x.strip())
jolts += [jolts[-1] + 3]


def one():
    diffs = []

    ones = 0
    threes = 0
    for x in range(1, len(jolts)):
        jolt_diff = abs(jolts[x] - jolts[x - 1])

        diffs.append(jolt_diff)

        if jolt_diff == 1:
            ones += 1
        elif jolt_diff == 3:
            threes += 1
        else:
            raise ValueError("NO")
        
    print(ones, threes, len(jolts), ones + threes, ones * threes)
    return diffs


_memory = {}

def traversal(current, rest, depth=0):
    if not rest:
        return 1

    if current not in _memory:
        total = 1
        if (rest[0] - current) < 3:
            print(" " * depth, "Can skip", current, rest)
            total = traversal(rest[1], rest[2:], depth+1)

        _memory[current] = total + traversal(rest[0], rest[1:], depth+1)

    return _memory[current]



def two(diffs):
    print(traversal(diffs[0], diffs[1:]))

diffs = one()
two(jolts)
