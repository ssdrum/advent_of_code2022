#!/usr/bin/env python3


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


def gen_tree():
    root = Directory("/")
    curr = root

    with open("input7.txt") as f:
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


def calc_size(root):
    tot_size = 0
    tot_size = root.size
    for c in root.children:
        tot_size += calc_size(c)
    return tot_size


def post_traversal(root, dirs={}):
    if root is not None:
        for c in root.children:
            if isinstance(c, Directory):
                dirs[c.name] = calc_size(c)
                post_traversal(c, dirs)
    return dirs
        

def main():
    root = gen_tree()
    dirs = post_traversal(root)

    solution = 0
    for k,v in dirs.items():
        if v <= 100000:
            solution += v
    print(solution)


if __name__ == '__main__':
    main()
