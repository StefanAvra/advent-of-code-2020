import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
with open('input.txt') as f:
    lines = f.readlines()
lines = [int(line.rstrip('\n')) for line in lines]
# write once
result = None
for a in lines:
    for b in lines:
        if a + b == 2020:
            result = a * b
print(result)

# copy once
result = None
for a in lines:
    for b in lines:
        for c in lines:
            if a + b + c == 2020:
                result = a * b * c
print(f'part two: {result}')