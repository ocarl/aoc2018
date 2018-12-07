test_input = 'dabAcCaCBAcCcaDA'


def destroyer(instring: str):
    outstring = ''
    inlist = list(instring)
    for i, char in enumerate(inlist):
        try:
            if char == inlist[i+1].swapcase():
                inlist.pop(i)
                inlist.pop(i)
        except IndexError:
            pass
    outstring = ''.join(inlist)
    if outstring != instring:
        outstring = destroyer(outstring)
    return outstring


assert destroyer(test_input) == 'dabCBAcaDA'


if __name__ == '__main__':

    with open('5.txt') as f:
        instring = f.read()
        print(len(destroyer(instring)))