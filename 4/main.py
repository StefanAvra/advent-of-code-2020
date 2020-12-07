import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
with open('input.txt') as f:
    lines = f.readlines()

def passport_parser(lines):
    passports = []
    passport = {}
    for line in lines:
        if line == '\n':
            passports.append(passport)
            passport = {}
        else:
            line = line.rstrip('\n')
            pairs = line.split(' ')
            for pair in pairs:
                key, value = pair.split(':')
                passport[key] = value
    passports.append(passport)
    return passports


def validator(passport):
    keys = (
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
    )
    for key in keys:
        if not key in passport:
            return False
    return True

count_valid_passports = 0
for passport in passport_parser(lines):
    count_valid_passports += 1 if validator(passport) else 0
print(count_valid_passports)
