#!/usr/bin/env python3


MOVES = {(2, 0): (1, 0), (-2, 0): (-1, 0), (0, 2): (0, 1), (0, -2): (0, -1),
         (1, 2): (1, 1), (1, -2): (1, -1), (2, 1): (1, 1), (2, -1): (1, -1),
         (-1, 2): (-1, 1), (-2, 1): (-1, 1), (-2, -1): (-1, -1),
         (-1, -2): (-1, -1), (-2, -1): (-1, -1), (2, 2): (1, 1),
         (-2, -2): (-1, -1), (2, -2): (1, -1), (-2, 2): (-1, 1)}


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


def move_rope(head, points, dirctn):
    if dirctn == "U":
        head.y += 1
    elif dirctn == "D":
        head.y -= 1
    elif dirctn == "R":
        head.x += 1
    else:
        head.x -= 1

    move_points(head, points)


# Moves all points of the rope one by one
def move_points(head, points):
    prev = head
    for p in points:
        try:
            curr = p
            move = MOVES[(prev.x - curr.x, prev.y - curr.y)]
            (x, y) = move
            curr.x += x
            curr.y += y
            prev = curr
        except KeyError:
            return


def main():
    head = Point(0, 0)
    p1 = Point(0, 0)
    p2 = Point(0, 0)
    p3 = Point(0, 0)
    p4 = Point(0, 0)
    p5 = Point(0, 0)
    p6 = Point(0, 0)
    p7 = Point(0, 0)
    p8 = Point(0, 0)
    p9 = Point(0, 0)

    visited = set()
    visited.add((0, 0))
    points = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
    # store visited points in a set to avoid duplicates
    
    with open("input9.txt") as f:
        for l in f:
            dirctn, amount = l.split()
            for _ in range(int(amount)):
                move_rope(head, points, dirctn)
                tail = points[8]
                visited.add((tail.x, tail.y))


    print(len(visited))
    return 0


if __name__ == '__main__':
    main()
