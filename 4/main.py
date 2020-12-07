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


def validator_two(passport):
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
        else:
            value = passport[key]
            if key == 'byr':
                if len(value) != 4 or not 1920 <= int(value) <= 2002:
                    return False
            if key == 'iyr':
                if len(value) != 4 or not 2010 <= int(value) <= 2020:
                    return False
            if key == 'eyr':
                if len(value) != 4 or not 2020 <= int(value) <= 2030:
                    return False
            if key == 'hgt':
                if value[-2:] == 'cm':
                    if not 150 <= int(value.rstrip('cm')) <= 193:
                        return False 
                elif value[-2:] == 'in':
                    if not 59 <= int(value.rstrip('in')) <= 76:
                        return False 
                else:
                    return False
            if key == 'hcl':
                if value[0] == '#':
                    if len(value) != 7:
                        return False
                    for char in value[1:]:
                        if char.lower() not in '1234567890abcdef':
                            return False
                else:
                    return False
            if key == 'ecl':
                if value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    return False
            if key == 'pid':
                if len(value) != 9:
                    return False
                try:
                    int(value)
                except ValueError as e:
                    return False                
    return True


count_valid_passports = 0
count_valid_passports_two = 0
for passport in passport_parser(lines):
    count_valid_passports += 1 if validator(passport) else 0
    count_valid_passports_two += 1 if validator_two(passport) else 0
print(count_valid_passports, count_valid_passports_two)
