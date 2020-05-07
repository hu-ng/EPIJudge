from test_framework import generic_test
import collections


def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    # Frequency of letters in the letter
    letter_freq = collections.Counter(letter_text)

    # Pass over the magazine text
    for char in magazine_text:
        if char in letter_freq.keys():
            if letter_freq[char] != 0:
                letter_freq[char] -= 1
                if letter_freq[char] == 0:
                    del letter_freq[char]

    return len(letter_freq.keys()) == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
