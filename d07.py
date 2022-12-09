f = open("inputs/d07", "r")


def get_dir_by_path():
    return root_dir.get_dir()


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name):
        self.name = name
        self.subdirs = []
        self.files = []

    def add_dir(self, name):
        cur_path_cpy = current_path.copy()
        cur_path_cpy.append(name)
        new_dir = Directory(cur_path_cpy)
        self.subdirs.append(new_dir)

    def add_file(self, name, size):
        for file in self.files:
            if file.name == name:
                return
        new_file = File(name, size)
        self.files.append(new_file)

    def get_dir(self):
        if current_path == self.name:
            return self
        else:
            for dir in self.subdirs:
                if dir.get_dir() != None:
                    return dir.get_dir()

    def get_dir_size(self):
        total_size = 0
        for f in self.files:
            total_size += f.size
        for d in self.subdirs:
            total_size += d.get_dir_size()
        return total_size


root_dir = Directory(["/"])
list_mode = False

current_path = ["/"]

for line in f.readlines():
    line = line.strip()
    if list_mode == True:
        if line.startswith("$"):
            list_mode = False
        else:
            cur_dir = get_dir_by_path()
            if line.startswith("dir"):
                dir_line = line.split(" ")
                cur_dir.add_dir(dir_line[1])
            elif line[0].isdigit():
                file_line = line.split(" ")
                cur_dir.add_file(file_line[1], int(file_line[0]))
    if line.startswith("$ cd"):
        dir_line = line.split("cd ")
        if dir_line[1] == "/":
            continue
        elif dir_line[1] == "..":
            current_path.pop()
        else:
            current_path.append(dir_line[1])
    elif line == "$ ls":
        list_mode = True


total_disk = 70000000
used = total_disk - root_dir.get_dir_size()
wanted = 30000000 - used


def scan_dir(dir, smallest):
    curdir_size = dir.get_dir_size()
    if curdir_size > wanted and (
        smallest == None or curdir_size < smallest.get_dir_size()
    ):
        smallest = dir

    for d in dir.subdirs:
        sd_smallest = scan_dir(d, smallest)
        if sd_smallest != None:
            if sd_smallest.get_dir_size() < smallest.get_dir_size():
                smallest = sd_smallest

    return smallest


print(scan_dir(root_dir, None).get_dir_size())
