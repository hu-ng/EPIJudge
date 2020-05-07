import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    # First pass: remove the b's
    write_idx = 0
    b_count = 0
    a_count = 0

    for idx, value in enumerate(s):
        if value != "b":
            s[write_idx] = s[idx]
            write_idx += 1
            if value == "a":
                a_count += 1
        elif value == "b":
            b_count += 1
            
    # Second pass: move backwards, start from write_idx
    new_size = size + a_count - b_count
    write_idx = size - b_count - 1
    new_write_idx = new_size - 1
    for idx in range(write_idx, -1, -1):
        if s[idx] == "a":
            s[new_write_idx]  = "d"
            s[new_write_idx - 1] = "d"
            new_write_idx -= 2
        else:
            s[new_write_idx] = s[idx]
            new_write_idx -= 1
    return new_size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
