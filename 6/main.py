import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
with open('input.txt') as f:
    lines = f.readlines()


def get_answers():
    groups = []
    group = set()
    for line in lines:
        if line == '\n':
            groups.append(group)
            group = set()
        else:
            line = line.rstrip('\n')
            for char in line:
                group.add(char)
    groups.append(group)
    return groups


count_answers = [len(answers) for answers in get_answers()]

print(sum(count_answers))


def get_groups():
    groups = []
    group = []
    for line in lines:
        if line == '\n':
            groups.append(group)
            group = []
        else:
            person = line.rstrip('\n')
            group.append(person)
    groups.append(group)
    return groups


everyone_yes = []
for group in get_groups():
    if len(group) == 1:
        everyone_yes.append(len(group[0]))
    else:
        check = group[0]
        group_yes = 0
        for person in group:
            for answer in check:
                if answer not in person:
                    check = check.replace(answer, '')
        group_yes += len(check)
        everyone_yes.append(group_yes)

print(sum(everyone_yes))

