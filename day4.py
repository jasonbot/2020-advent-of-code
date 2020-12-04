import re

fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}

field_re = r"(?P<key>{fields}):(?P<value>\S+)".format(fields="|".join(fields))

match_re = re.compile(field_re)

height_rule = re.compile("(\d+)(in|cm)", re.IGNORECASE)


def int_in_range(minimum, maximum):
    def in_range(value):
        try:
            return minimum <= int(value) <= maximum
        except:
            return False
    return in_range


def height(htstr):
    if not htstr:
        return False

    match = height_rule.match(htstr)
    if match:
        size, units = match.groups()
        size = int(size)
        if units.lower() == 'in':
            return 59 <= size <= 76
        else:
            return 150 <= size <= 193


def hex_color(item):
    if item:
        return re.match("[#][a-f0-9]{6}$", item.lower()) is not None


def pid(value):
    if value:
        return len(value) == 9 and all(i.isdigit() for i in value)


field_rules = {
    'byr': int_in_range(1920, 2002),
    'iyr': int_in_range(2010, 2020),
    'eyr': int_in_range(2020, 2030),
    'hgt': height,
    'hcl': hex_color,
    'ecl': lambda x: x in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
    'pid': pid
}

def passport_flow(filename):
    passport_text = ''
    for line in open(filename):
        if line.strip():
            passport_text += line
        else:
            if passport_text:
                yield passport_text
            passport_text = ''
    if passport_text:
        yield passport_text


def group_fields(filename):
    for passport in passport_flow('day4.input'):
        print(passport)
        yield dict(match_re.findall(passport))


def valid_passports(filename):
    required_keys = fields - {'cid'}
    valid = 0
    super_valid = 0
    for passport in group_fields(filename):
        valid += 1 if all(key in passport for key in required_keys) else 0
        for key, validator in field_rules.items():
            print(key, passport.get(key), validator(passport.get(key)))
        super_valid += 1 if all(validator(passport.get(key)) for key, validator in field_rules.items()) else 0
    return (valid, super_valid)


print(valid_passports('day4.input'))
