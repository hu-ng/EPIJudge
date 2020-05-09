from test_framework import generic_test
from test_framework.test_failure import TestFailure
import functools

def int_to_string(x: int) -> str:
    # Deal with negatives
    is_negative = False
    if x < 0:
        x = -x
        is_negative = True
    
    result = []
    to_convert = x

    # Case when int is 0
    if to_convert == 0:
        return "0"

    
    while to_convert > 0:
        last_digit = to_convert % 10
        to_convert = to_convert // 10
        result.append(chr(ord("0") + last_digit))

    if is_negative:
        return "-" + "".join(reversed(result))
    else:
        return "".join(reversed(result))


def string_to_int(s: str) -> int:
    is_negative = False
    if s[0] == "-":
        s = s[1:]
        is_negative = True
    if s[0] == "+":
        s = s[1:]

    sum_amt = 0
    for char in s:
        sum_amt = sum_amt * 10 + (ord(char) - ord("0"))
    return -1*sum_amt if is_negative else sum_amt



def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
