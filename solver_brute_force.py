#!/usr/bin/env python3

from itertools import permutations, product
import sys
#
#   There's only C_5 = 5 possible parse trees
#
def brute_force_solver(num: str):
    """
        Take a four digit number
    """
    trees = [
        '((({} {} {}) {} {}) {} {})',
        '(({} {} ({} {} {})) {} {})',
        '(({} {} {}) {} ({} {} {}))',
        '({} {} (({} {} {}) {} {}))',
        '({} {} ({} {} ({} {} {})))',
    ]

    nums = list(num)
    ops = ['+', '-', '/', '*']

    #print(len(list(permutations(nums))))
    #print(len(list(product(ops, repeat=3))))

    for tree in trees:
        for (n1, n2, n3, n4) in permutations(nums):
            for (op1, op2, op3) in product(ops, repeat=3):
                expr = tree.format(n1, op1, n2, op2, n3, op3, n4)

                try:
                    res = eval(expr)
                    if res == 10: print (f'{expr} = 10')
                except ZeroDivisionError as e:
                    pass


def main():
    if len(sys.argv) != 2 or len(sys.argv[1]) != 4:
        return

    brute_force_solver(sys.argv[1])

if __name__ == '__main__':
    main()