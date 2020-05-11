from test_framework import generic_test


def look_and_say(n: int) -> str:

    # Old implementation (the book's answer). Kinda clunky tbh

    # def next_number(s):
    #     curr_idx = 0
    #     result = ""
    #     while curr_idx < len(s):
    #         temp_idx = curr_idx
    #         count = 0
    #         char = s[curr_idx]
    #         while temp_idx < len(s):
    #             if s[temp_idx] == s[curr_idx]:
    #                 count += 1
    #                 temp_idx += 1
    #             else:
    #                 break
    #         curr_idx = temp_idx
    #         result = result + str(count) + char
    #     return result

    # s = "1"
    # for _ in range(1, n):
    #     s = next_number(s)

    def next_number(s):
        result = []

        # Initialize the variables
        count = 0
        curr_char = s[0]

        for char in s:
            # If char is the same, add to count
            if char == curr_char:
                count += 1
            # If different char is found, append the result and reset variables
            else:
                result.append(str(count) + curr_char)
                count = 1  # Set to 1 because we found the first of the new char.
                curr_char = char

        # Process the result for the last set of chars because for loop stops at the last char.
        result.append(str(count) + curr_char)
        return "".join(result)

    s = "1"
    for _ in range(1, n):
        s = next_number(s)
    
    return s


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
