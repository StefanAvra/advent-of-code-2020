import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def check_slope(to_right, down):
    with open('input.txt') as f:
        lines = f.readlines()
    lines = [line.rstrip('\n') for line in lines]
    trees = 0
    pos = 0
    lines.pop(0)
    while lines:
        pos += to_right
        pos = pos % len(lines[0])
        try:
            for i in range(down-1):
                lines.pop(0)
            line = lines.pop(0)
            trees += 1 if line[pos] == '#' else 0
        except IndexError as e:
            pass
    return trees


slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]
result = 1
for slope in slopes:
    trees = check_slope(*slope)
    print(f'{trees} trees in slope {slope}')
    result *= trees

print(result)
