import sys
from math import prod
from itertools import combinations


entries = [int(n) for n in sys.stdin]


def solve(n):
    return next(prod(v) for v in combinations(entries, n) if sum(v) == 2020)


print("part 1:", solve(2))
print("part 2:", solve(3))
