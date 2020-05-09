from test_framework import generic_test
import string

def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    is_negative = num_as_string[0] == "-"
    if is_negative:
        num_as_string = num_as_string[1:]

    # Convert b1 to 10
    num_as_int = 0
    for idx, char in enumerate(reversed(num_as_string)):
        num_as_int += string.hexdigits.index(char.lower())*b1**idx
    
    # Convert from 10 to b2
    result = []
    while True:
        result.append(string.hexdigits[num_as_int % b2].upper())
        num_as_int = num_as_int // b2
        if num_as_int == 0:
            break

    return ''.join(reversed(result)) if not is_negative else "-" + ''.join(reversed(result))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
