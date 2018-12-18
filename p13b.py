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
        self.opponents = []
        Cart.carts.append(self)

    def __repr__(self):
        return f'{self.x}, {self.y}'

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
            if self.dir in ['w', 'e']:
                self.dir = turn_left[self.dir]
            elif self.dir in ['s', 'n']:
                self.dir = turn_right[self.dir]
        if instruction == '\\':
            if self.dir in ['e', 'w']:
                self.dir = turn_right[self.dir]
            elif self.dir in ['n', 's']:
                self.dir = turn_left[self.dir]


test_input = r'''/>-<\  
|   |  
| /<+-\
| | | v
\>+</ |
  |   ^
  \<->/'''

#test_input = r'''/->-\
#|   |  /----\
#| /-+--+-\  v
#^ | |  | v  |
#\-+-/  \-+--/
#  \--->--/   '''

dir_to_abs = {'v': 's', '<': 'w', '^': 'n', '>': 'e'}

ins_dict = dict()

with open('13.txt') as f:
    test_input = f.read()
    for j, line in enumerate(test_input.split('\n')):
        for i, char in enumerate(line):
            ins_dict[(i, j)] = char

    for j, line in enumerate(test_input.split('\n')):
        for i, char in enumerate(line):
            if char in ['v', '<', '^', '>']:
                Cart(i, j, dir_to_abs[char], ins_dict)

    for i, cart in enumerate(Cart.carts):
        carts_list = Cart.carts.copy()
        carts_list.pop(i)
        cart.opponents = carts_list

    while len(Cart.carts) > 1:
        cart_list = Cart.carts
        for i, cart in enumerate(cart_list):
            cart.tick()
            # detect collisions
            for j, other_cart in enumerate(cart.opponents):
                if (other_cart.x, other_cart.y) == (cart.x, cart.y):
                    cart.opponents.pop(j)
                    Cart.carts = cart.opponents
                    for i, cart in enumerate(Cart.carts):
                        carts_list = Cart.carts.copy()
                        carts_list.pop(i)
                        cart.opponents = carts_list
                    break

    print((Cart.carts[0].x, Cart.carts[0].y, Cart.carts[0].dir))
