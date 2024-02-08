#!/usr/bin/env python3

from itertools import permutations, product
import sys

def brute_force_solver(num: str) -> list:
    """
        Takes a four digit number as a string, and checks for solutions to the train game and returns a list
        of expressions that will evaluate to ten using the four digits and only arithmetic operations

        How it works:
        - There are 5 possible expression trees (the third Catalan number)
        - 4^3 possible ways of choosing binary operations (ignoring the fact * and + are commutative)
        - 4! permutations of the four numbers

        Which is 7680 expressions to check, so a computer can bruteforce it.
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

    solns = []

    for tree in trees:
        for (n1, n2, n3, n4) in permutations(nums):
            for (op1, op2, op3) in product(ops, repeat=3):
                expr = tree.format(n1, op1, n2, op2, n3, op3, n4)
                try:
                    res = eval(expr)
                    if res == 10:
                        print (f'{expr} = 10')
                        solns.append(expr)
                except ZeroDivisionError as e:
                    pass

    if not solns:
        print(f"{sys.argv[0]}: can't solve this with only arithmetic operations")

    return solns



def main():

    if len(sys.argv) != 2 or not (len(sys.argv[1]) == 4 and sys.argv[1].isnumeric()):
        print(f'{sys.argv[0]}: input must be a four digit number')
        return

    brute_force_solver(sys.argv[1])

if __name__ == '__main__':
    main()