#!/usr/bin/env python3


def main():
    tot = 0
    with open("input4.txt") as f:
        for l in f:
            [r1, r2] = l.split(",")
            tot += is_contained(r1, r2)
    print(tot)


def is_contained(r1, r2):
    [r1_min, r1_max] = map(int, r1.split("-"))
    [r2_min, r2_max] = map(int, r2.split("-"))
    r1_set = set(range(r1_min, r1_max + 1))
    r2_set = set(range(r2_min, r2_max + 1))

    # check if intersection is equal to size of smallest set
    if len(r1_set & r2_set) == len(min(r1_set, r2_set)):
        return 1
    return 0


if __name__ == '__main__':
    main()
