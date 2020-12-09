import sys
from collections import deque
from itertools import islice, combinations


def find_invalid(ns, size):
    window = deque(islice(ns, size), size)

    for i, n in enumerate(ns, size):
        if not has_sum(window, n):
            return n
        window.append(n)


def has_sum(window, n):
    for a, b in combinations(window, 2):
        if a + b == n:
            return True
    return False


def find_contiguous(ns, target):
     for i in range(len(ns)-1):
         for j in range(i+1, len(ns)):
             window = ns[i:j]
             s = sum(window)
             if s == target:
                 return window
             elif s > target:
                 break
     raise ValueError("no range found")


def main():
    window_size = int(sys.argv[1])
    inputs = [int(x.strip()) for x in sys.stdin]
    n = find_invalid(iter(inputs), window_size)
    print(n)

    sum_range = find_contiguous(inputs, n)
    print(sum_range)
    print(min(sum_range) + max(sum_range))


if __name__ == '__main__':
    main()

