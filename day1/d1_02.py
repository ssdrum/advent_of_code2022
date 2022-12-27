#!/usr/bin/env python3


def main():
    elves = []

    f = open("input1.txt", "r")
    lines = f.readlines()
    num_lines = len(lines)

    i = 0
    while i < num_lines:
        curr_elf = 0
        j = i
        while j < num_lines and lines[j] != "\n":
            curr_elf += int(lines[j])
            j += 1
        elves.append(curr_elf)
        i = j + 1

    f.close()

    elves = sorted(elves)
    print(elves[-1] + elves[-2] + elves[-3])


if __name__ == "__main__":
    main()
