from test_framework import generic_test


def intersect_two_sorted_arrays(A, B):
    a_idx, b_idx, result = 0, 0, []
    # Traverse the two arrays simultaneously
    while a_idx < len(A) and b_idx < len(B):

        # If element in A is smaller than element in B
        # then elem A can't be in intersection
        if A[a_idx] < B[b_idx]:
            a_idx += 1

        # If elem B < elem A, same
        elif A[a_idx] > B[b_idx]:
            b_idx += 1
        else:
            if A[a_idx] not in result:
                result.append(A[a_idx])
            a_idx += 1
            b_idx += 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
