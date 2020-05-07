from typing import List

from test_framework import generic_test
import heapq as hq


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    # Form iterators out of sorted arrays
    heap = []
    result = []

    # Create iterators out of arrays, default to None
    sorted_iters = [iter(array) for array in sorted_arrays]
    hq.heapify(heap)

    # Add iterators to heap
    for idx, iterator in enumerate(sorted_iters):
        first_elem = next(iterator, None)
        if first_elem is not None:
            hq.heappush(heap, (first_elem, idx))

    # Extract from heap
    while heap:
        pop_elem = hq.heappop(heap)
        elem, idx = pop_elem[0], pop_elem[1]
        result.append(elem)
        next_elem = next(sorted_iters[idx], None)
        if next_elem is not None:
            hq.heappush(heap, (next_elem, idx))
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
