import re
from collections import Counter


def generate_set(instring: str):
    numbers = [int(num) for num in re.findall('\d+', instring)]
    id = numbers[0]
    pos = numbers[1], numbers[2]
    size = numbers[3], numbers[4]
    x, y = [], []
    for i in range(size[0]):
        for j in range(size[1]):
            x.append(pos[0] + i)
            y.append(pos[1] + j)
    return id, set(zip(x, y))


assert generate_set('#1 @ 1,1: 2x2') == (1, {(1, 2), (1, 1), (2, 1), (2, 2)})

test_list = ['#1 @ 1,3: 4x4',
             '#2 @ 3,1: 4x4',
             '#3 @ 5,5: 2x2',
             '#4 @ 1,1: 1x1',
             '#5 @ 1,1: 2x2']


def find_unique(inlist: list):
    pos_count = Counter()
    for square in inlist:
        this_square = generate_set(square)
        for pos in this_square[1]:
            pos_count[pos] += 1
    for square in inlist:
        pos_count2 = pos_count.copy()
        this_square = generate_set(square)
        check_list = []
        for pos in this_square[1]:
            pos_count2[pos] -= 1
            check_list.append(pos_count2[pos])
        if [0]*len(this_square[1]) == check_list:
            return this_square[0]

print(find_unique(test_list))
assert find_unique(test_list) == 3

with open('3.txt') as f:
    inlist = f.readlines()
    print(find_unique(inlist))
