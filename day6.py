def group_lines(all=False):
    group_line_set = None
    for line in open('day6.input'):
        if line.strip():
            if group_line_set is None:
                group_line_set = set(line.strip())
            else:
                if all:
                    group_line_set &= set(line.strip())
                else:
                    group_line_set |= set(line.strip())
        else:
            yield group_line_set
            group_line_set = None

    if group_line_set is not None:
        yield group_line_set

for ll in group_lines():
    print(ll)

print(sum([len(l) for l in group_lines(all=False)]))
print(sum([len(l) for l in group_lines(all=True)]))
