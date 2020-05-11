import collections
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:

    words_to_cover = collections.Counter(keywords)
    result = (-1, -1)
    remaining_words = len(keywords)

    left = 0
    # Expand the right boundary until the condition is met
    for right, word in enumerate(paragraph):
        if word in keywords:
            words_to_cover[word] -= 1
            # If count of keyword turns to zero, subtract 1 from remaining words
            if words_to_cover[word] == 0:
                remaining_words -= 1

        # Contract the left boundary until the condition is broken
        while remaining_words == 0:
            # If result is the default value or the new range is smaller than the existing range
            if result == (-1, -1) or right - left < result[1] - result[0]:
                result = (left, right)
            
            curr_word = paragraph[left]
            if curr_word in keywords:
                words_to_cover[curr_word] += 1

                # If keyword gained a new count, add one to remaining words count
                if words_to_cover[curr_word] == 1:
                    remaining_words += 1
            left += 1
    return result


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure('Index out of range')

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure('Not all keywords are in the range')

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_set.py',
            'smallest_subarray_covering_set.tsv',
            find_smallest_subarray_covering_set_wrapper))
