import os

template = """import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
with open('input.txt') as f:
    lines = f.readlines()
"""
empty_files = ['input.txt', 'README.md']
day = '8'

os.chdir(os.path.dirname(os.path.abspath(__file__)))

if not os.path.exists(day):
    os.mkdir(day)
os.chdir(day)
if not os.path.exists('main.py'):
    with open('main.py', 'w+') as f:
        f.writelines(template)

for f in empty_files:
    if not os.path.exists(f):
        open(f, 'x')
