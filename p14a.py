def calc_next_10(input):
    recipies = [3, 7]
    i1 = 0
    i2 = 1
    while len(recipies) < (input + 10):
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
    return ''.join([str(x) for x in recipies])[input:input + 10]

assert calc_next_10(9) == '5158916779'
assert calc_next_10(5) == '0124515891'
assert calc_next_10(18) == '9251071085'
assert calc_next_10(2018) == '5941429882'

print(calc_next_10(637061))
