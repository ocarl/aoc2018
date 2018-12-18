import xml.etree.ElementTree as ET
import sys

with open('8.txt') as f:

    sys.setrecursionlimit(3000)

    test_input = '''2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'''

    test_input = f.read()

    inlist = iter([int(x) for x in test_input.split(' ')])

    root = ET.Element('root')

    def calc_value(node):
        if len(list(node)) == 0:
            return sum(node.attrib['metadata'])
        else:
            val = 0
            for index in node.attrib['metadata']:
                if index > len(list(node) or index == 0):
                    val += 0
                else:
                    child_at_index = list(node)[index-1]
                    val += calc_value(child_at_index)
            return val


    def add_node(root, inlist):
        no_children = next(inlist)
        no_meta = next(inlist)
        if no_children == 0:
            metalist = []
            for _ in range(no_meta):
                metalist.append(next(inlist))
            root.attrib['metadata'] = metalist
        else:
            for _ in range(no_children):
                child = ET.Element('child')
                next_round = add_node(child, inlist)
                root.append(next_round)
            metalist = []
            for _ in range(no_meta):
                metalist.append(next(inlist))
            root.attrib['metadata'] = metalist
        return root

    root = add_node(root, inlist)

    print(calc_value(root))

