from test_framework import generic_test


def find_nearest_repetition(paragraph):
    hash = {}
    char = None
    lowest = float("inf")

    for idx, val in enumerate(paragraph):
        if val not in hash.keys():
            hash[val] = [float("inf"), idx]
        else:
            if idx - hash[val][1] < hash[val][0]:
                hash[val][0] = idx - hash[val][1]
                if idx - hash[val][1] < lowest:
                    char = val
                    lowest = idx - hash[val][1]
            hash[val][1] = idx
    return hash[char][0] if char is not None else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
