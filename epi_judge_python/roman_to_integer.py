from test_framework import generic_test


def roman_to_integer(s: str) -> int:
    mapping = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    # Go from right to left is easier to code.
    result = 0
    for idx in reversed(range(len(s))):

        current_value = mapping[s[idx]]
        last_value = mapping[s[idx + 1]] if idx < len(s) - 1 else current_value

        if current_value < last_value:
            result -= current_value
        else:
            result += current_value

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
