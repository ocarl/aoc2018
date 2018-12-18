def calc_next_10(input):
    recipies = [3, 7]
    i1 = 0
    i2 = 1
    retstr = ''
    count = -1
    while retstr.find(input) == -1:
        count += 1
        sr = sum([recipies[i1], recipies[i2]])
        if sr > 9:
            recipies.append(int(str(sr)[0]))
            recipies.append(int(str(sr)[1]))
        else:
            recipies.append(int(str(sr)[0]))
        i1 += (1 + recipies[i1])
        i1 = i1 % len(recipies)
        i2 += (1 + recipies[i2])
        i2 = i2 % len(recipies)
        retstr = ''.join([str(x) for x in recipies])
    return count

assert calc_next_10('51589') == 9
assert calc_next_10('01245') == 5
assert calc_next_10('92510') == 18
assert calc_next_10('59414') == 2018

print(calc_next_10('637061'))
