import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook



def delete_duplicates(A: List[int]) -> int:
    # One pointer approach
    # That pointer always writes new unique entries
    if not A:
        return 0
    
    write_idx = 1
    for i, val in enumerate(A):
        if val != A[write_idx - 1]:
            A[write_idx] = val
            write_idx += 1
    return write_idx


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
