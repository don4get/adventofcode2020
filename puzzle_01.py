# -*- coding: utf-8 -*-
"""
puzzle_01.py module.

--- Day 1: Report Repair --- After saving Christmas five years in a row,
you've decided to take a vacation at a nice resort on a tropical island. Surely,
Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins
used there have a little picture of a starfish; the locals just call them stars. None
of the currency exchanges seem to have heard of them, but somehow, you'll need to
find fifty of these coins by the time you arrive so you can pay the deposit on your
room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in
the Advent calendar; the second puzzle is unlocked when you complete the first. Each
puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (
your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then
multiply those two numbers together.

For example, suppose your expense report contained the following:

1721 979 366 299 675 1456 In this list, the two entries that sum to 2020 are 1721 and
299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is
514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020;
what do you get if you multiply them together? """

from time import time

import pandas as pd

_tstart_stack = []


def tic():
    _tstart_stack.append(time())


def toc(fmt="Elapsed: %s seconds."):
    elapsed_time = time() - _tstart_stack.pop()
    print(fmt % (elapsed_time))
    return elapsed_time


def main(two_arguments = True):
    data = pd.read_csv("puzzle_01_input.csv", header=None).T
    values = data.values[0]
    found = False
    tic()
    if two_arguments:
        result = [(v1, v2, v1 * v2)
                  for v1 in values
                  for v2 in values
                  if v1 + v2 == 2020]
        v1, v2, product = result[0]
        print(f"Result with list comprehension: "
              f"{v1} * {v2} = {product}")
    else:
        result = [(v1, v2, v3, v1 * v2 * v3)
                  for v1 in values
                  for v2 in values
                  for v3 in values
                  if v1 + v2 + v3 == 2020]
        v1, v2, v3, product = result[0]
        print(f"Result with list comprehension: "
              f"{v1} * {v2} * {v3} = {product}")

    toc()
    tic()
    for v1 in values:
        for v2 in values:
            if two_arguments:
                sum = v1 + v2
                if sum == 2020:
                    print(f"Result with 2 for loops: "
                          f"{v1} * {v2} = {v1 * v2}")
                    found = True
                    break
            else:
                for v3 in values:
                    sum = v1 + v2 + v3
                    if sum == 2020:
                        print(f"Result with 3 for loops: "
                              f"{v1} * {v2} * {v3} = {v1 * v2 * v3}")
                        found = True
                        break
            if found:
                break
        if found:
            break
    toc()


if __name__ == "__main__":
    main(two_arguments=False)
