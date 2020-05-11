from test_framework import generic_test


def snake_string(s: str) -> str:
    result = []

    # Do this in three iterations
    # Top row
    for idx in range(1, len(s), 4):
        result.append(s[idx])
    
    # Middle
    for idx in range(0, len(s), 2):
        result.append(s[idx])
    
    # Bottom row
    for idx in range(3, len(s), 4):
        result.append(s[idx])
    
    return "".join(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('snake_string.py', 'snake_string.tsv',
                                       snake_string))
