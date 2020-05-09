import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].

def reverse_range(s, start, end):
    # Reverse a string from start to end
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1


def reverse_words(s):
    # Reverse the whole string first
    reverse_range(s, 0, len(s) - 1)

    # Reverse every word in the list
    start_idx = 0
    for end_idx, val in enumerate(s):
        if val == " ":
            reverse_range(s, start_idx, end_idx - 1)
            start_idx = end_idx + 1
        if end_idx == len(s) - 1:
            reverse_range(s, start_idx, end_idx)

    return s


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
