from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    stack = []
    mapping = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in s:
        # If char is in the mapping, then there are two fail conditions
        if char in mapping:
            # stack is empty or most recent open brack does not match most recent closing bracket
            if not stack or stack[-1] != mapping[char]:
                return False
            else:
                stack.pop()
        else:
            stack.append(char)
    
    return stack == []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
