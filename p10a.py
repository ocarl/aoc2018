import re


test_input = '''position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>'''

class Point:
    points = []

    def __init__(self, x, y, vx, vy):
        self.position = [x, y]
        self.velocity = [vx, vy]
        Point.points.append(self)

    def tick(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

    def tock(self):
        self.position[0] -= self.velocity[0]
        self.position[1] -= self.velocity[1]

    @staticmethod
    def calc_min_x():
        min_x = 9999999
        for pt in Point.points:
            if pt.position[0]<min_x:
                min_x = pt.position[0]
        return min_x

    @staticmethod
    def calc_min_y():
        min_y = 9999999
        for pt in Point.points:
            if pt.position[1]<min_y:
                min_y = pt.position[1]
        return min_y

    @staticmethod
    def calc_max_x():
        max_x = -9999999
        for pt in Point.points:
            if pt.position[0]>max_x:
                max_x = pt.position[0]
        return max_x

    @staticmethod
    def calc_max_y():
        max_y = -9999999
        for pt in Point.points:
            if pt.position[1]>max_y:
                max_y = pt.position[1]
        return max_y




with open('10.txt') as f:
    test_input = f.read()
    for line in test_input.split('\n'):
        x,y,vx,vy = re.findall('[-]?\d+', line)
        Point(int(x),int(y),int(vx),int(vy))


max_x = 999999
min_x = -999999
max_y = 999999
min_y = -999999

dist_x = max_x - min_x
dist_y = max_y - min_y

prev_dist_x = dist_x + 1
prev_dist_y = dist_y + 1

secs = 0
while prev_dist_x > dist_x and prev_dist_y > dist_y:
    secs += 1
    prev_dist_x = dist_x
    prev_dist_y = dist_y
    for pt in Point.points:
        pt.tick()

    min_x = Point.calc_min_x()
    min_y = Point.calc_min_y()
    max_x = Point.calc_max_x()
    max_y = Point.calc_max_y()
    dist_x = max_x - min_x
    dist_y = max_y - min_y





for pt in Point.points:
    pt.tock()

print('found')

min_x = Point.calc_min_x()
min_y = Point.calc_min_y()
max_x = Point.calc_max_x()
max_y = Point.calc_max_y()

outstring = ''

for j in range(min_y, max_y+1):
    for i in range(min_x, max_x+1):
        outstring += '.'
        for pt in Point.points:
            if pt.position == [i, j]:
                outstring = outstring[:-1] + '#'
    outstring += '\n'

print(outstring+f'\n{secs-1}')








