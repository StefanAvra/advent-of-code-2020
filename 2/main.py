import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def check_password(policy, pw):
    policy_range, policy_char = policy.split(' ')
    lowest, highest = policy_range.split('-')
    return int(lowest) <= pw.count(policy_char) <= int(highest)


with open('input.txt') as f:
    lines = f.readlines()

count_pw_ok = 0
for line in lines:
    count_pw_ok += 1 if check_password(*line.split(': ')) else 0

print(count_pw_ok)
