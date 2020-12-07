import math
import sys


SLOPES = [
    (1, 1),
    (3, 1), 
    (5, 1),
    (7, 1),
    (1, 2),
]


class Map:

    def __init__(self):
        self.rows = []
        self.width = None

    def add_row(self, row):
        if self.width is not None and len(row) != self.width:
            raise ValueError(f"unexpected row width, wanted {self.width}, got {len(row)}")
        self.rows.append(row)
        self.width = len(row)

    def is_tree(self, row, col):
        return self.rows[row][col % self.width] == "#"

    def height(self):
        return len(self.rows)


def count_trees(m, slope):
    right, down = slope
    row, col = 0, 0
    tree_count = 0
    while row < m.height():
        if m.is_tree(row, col):
            tree_count += 1
        col += right
        row += down
    return tree_count


def main():
    m = Map()
    for line in sys.stdin:
        m.add_row(line.strip())

    print(math.prod(count_trees(m, slope) for slope in SLOPES))


if __name__ == '__main__':
    main()

