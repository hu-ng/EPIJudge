from typing import List

from test_framework import generic_test, test_utils


def phone_mnemonic(phone_number: str) -> List[str]:
    mapping = ("0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ")

    # Alternative implementation, same idea of exploration

    # def helper(digit):
    #     if digit == len(phone_number):
    #         mnemonics.append("".join(current_mnemonic))
    #     else:
    #         for char in mapping[int(phone_number[digit])]:
    #             current_mnemonic[digit] = char
    #             helper(digit + 1)

    mnemonics = []
    # current_mnemonic = [0] * len(phone_number)
    # helper(0)

    def helper(idx, partial, storage):
        # Base case
        if idx == len(phone_number):
            storage.append("".join(partial))
            return
        
        # Get all the characters at the digit
        chars = mapping[int(phone_number[idx])]

        # Try every single character
        for char in chars:
            partial.append(char)
            helper(idx + 1, partial, storage)

            # Backtrack
            partial.pop()

    helper(0, [], mnemonics)

    return mnemonics


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
