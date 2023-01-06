#!/usr/bin/env python3


DISK_SIZE = 70000000 # tot disk size

class Node():
    def __init__(self, name, parent, size):
        self.name = name
        self.parent = parent
        self.size = size
        self.children = []


class Directory(Node):
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.size = 0
        self.children = []

    def get_child(self, name):
        for c in self.children:
            if c.name == name:
                return c
    

class File(Node):
    pass


# builds the tree
def gen_tree():
    root = Directory("/")
    curr = root

    with open("input7.txt") as f:
        l = f.readline() # skip first line
        l = f.readline()
        while l:
            tokens = l.split()
            if tokens[0] == "$": # command
                command = tokens[1]
                if command == "cd":
                    dir_name = tokens[2]
                    if dir_name == "..":
                        curr = curr.parent # up one level
                    else:
                        curr = curr.get_child(dir_name) # down one level
            else:
                name = tokens[1]
                if tokens[0] == "dir": # directory
                    curr.children.append(Directory(name, curr)) # create directory
                else:
                    size = int(tokens[0]) # file
                    curr.children.append(File(name, curr, size)) # add file to directory
            l = f.readline()

    return root


# calculates size of subtree with root = root
def calc_size(root):
    tot_size = root.size
    for c in root.children:
        tot_size += calc_size(c)
    return tot_size


# traverses the tree in post-traversal and generates a list with the sizes of
# all the directories
def get_dirs_sizes(root, dirs_sizes=[]):
    if root is not None:
        for c in root.children:
            if isinstance(c, Directory):
                dirs_sizes.append(calc_size(c))
                get_dirs_sizes(c, dirs_sizes)
    return dirs_sizes
        

def main():
    root = gen_tree()
    dirs_sizes = get_dirs_sizes(root)
    used = calc_size(root) # used space
    free = DISK_SIZE - used # free space

    solution = used
    for s in dirs_sizes:
        if s + free >= 30000000 and s < solution:
            solution = s

    print(solution)


if __name__ == '__main__':
    main()
