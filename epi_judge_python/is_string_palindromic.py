from test_framework import generic_test


def is_palindromic(s: str) -> bool:
    # i moves forward, and j moves backward.
    i, j = 0, len(s) - 1

    # isalnum() to check if a string is alphanumeric

    while i < j:
        # Move forward until s[i] is alphanumeric
        while not s[i].isalnum() and i < j:
            i += 1

        # Move backward until s[j] is alphanumeric
        while not s[j].isalnum() and i < j:
            j += 1

        # Check palindrome condition
        if s[i].lower() != s[j].lower():
            return False
        
        i += 1
        j -= 1
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_palindromic.py',
                                       'is_string_palindromic.tsv',
                                       is_palindromic))
