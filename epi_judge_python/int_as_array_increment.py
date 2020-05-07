from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    # Operate on the array itself so as to not rely on the integer representation
    # More about implementation than logic

    # Add 1 to the last digit
    A[-1] += 1

    for idx in reversed(range(1, len(A))):

        # If there is no carry-over, just end it there
        if A[idx] != 10:
            break
        # If there is, continue adding over
        A[idx] = 0
        A[idx - 1] += 1
    
    # Happens with A = [9,9,9]
    if A[0] == 10:
        # If the first digit is "10", then we append 0 at the end.
        A.append(0)
        A[0] = 1

    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
