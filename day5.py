total_range = list(range(128))

def ss(string, set_total=total_range):
    seat = 4
    sm = 4
    seat = list(range(8))

    # print(string, set_total)

    string = string.strip()
    for s in string:
        if len(set_total) == 1:
            if s.lower() == 'l':
                seat = seat[:len(seat)//2]
            else:
                seat = seat[len(seat)//2:]
        elif s.lower() == 'f':
            set_total = set_total[:len(set_total)//2]
        else:
            set_total = set_total[len(set_total)//2:]
        if len(set_total) == 1 and len(seat) == 1:
            print('->', string, set_total[0], seat[0], (set_total[0] * 8) + seat[0])
            return set_total[0], seat[0], (set_total[0] * 8) + seat[0]

with open('day5.input') as line:
    print(max(list(ss(l)[-1] for l in line)))

with open('day5.input') as line:
    print(set(sorted(ss(l)[-1] for l in line)) ^ set(range(832)))
