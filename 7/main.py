import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
with open('input.txt') as f:
    lines = f.readlines()

bag_rules = {}


def init_bag_rules():
    for line in lines:
        line = line.rstrip('.\n')
        line = line.split(' bags contain ')
        if 'no other bags' in line[1]:
            bag_rules[line[0]] = 0
        else:
            bags = line[1].split(', ')
            bags = [(bag[2:-4], bag[2:-5])['bags' in bag] for bag in bags]
            bag_rules[line[0]] = bags


def check_shiny_gold(rule):
    # print(f'checking: {rule}')
    if rule == 0:
        return 0
    bag_count = 0
    for bag in rule:
        if bag == 'shiny gold':
            bag_count += 1
        else:
            bag_count += check_shiny_gold(bag_rules.get(bag))
    return bag_count


init_bag_rules()


can_contain_shiny_gold = []
for key, value in bag_rules.items():
    if check_shiny_gold(value):
        can_contain_shiny_gold.append(key)

print(len(can_contain_shiny_gold))
