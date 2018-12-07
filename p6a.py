import re

test_input = '''1, 1
1, 6
8, 3
3, 4
5, 5
8, 9'''


class Node:
    nodes = []

    def __init__(self, x, y, inlist):
        self.x = x
        self.y = y
        self.inlist = inlist
        self.owned_by = self.closest_to(self.inlist)
        Node.nodes.append(self)

    def to_tuple(self):
        return self.x, self.y

    def distance_to(self, innode):
        dist = abs(self.x - innode[0]) + abs(self.y - innode[1])
        return dist

    def closest_to(self, inlist):
        distances = dict()
        # find distance to each base node
        for base in inlist:
            distances[base] = self.distance_to(base)
        min_val = 9999999999
        # find closest base node
        for val in distances.values():
            if val < min_val:
                min_val = val
        vals = list(distances.values())
        if vals.count(min_val) > 1:
            return 0, 0
        for key in distances.keys():
            if distances[key] == min_val:
                return key

def parse_input(instring: str):
    xa, ya = [], []
    for line in instring.split('\n'):
        nums = re.findall('\d+', line)
        xa.append(int(nums[0]))
        ya.append(int(nums[1]))
    return xa, ya

if __name__ == '__main__':
    with open('6.txt') as f:
        test_input = f.read()
        xa, ya = parse_input(test_input)
        infinite_seeds = []
        for i in range(min(xa)-1, max(xa)+1):
            for j in range(min(ya)-1, max(ya)+1):
                this_node = Node(i,j, zip(xa,ya))
                if i == min(xa) or i == max(xa) or j == min(ya) or j == max(ya):
                    infinite_seeds.append(this_node.owned_by)
        # remove infinites
        area_dict = dict()
        for node in Node.nodes:
            if node.owned_by not in infinite_seeds and node.owned_by != (0,0):
                area_dict[node.to_tuple()] = node.owned_by
        #find most common entry
        vals = list(area_dict.values())
        most_common = max(vals, key=vals.count)
        print('{}: {}'.format(most_common, vals.count(most_common)))
        print('#########')
