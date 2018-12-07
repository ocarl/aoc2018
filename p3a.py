import re


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
             '#3 @ 5,5: 2x2 ']


def find_overlap(inlist: list):
    my_sets = []
    big_set = set()
    ret_set = set()
    for square in inlist:
        my_sets.append(generate_set(square)[1])
        ret_set.update(big_set.intersection(my_sets[-1]))
        big_set.update(my_sets[-1])
    return ret_set

assert find_overlap(test_list) == {(3, 3), (3, 4), (4, 3), (4, 4)}

with open('3.txt') as f:
    inlist = f.readlines()
    print(len(find_overlap(inlist)))
