#!/usr/bin/env python3


class Monkey():
    def __init__(self):
        self.items = []
        self.inspected = 0
        self.oper = ()
        self.test = None
        self.throw1 = None
        self.throw2 = None


def store_monkeys(lines):
    monkeys = []
    num_monkeys = (len(lines) - 6) // 7 + 1

    for i in range(num_monkeys):
        m = Monkey()
        # store items as a list of integers
        m.items = [int(i.removesuffix(",")) for i in lines[i * 7 + 1].split()[2:]]
        # store operation and number as a touple
        oper = lines[i * 7 + 2].split()[-2]
        try:
            n = int(lines[i * 7 + 2].split()[-1])
        except ValueError: # only triggers if item gets squared
            n = None
        m.oper = (oper, n)
        # test, throw1 and throw2 are three integers. If test divides an item
        # evenly, item is passed to the monkey at index throw1. Otherwise, item
        #is passed to the monkey at index throw2
        m.test = int(lines[i * 7 + 3].split()[-1]) 
        m.throw1 = int(lines[i * 7 + 4].split()[-1])
        m.throw2 = int(lines[i * 7 + 5].split()[-1])

        monkeys.append(m)
        
    return monkeys


def find_big_int(monkeys):
    big_int = 1
    for m in monkeys:
        big_int *= m.test

    return big_int


def main():
    with open("input11.txt") as f:
        lines = f.readlines()

    monkeys = store_monkeys(lines)
    big_int = find_big_int(monkeys)

    for _ in range(10000):
        for m in monkeys:
            for item in m.items: # loop through monkey's items
                m.inspected += 1
                n = m.oper[1] # either * or +
                if m.oper[0] == "*":
                    if m.oper[1] == None: # item is squared
                        item *= item
                    else: # item is multiplied by n
                        item *= n 
                else: # item is summed with n
                    item += n
                
                item %= big_int
                rem = item % m.test # test
                if rem == 0:
                    monkeys[m.throw1].items.append(item) # true test
                else:
                    monkeys[m.throw2].items.append(item) # false test

            m.items = [] # empty items

        inspections = sorted(m.inspected for m in monkeys)
        print(inspections[-1] * inspections[-2])



if __name__ == '__main__':
    main()
