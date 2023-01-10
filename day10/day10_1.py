#!/usr/bin/env python3


CHECKS = {20: True, 60: True, 100: True, 140: True, 180: True, 220: True}


# returns cycle increased by 1 and updated sygnal sum
def incr_cycle(cycle, val, sygn_sum):
    cycle += 1
    if cycle in CHECKS:
        sygn_sum += cycle * val
    return (cycle, sygn_sum)


def main():
    cycle = 0
    val = 1
    sygn_sum = 0

    with open("input10.txt") as f:
        for l in f:
            tokens = l.split()
            if tokens[0] == "addx":
                (cycle, sygn_sum) = incr_cycle(cycle, val, sygn_sum)
                (cycle, sygn_sum) = incr_cycle(cycle, val, sygn_sum)
                val += int(tokens[1])
            else:
                (cycle, sygn_sum) = incr_cycle(cycle, val, sygn_sum)


    print(sygn_sum)
    return 0


if __name__ == '__main__':
    main()
