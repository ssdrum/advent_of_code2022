#!/usr/bin/env python3


MOVES = {(2, 0): (1, 0), (-2, 0): (-1, 0), (0, 2): (0, 1), (0, -2): (0, -1),
         (1, 2): (1, 1), (1, -2): (1, -1), (2, 1): (1, 1), (2, -1): (1, -1),
         (-1, 2): (-1, 1), (-2, 1): (-1, 1), (-2, -1): (-1, -1),
         (-1, -2): (-1, -1), (-2, -1): (-1, -1)}


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


def move_rope(head, tail, dirctn):
    if dirctn == "U":
        head.y += 1
    elif dirctn == "D":
        head.y -= 1
    elif dirctn == "R":
        head.x += 1
    else:
        head.x -= 1

    move_tail(head, tail)


def move_tail(head, tail):
    try:
        # pick right move based on how the head is positioned relative to the
        # tail
        move = MOVES[(head.x - tail.x, head.y - tail.y)]
        (x, y) = move
        # update tail position
        tail.x += x
        tail.y += y
    # only triggered if tail doesn't have to move
    except KeyError:
        return


def main():
    head = Point(0, 0)
    tail = Point(0, 0)
    # store visited points in a set to avoid duplicates
    visited = set()
    visited.add((0, 0))
    
    with open("input9.txt") as f:
        for l in f:
            dirctn, amount = l.split()
            for _ in range(int(amount)):
                move_rope(head, tail, dirctn)
                tail_postn = (tail.x, tail.y)
                visited.add(tail_postn)

    print(len(visited))
    return 0


if __name__ == '__main__':
    main()
