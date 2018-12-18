from itertools import cycle

turn_left = {'n': 'w',
             'w': 's',
             's': 'e',
             'e': 'n'}

turn_right = {'n': 'e',
              'w': 'n',
              's': 'w',
              'e': 's'}

tick_dict = {'n': (0, -1),
             'w': (-1, 0),
             's': (0, 1),
             'e': (1, 0)}


class Cart:
    carts = []

    def __init__(self, x, y, dir, ins_dict):
        self.turn_order = cycle([self.left, self.straight, self.right])
        self.ins_dict = ins_dict
        self.x = x
        self.y = y
        self.dir = dir
        Cart.carts.append(self)

    def straight(self):
        pass

    def right(self):
        self.dir = turn_right[self.dir]

    def left(self):
        self.dir = turn_left[self.dir]

    def tick(self):
        step = tick_dict[self.dir]
        self.x += step[0]
        self.y += step[1]
        self.resolve_instruction(ins_dict[(self.x, self.y)])

    def resolve_instruction(self, instruction):
        if instruction == '+':
            next(self.turn_order)()
        if instruction == '/':
            if self.dir in ['e', 's']:
                self.dir = turn_left[self.dir]
            if self.dir in ['n', 'w']:
                self.dir = turn_right[self.dir]
        if instruction == '\\':
            if self.dir in ['e', 's']:
                self.dir = turn_right[self.dir]
            if self.dir in ['n', 'w']:
                self.dir = turn_left[self.dir]


test_input = '''/->-\        
|   |  /----\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/   '''

dir_to_abs = {'v': 's', '<': 'w', '^': 'n', '>': 'e'}

ins_dict = dict()

for j, line in enumerate(test_input.split('\n')):
    for i, char in enumerate(line):
        ins_dict[(i, j)] = char

for j, line in enumerate(test_input.split('\n')):
    for i, char in enumerate(line):
        if char in ['v', '<', '^', '>']:
            Cart(i, j, dir_to_abs[char], ins_dict)

crashed = False

while not crashed:
    positions = []
    for cart in Cart.carts:
        cart.tick()
        positions.append((cart.x, cart.y))
    for cart in Cart.carts:
        print((cart.x, cart.y))
        if (cart.x, cart.y) in positions:
            print((cart.x, cart.y))
            crashed = True
