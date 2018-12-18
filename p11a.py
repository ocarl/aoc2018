def calc_power(x,y,grid):
    last_three = ((x + 10)*y+grid)*(x+10) % 1000
    if last_three < 100:
        power = 0
    else:
        power = (last_three - (last_three % 100))/100
    power -= 5
    return power

assert calc_power(3,5,8) == 4
assert calc_power(122,79, 57) == -5
assert calc_power(217,196, 39) == 0
assert calc_power(101,153, 71) == 4


power_dict = dict()

def calc_tot(x,y,grid):
    tot = 0
    for i in range(x,x+3):
        for j in range(y,y+3):
            tot += calc_power(i,j,grid)
    return tot

assert calc_tot(33,45,18) == 29


for j in range(1, 301):
    for i in range(1, 301):
        power_dict[(i,j)] = calc_tot(i,j,1723)

top_key = 0
max_val = 0
for key in power_dict.keys():
    if power_dict[key] > max_val:
        max_val = power_dict[key]
        top_key = key

print(top_key)
