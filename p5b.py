import sys

def destroyer(instring: str, inchar: str):
    inlist = list(instring)
    for i, char in enumerate(inlist):
        if char == inchar:
            inlist.pop(i)
            continue
        if char == inchar.swapcase():
            inlist.pop(i)
            continue
        try:
            if char == inlist[i + 1].swapcase():
                inlist.pop(i)
                inlist.pop(i)
        except IndexError:
            pass
    outstring = ''.join(inlist)
    if outstring != instring:
        outstring = destroyer(outstring, inchar)
    return outstring


def shorten(instring: str):
    results = dict()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        results[char] = len(destroyer(instring, char))
    return results


if __name__ == '__main__':
    sys.setrecursionlimit(3000)
    with open('5.txt') as f:
        test_input = f.read()
        # test_input = 'dabAcCaCBAcCcaDA'
        char_dict = shorten(test_input)
        print(sorted(char_dict.items(), key=lambda kv: kv[1]))
