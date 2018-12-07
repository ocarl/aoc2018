import re

test_input = '''1, 1
1, 6
8, 3
3, 4
5, 5
8, 9'''


class Node:
    def __init__(self, x, y, inlist):
        self.x = x
        self.y = y
        self.inlist = inlist

    def sum_distance_to(self):
        dist = 0
        for innode in self.inlist:
            dist += abs(self.x - innode[0]) + abs(self.y - innode[1])
        return dist

    def in_region(self):
        return self.sum_distance_to() < limit

def parse_input(instring: str):
    xa, ya = [], []
    for line in instring.split('\n'):
        nums = re.findall('\d+', line)
        xa.append(int(nums[0]))
        ya.append(int(nums[1]))
    return xa, ya

if __name__ == '__main__':
    global limit
    limit = 10000
    with open('6.txt') as f:
        test_input = f.read()
        xa, ya = parse_input(test_input)
        nodes_in_region = []
        for i in range(min(xa)-1, max(xa)+1):
            for j in range(min(ya)-1, max(ya)+1):
                this_node = Node(i,j, zip(xa,ya))
                if this_node.in_region():
                    nodes_in_region.append(this_node)
        print(len(nodes_in_region))
        print('#########')
