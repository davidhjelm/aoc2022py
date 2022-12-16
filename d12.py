import copy


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


f = open("inputs/d12", "r")

input = f.readlines()


class Path:
    def __init__(self, input):
        self.grid, self.pos, self.end = self.get_grid(input)
        self.root = copy.deepcopy(self.pos)
        self.shortest = None

    def get_options(self):
        # up, right, down, left
        options = [
            (self.pos[0] - 1, self.pos[1]),
            (self.pos[0], self.pos[1] + 1),
            (self.pos[0] + 1, self.pos[1]),
            (self.pos[0], self.pos[1] - 1),
        ]

        routes = []

        for option in options:
            if (option[0] >= 0 and option[1] >= 0) and (
                option[0] < len(self.grid) and option[1] < len(self.grid[0])
            ):
                op_letter = self.grid[option[0]][option[1]]
                cur_letter = self.grid[self.pos[0]][self.pos[1]]

                if (
                    (cur_letter == "S" and op_letter == "a")
                    or (op_letter == "E" and cur_letter == "z")
                    or cur_letter == op_letter
                    or ord(cur_letter) + 1 == ord(op_letter)
                    or (ord(cur_letter) > ord(op_letter) and op_letter >= "a")
                ):
                    routes.append(option)

        return routes

    def dfs(self, root):
        queue = [root]
        visited = [root]
        parents = {}

        while len(queue) > 0:
            self.pos = queue.pop(0)
            if self.grid[self.pos[0]][self.pos[1]] == "E":
                path = []
                p = parents[self.pos]
                while True:
                    path.append(p)
                    if p in parents:
                        p = parents[p]
                    else:
                        break
                self.shortest = path
            options = self.get_options()

            for option in options:
                if option not in visited:
                    queue.append(option)
                    visited.append(option)
                    parents[option] = self.pos

    def get_grid(self, input):
        grid = []
        start = ()
        end = ()

        for iy, line in enumerate(input):
            grid.append([])
            for ix, x in enumerate(line.strip()):
                grid[iy].append(x)
                if x == "S":
                    start = (iy, ix)
                elif x == "E":
                    end = (iy, ix)

        return grid, start, end

    def draw(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if (y, x) in self.shortest:
                    print(f"{bcolors.OKGREEN}{self.grid[y][x]}", end="")
                else:
                    print(f"{bcolors.ENDC}{self.grid[y][x]}", end="")
            print("  ")
        print("")


path = Path(input)
path.dfs(path.root)

print(len(path.shortest))

path.draw()
