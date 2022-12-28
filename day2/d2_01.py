#!/usr/bin/env python3


def main():
    tot_score = 0

    with open("input2.txt") as f:
        for l in f:
            tot_score += calc_score("".join(l.split()))

    print(tot_score)


def calc_score(round):
    shapes = {"X": 1, "Y": 2, "Z": 3}
    combs = {"AX": 3, "AY": 6, "AZ": 0, "BX": 0, "BY": 3, "BZ": 6, "CX": 6, "CY": 0, "CZ": 3}

    return combs[round] + shapes[round[1]]


if __name__ == '__main__':
    main()
