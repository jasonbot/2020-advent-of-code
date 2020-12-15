import itertools

def window(window_size=25, sequence=2):
    with open('day9.input') as number_stream:
        stream = iter(number_stream)
        window = []
        while len(window) < window_size:
            window.append(int(next(stream).strip()))

        while len(window) > sequence:
            # print(window, stream)
            try:
                if stream:
                    window.append(int(next(stream)))
            except StopIteration:
                stream = None

            # print([(sum(items), (items,)) for items in itertools.combinations(window[:-1], sequence)])
            for item in window[(-(window_size + 2)):-1]:
                # print(item, window[-window_size:-1], len(window[-window_size:-1]), window[-1])

                items = window[-(window_size+1):-1]

                if any (s == window[-1] for s in (sum(i) for i in itertools.combinations(items, 2))):
                    pass
                else:
                    return window[-1]

            window = window[1:]

def find_number(num):
    with open('day9.input') as number_stream:
        stream = [int(line.strip()) for line in number_stream]
        for start in range(0, len(stream)):
            for end in range(start, len(stream)):
                if sum(stream[start:end]) == num:
                    st = stream[start:end]
                    return(min(st) + max(st))
                # print(start, end, stream[start:end])


print(window())
num = window()
print(find_number(num))
