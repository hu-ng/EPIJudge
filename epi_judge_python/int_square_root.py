from test_framework import generic_test


def square_root(k: int) -> int:
    # Binary search, but compare using the square of the middle entry
    L, R = 0, k
    while L <= R:
        M = L + (R - L)//2
        if M**2 > k:
            R = M - 1
        elif M**2 <= k:
            L = M + 1

    return L - 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
