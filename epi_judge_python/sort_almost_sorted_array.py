from typing import Iterator, List

from test_framework import generic_test
import heapq as hq


def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    result = []
    heap = []

    hq.heapify(heap)

    for _ in range(k):
        hq.heappush(heap, next(sequence))

    for x in sequence:
        smallest = hq.heappushpop(heap, x)
        result.append(smallest)

    while heap:
        result.append(hq.heappop(heap))
    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
