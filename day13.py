import collections

def get_times(line):
    return [int(x) for x in line.strip().split(',') if x != 'x']


def get_ekses(line):
    ekses = collections.defaultdict(int)
    key = None
    for x in line.strip().split(','):
        if x == 'x':
            ekses[key] += 1
        else:
            key = int(x)
    return ekses


def iterate_times(times, starting=0):
    time = starting

    while True:
        yield (time, [t for t in times if time % t== 0])
        time += 1


def window(iterable, slice):
    window = tuple()
    for it in iterable:
        window += (it,)
        if len(window) == slice:
            yield window
            window = window[1:]


def validate_loop(keys, indexes, ekses):
    # print("    Checking work", keys, indexes, ekses)
    for prev, next in window(keys, 2):
        # print(f"         Matching {prev}({indexes[prev]}) - {next}({indexes[next]}) ({ekses[prev]} -- {indexes[next] - indexes[prev]})")
        if ekses[prev] != ((indexes[next] - indexes[prev]) - 1):
            return False
    return True


with open('day13.input') as input:
    time = int(next(input).strip())
    time_line_value = next(input)


time_line = get_times(time_line_value)
ekses = get_ekses(time_line_value)

# Day 1
for current_time, lines in iterate_times(time_line, time):
    if lines:
        print(current_time, [(current_time - time) * l for l in lines])
        break

# Day 2
time_window = []
index = None
indexes = {}
for current_time, lines in iterate_times(time_line, 0):
    if current_time % 100000 == 0:
        print("AT", current_time)
    if lines:
        next_line = max(time_line.index(i) for i in lines)
        if next_line == 0:
            indexes.clear()
            indexes.update({line: current_time for line in lines})
        elif indexes:
            indexes.update({line: current_time for line in lines})
            # print(f"Leaves at {current_time}: {lines} ({indexes})")
            if len(time_line) == len(indexes):
                vl = validate_loop(time_line, indexes, ekses)
                if vl:
                    raise ValueError(current_time)
                indexes.clear()
        else:
            indexes.clear()

    if False:  # current_time > 3450:
        break
