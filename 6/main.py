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
