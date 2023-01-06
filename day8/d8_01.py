#!/usr/bin/env python3


def main():
    trees = [] # all trees
    rows = [] # all rows
    cols = [] # all columns

    with open("input8.txt") as f:
        lines = f.readlines()
        for line in lines:
            rows.append([int(n) for n in line.rstrip()])
            for tree in line.rstrip():
                trees.append(int(tree))

    cols = [list(l) for l in zip(*rows)] # transpose of columns
    # calculate length and height of grid
    h = len(lines)
    l = len(trees) // h

    # find central trees positions 
    centr_trees = []
    for i, tree in enumerate(trees[l:len(trees) - l]):
        if i % l != 0 and (i + 1) % l != 0:
            centr_trees.append(i + l)

    solution = 2 * l + 2 * (h - 2) # initialise solution counting outer trees
    for pos in centr_trees:
        # find trees on the left and on the right of the current central tree
        row_num = pos // l
        row = rows[row_num]
        left = row[:pos % l]
        right = row[pos % l + 1:]
        # find trees above and below of the current central tree
        col_num = pos % l
        col = cols[col_num]
        above = col[:pos // l]
        below = col[pos // l + 1:]

        # find all visible trees
        curr = trees[pos]
        if all(t < curr for t in left) or all(t < curr for t in right) \
        or all(t < curr for t in above) or all(t < curr for t in below):
            solution += 1

    print(solution)


if __name__ == '__main__':
    main()
