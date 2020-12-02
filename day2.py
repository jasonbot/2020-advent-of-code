import re


re_match = re.compile('(?P<min>[0-9]+)-(?P<max>[0-9]+) (?P<char>[a-z]+): (?P<password>.+)')


def valid1(line):
    match = re_match.search(line.strip())
    min, max = int(match['min']), int(match['max'])
    char = match['char']
    password = match['password']
    matches = len([character for character in password if character in char])
    # print(match, min, max, password, matches)
    return min <= matches <= max


def valid2(line):
    match = re_match.search(line.strip())
    min, max = int(match['min']), int(match['max'])
    char = match['char']
    password = match['password']
    match_substr = [password[min - 1], password[max - 1]]
    matches = [s for s in match_substr if s in char]
    # print("[ X ]" if len(matches) == 1 else "[   ]", line.strip(), min, max, match_substr, matches, len(matches) == 1)
    return len(matches) == 1


print(len([1 for line in open('day2.input') if valid1(line)]))
print(len([1 for line in open('day2.input') if valid2(line)]))
