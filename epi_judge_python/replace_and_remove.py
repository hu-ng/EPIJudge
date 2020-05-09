import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    # First pass: remove the b's
    write_idx = 0
    a_count = 0

    for idx, value in enumerate(s):
        if value != "b" and value != "":
            s[write_idx] = s[idx]
            write_idx += 1
        if value == "a":
            a_count += 1
            
    # Second pass: move backwards, start from write_idx

    # Current idx: after deleting all the b's
    cur_idx = write_idx - 1

    # Where to start writing
    write_idx += a_count - 1

    # Final size = last idx + 1
    final_size = write_idx + 1

    while cur_idx >= 0:
        if s[cur_idx] == "a":
            s[write_idx]  = "d"
            s[write_idx - 1] = "d"
            write_idx -= 2
        else:
            s[write_idx] = s[cur_idx]
            write_idx -= 1
        cur_idx -= 1
    return final_size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
