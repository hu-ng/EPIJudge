from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    # Merge elements from the back
    write_idx = m + n - 1
    a_idx, b_idx = m - 1, n - 1
    while a_idx > -1 and b_idx > -1:
        # If from a is larger
        if A[a_idx] > B[b_idx]:
            A[write_idx] = A[a_idx]
            a_idx -= 1
        # If from b is larger
        else:
            A[write_idx] = B[b_idx]
            b_idx -= 1
        write_idx -= 1
    
    # If a runs out, its ok
    # If b runs out, still have to merge it back
    while b_idx > -1:
        A[write_idx] = B[b_idx]
        write_idx -= 1
        b_idx -= 1

    return A


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
