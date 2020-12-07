import os
import functools
os.chdir(os.path.dirname(os.path.abspath(__file__)))
with open('input.txt') as f:
    lines = f.readlines()


def get_row(space_string):
    binary = space_string.replace('F', '0').replace('B', '1')
    return int(f'0b{"".join(binary)}', 2)


def get_col(space_string):
    binary = space_string.replace('L', '0').replace('R', '1')
    return int(f'0b{"".join(binary)}', 2)


def get_seat_id(row, col):
    return row * 8 + col


seat_ids = []
for line in lines:
    line = line.strip('\n')
    row = get_row(line[:7])
    col = get_col(line[7:10])
    seat_id = get_seat_id(row, col)
    seat_ids.append(seat_id)
    # print(f'{line}: {row}, {col}, {seat_id}')

print(max(seat_ids))


def find_my_seat():
    seat_id_range = [n for n in range(min(seat_ids), max(seat_ids)+1)]
    return [seat for seat in seat_id_range if seat not in seat_ids]


print(find_my_seat())
