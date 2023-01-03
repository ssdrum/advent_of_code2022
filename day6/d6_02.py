#!/usr/bin/env python3


def main():
    with open("input6.txt") as f:
        data = f.readline()


    win_size = 14
    i = 0
    while len(set(data[i:i + win_size])) != win_size:
        i += 1

    print(i + win_size)

    return 0


if __name__ == '__main__':
    main()
