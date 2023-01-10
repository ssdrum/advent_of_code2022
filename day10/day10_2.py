#!/usr/bin/env python3


def draw(cycle, mid):
    cycle %= 40
    if cycle == 0:
        print()
    elif abs(cycle - mid) < 2:
        print("#", end="")
    else:
        print(" ", end="") # space just works better than dots


def main():
    cycle = 1
    mid = 2

    with open("input10.txt") as f:
        for l in f:
            tokens = l.split()
            if tokens[0] == "addx":
                draw(cycle, mid)
                cycle += 1
                draw(cycle, mid)
                cycle += 1
                mid += int(tokens[1])
            else:
                draw(cycle, mid)
                cycle += 1

    return 0


if __name__ == '__main__':
    main()
