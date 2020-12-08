def group_lines():
    for group in open('day6.input'):
        line_ = set()
        for line in group:
            if line.strip():
                line_ |= set(line.strip())
            else:
                yield line_, len(line_)
                line_ = set()

    if line_:
        yield line_, len(line_)

for ll in group_lines():
    print(ll)

print(sum([l[1] for l in group_lines()]))
