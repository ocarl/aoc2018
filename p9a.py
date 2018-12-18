from collections import defaultdict
from itertools import cycle

real_input = '430 players; last marble is worth 71588 points'


def calc_score(no_players, top_score):
    score = defaultdict(lambda : 0)
    ring = []
    curr_index = 0
    ring.insert(curr_index, 0)
    for i in range(1,10):
        while curr_index > len([0]*10)
            curr_index += 2



        insert_into_ring(curr_index, i, ring)
        print(curr_index, ring)

    return max(score.values())


def insert_into_ring(curr_index, i, ring):
    if curr_index == 0:
        ring.append(i)
    else:
        ring.insert(curr_index, i)


print(calc_score(9, 25))






assert calc_score(10, 1618) == 8317
assert calc_score(13, 7999) == 146373
assert calc_score(17, 1104) == 2764
assert calc_score(21, 6111) == 54718
assert calc_score(30, 5807) == 37305