#!/usr/bin/env python3

global rows
global cols
rows = []
cols = []

def main():



    with open("input8.txt") as f:
        lines = f.readlines()

    for l in lines:
        rows.append([int(n) for n in l.rstrip()])
    cols = [list(i) for i in zip(*rows)]
    
    for r in rows:
        print(r)

    h = len(rows)
    l = len(cols)

    vis = 0
    for i in range(1, h - 1):
        for j in range(1, l - 1):
            print(f"{i}, {j}, {rows[i][j]}")

    print(vis)


def is_vis(tree, row, col):
    # check row
    for i, t in enumerate(rows[row]):
        print(i, t)














if __name__ == '__main__':
    main()
