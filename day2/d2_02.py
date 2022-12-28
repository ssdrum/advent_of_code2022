#!/usr/bin/env python3


def main():
    tot_score = 0

    with open("input2.txt") as f:
        for l in f:
            [opp, res] = l.split()
            tot_score += calc_score(opp, res)

    print(tot_score)


def calc_score(opp, res):
    shapes = {"X": 1, "Y": 2, "Z": 3}
    opp_int = ord(opp) - 65  # change opponent's choice into an int between 0 and 2
    score = 0

    if res == "X":
        score = shapes[chr((opp_int - 1) % 3 + 88)]
    elif res == "Y":
        score = shapes[chr(opp_int + 88)] + 3
    else:
        score = shapes[chr((opp_int + 1) % 3 + 88)] + 6

    return  score


if __name__ == '__main__':
    main()
