def freq(start_freq: int, inlist: list):
    return start_freq + sum(inlist)

assert freq(0, [1,1,-2])==0
assert freq(0, [1,1,1])==3
assert freq(0, [-1,-2,-3])==-6

with open('1.txt') as f:
    a = list()
    for line in f.readlines():
        a.append(int(line.lstrip('+')))
    print(freq(0, a))
