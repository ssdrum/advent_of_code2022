#!/usr/bin/env python3


def main():
    f = open("input1.txt", "r")
    lines = f.readlines()
    num_lines = len(lines)

    max_elf = 0
    i = 0
    while i < num_lines:
        curr_elf = 0
        j = i
        while j < num_lines and lines[j] != "\n":
            curr_elf += int(lines[j])
            j += 1
        if max_elf < curr_elf:
            max_elf = curr_elf
        i = j + 1

    f.close()
    print(max_elf)


if __name__ == "__main__":
    main()
