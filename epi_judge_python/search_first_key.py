from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    L, R = 0, len(A) - 1
    first_oc = None

    while L <= R:
        M = L + (R - L)//2
        if A[M] < k:
            L = M + 1
        elif A[M] > k:
            R = M - 1
        elif A[M] == k:
            first_oc = M
            R = M - 1
    return first_oc if first_oc is not None else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
