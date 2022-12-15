f = open("inputs/d14", "r")


class Fluid:
    rocks = []
    source = (500, 0)
    sand = []
    directions = [(0, 1), (-1, 1), (1, 1)]

    def draw(self):
        for y in range(0, 170):
            for x in range(460, 590):
                if (x, y) in self.rocks:
                    print("#", end="")
                elif (x, y) in self.sand:
                    print("o", end="")
                elif (x, y) == self.source:
                    print("+", end="")
                else:
                    print(".", end="")

            print("")

    def get_route(self, pos):
        for dir in self.directions:
            check_pos = (pos[0] + dir[0], pos[1] + dir[1])
            if (
                check_pos not in self.sand
                and check_pos not in self.rocks
                and check_pos[1] < self.floor
            ):
                return check_pos
        return False

    def gen_sand(self):
        pos = self.source
        blocked = False
        max_iter = 500
        i = 0
        while not blocked:
            route = self.get_route(pos)
            if not route:
                blocked = True
            else:
                pos = route
            i += 1
            if i > max_iter:
                return False
        if pos[1] == 0:
            return False
        self.sand.append(pos)
        return True

    def gen_rocks(self, ranges, i):
        start = tuple(map(lambda x: int(x), ranges[i].strip().split(",")))
        end = tuple(map(lambda x: int(x), ranges[i + 1].strip().split(",")))

        if start[0] != end[0]:
            if start[0] < end[0]:
                for y in range(start[0], end[0] + 1):
                    if (y, start[1]) not in self.rocks:
                        self.rocks.append((y, start[1]))
            if start[0] > end[0]:
                for y in range(end[0], start[0] + 1):
                    if (y, start[1]) not in self.rocks:
                        self.rocks.append((y, start[1]))
        if start[1] != end[1]:
            if start[1] < end[1]:
                for x in range(start[1], end[1] + 1):
                    if (start[0], x) not in self.rocks:
                        self.rocks.append((start[0], x))
            if start[1] > end[1]:
                for x in range(end[1], start[1] + 1):
                    if (start[0], x) not in self.rocks:
                        self.rocks.append((start[0], x))

    def parse(self, input):
        for line in input:
            ranges = line.split(" -> ")
            for i in range(len(ranges)):
                if i < len(ranges) - 1:
                    self.gen_rocks(ranges, i)
        self.floor = max(self.rocks, key=lambda y: y[1])[1] + 2


fluid = Fluid()
fluid.parse(f.readlines())
count = 0
while True:
    if not fluid.gen_sand():
        count += 1
        print(count)
        break
    if count % 100 == 0:
        fluid.draw()
        print("---------------------")
    count += 1
# fluid.draw()
