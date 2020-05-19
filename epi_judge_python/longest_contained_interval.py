from typing import List

from test_framework import generic_test
from collections import Counter

def longest_contained_range(A: List[int]) -> int:
    occurence = Counter(A)
    max_length = 0

    for num in A:
        if occurence.get(num):
            right = left =  num
            current_len = 1
            # Expand the set to the left and right and keeping track of length of current set.
            
            # Expand the set to the right
            while occurence.get(right + 1):
                right = right + 1
                del occurence[right]
                current_len += 1

            # Expand the set to the left
            while occurence.get(left - 1):
                left = left - 1
                del occurence[left]
                current_len += 1

            max_length = max(max_length, current_len)
    return max_length


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('longest_contained_interval.py',
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
