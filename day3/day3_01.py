#!/usr/bin/env python3


def main():
    tot = 0
    with open("input3.txt") as f:
        for l in f:
            tot += find_dup_item(l)

    print(tot)


def find_dup_item(items):
    num_items = len(items)
    half1 = {i:None for i in items[:num_items // 2]}
    half2 = {i:None for i in items[num_items // 2:]}
    p = 0 # priority

    # find duplicate item
    for i in half1:
        if i in half2:
            if i.islower():
                # calculate priority
                p = ord(i) - 96
            else:
                p = ord(i) - 38
            return p


if __name__ == '__main__':
    main()
