import xml.etree.ElementTree as ET

with open('8.txt') as f:
    test_input = '''2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'''

    test_input = f.read()

    inlist = iter([int(x) for x in test_input.split(' ')])

    root = ET.Element('root')

    def add_node(root, inlist, iter_sum):
        no_children = next(inlist)
        no_meta = next(inlist)
        if no_children == 0:
            metalist = []
            for _ in range(no_meta):
                metalist.append(next(inlist))
            root.attrib['metadata'] = metalist
            iter_sum += sum(metalist)
        else:
            for _ in range(no_children):
                child = ET.Element('child')
                next_round = add_node(child, inlist, iter_sum)
                root.append(next_round[0])
                iter_sum = next_round[1]
            metalist = []
            for _ in range(no_meta):
                metalist.append(next(inlist))
            root.attrib['metadata'] = metalist
            iter_sum += sum(metalist)
        return root, iter_sum

    iter_sum = 0
    root, iter_sum = add_node(root, inlist, iter_sum)

    print(iter_sum)
