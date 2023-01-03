#!/usr/bin/env python3


def main():
    stacks = [
        ["Z", "P", "M", "H", "R"],
        ["P", "C", "J", "B"],
        ["S", "N", "H", "G", "L", "C", "D"],
        ["F", "T", "M", "D", "Q", "S", "R", "L"], 
        ["F", "S", "P", "Q", "B", "T", "Z", "M"], 
        ["T", "F", "S", "Z", "B", "G"], 
        ["N", "R", "V"],
        ["P", "G", "L", "T", "D", "V", "C", "M"],
        ["W", "Q", "N", "J", "F", "M", "L"]
    ]

    with open("input5.txt") as f:
        for l in f:
            tokens = l.split()
            r = int(tokens[1]) # range
            s1 = stacks[int(tokens[3]) - 1]
            s2 = stacks[int(tokens[5]) - 1]

            for i in range(r):
                s2.append(s1.pop())

    for s in stacks:
        print(s[-1], end="")

    return 0


if __name__ == '__main__':
    main()
