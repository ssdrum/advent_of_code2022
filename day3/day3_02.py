#!/usr/bin/env python3


def main():
    tot = 0
    with open("input3.txt") as f:
        lines = f.readlines()

    for i in range(0, len(lines), 3):
        tot += calc_prior(lines[i], lines[i + 1], lines[i + 2])

    print(tot)


def calc_prior(l1, l2, l3):
    rucksack1 = {item:None for item in l1}
    rucksack2 = {item:None for item in l2}
    rucksack3 = {item:None for item in l3}
    p = 0 # priority

    # find common item
    for item in rucksack1:
        if item in rucksack2 and item in rucksack3:
            # calculate priority
            if item.islower():
                p = ord(item) - 96
            else:
                p = ord(item) - 38
            return p


if __name__ == '__main__':
    main()
