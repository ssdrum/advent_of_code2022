#!/usr/bin/env python3


def main():
    with open("input6.txt") as f:
        data = f.readline()

    i = 0
    while len(set(data[i:i + 4])) != 4:
        i += 1

    print(i + 4)

    return 0


if __name__ == '__main__':
    main()
