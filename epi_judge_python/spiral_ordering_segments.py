from test_framework import generic_test


def matrix_in_spiral_order(square_matrix):
    def spiral_clockwise(offset):
        if offset == len(square_matrix) - offset - 1:
            result.append(square_matrix[offset][offset])
        
        # top:
        result.extend(square_matrix[offset][offset: len(square_matrix) - offset - 1])

        # right:
        for row in range(offset, len(square_matrix) - offset - 1):
            result.append(square_matrix[row][len(square_matrix) - offset - 1])
        
        # bottom:
        result.extend(square_matrix[-1 - offset][-1 - offset : offset : -1])

        # left:
        for row in range(len(square_matrix) - offset - 1, offset, -1):
            result.append(square_matrix[row][offset])

    result = []
    for offset in range((len(square_matrix) + 1) // 2):
        spiral_clockwise(offset)

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
