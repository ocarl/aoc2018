from collections import defaultdict as ddict
from p1a import freq

def freq_check(start_freq: int, inlist: list):
    seen = ddict(lambda :0)
    curr_freq = start_freq
    seen[curr_freq] += 1
    while seen[curr_freq] < 2:
        curr_freq = freq(curr_freq, inlist[:1])
        inlist.append(inlist.pop(0))
        seen[curr_freq] += 1
    return curr_freq

assert freq_check(0, [1,-1])==0
assert freq_check(0, [3,3,4,-2,-4])==10
assert freq_check(0, [-6,3,8,5,-6])==5
assert freq_check(0, [7,7,-2,-7,-4])==14

with open('1.txt') as f:
    a = list()
    for line in f.readlines():
        a.append(int(line.lstrip('+')))
    print(freq_check(0, a))
