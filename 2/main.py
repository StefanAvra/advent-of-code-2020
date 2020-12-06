import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def check_password(policy, pw):
    lowest, highest, policy_char = policy_splitter(policy)
    return lowest <= pw.count(policy_char) <= highest

def check_password_part_two(policy, pw):
    first, second, policy_char = policy_splitter(policy)
    print(first, second, policy_char, pw)
    return (pw[first-1] == policy_char) != (pw[second-1] == policy_char)

def policy_splitter(policy):
    policy_range, policy_char = policy.split(' ')
    first, second = policy_range.split('-')
    return [int(first), int(second), policy_char]

with open('input.txt') as f:
    lines = f.readlines()

count_pw_ok = 0
count_pw_ok_part_two = 0
for line in lines:
    count_pw_ok += 1 if check_password(*line.split(': ')) else 0
    count_pw_ok_part_two += 1 if check_password_part_two(*line.split(': ')) else 0
    print(check_password_part_two(*line.split(': ')))


print(count_pw_ok, count_pw_ok_part_two)
