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

    cols = [list(l) for l in zip(*rows)] # transpose of rows
    # calculate length and height of grid
    h = len(lines)
    l = len(trees) // h

    # find central trees positions 
    centr_trees = []
    for i in range(len(trees[l:len(trees) - l])):
        if i % l != 0 and (i + 1) % l != 0:
            centr_trees.append(i + l)

    max_score = 0
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

        # find view distances on all four directions
        curr = trees[pos]
        distances = []
        distances.append(find_first_cover(curr, above[::-1]))
        distances.append(find_first_cover(curr, left[::-1]))
        distances.append(find_first_cover(curr, right))
        distances.append(find_first_cover(curr, below))

        # calculate scenic score
        score = mult_list(distances)
        if score > max_score:
            max_score = score

    print(max_score)


# finds number of trees visible from tree in line
def find_first_cover(tree, line):
    i = 0
    while line[i] < tree and i < len(line) - 1:
        i += 1
    return i + 1


def mult_list(nums):
    prod = 1
    for x in nums:
        prod *= x
    return prod


if __name__ == '__main__':
    main()
