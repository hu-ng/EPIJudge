from typing import List
import math
from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    # Constraints: row, column, sub 3x3 grid

    n = len(partial_assignment)
    def has_duplicate(block):
        block = list(filter(lambda x: x != 0, block))
        return len(block) != len(set(block))

    # Check rows and cols
    if any(
        has_duplicate([partial_assignment[i][j] for j in range(n)])
        or has_duplicate([partial_assignment[j][i] for j in range(n)]) for i in range(n)
    ):
        return False

    # Check all regions
    region_size = int(math. sqrt(n))
    return all(not has_duplicate([
        partial_assignment[a][b]
        for a in range(region_size * I, region_size * (I + 1))
        for b in range(region_size * J, region_size * (J + 1))
    ]) for I in range(region_size) for J in range(region_size))

    

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
