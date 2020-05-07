from test_framework import generic_test


def look_and_say(n):
    def next_number(s):
        curr_idx = 0
        result = ""
        while curr_idx < len(s):
            temp_idx = curr_idx
            count = 0
            char = s[curr_idx]
            while temp_idx < len(s):
                if s[temp_idx] == s[curr_idx]:
                    count += 1
                    temp_idx += 1
                else:
                    break
            curr_idx = temp_idx
            result = result + str(count) + char
        return result

    s = "1"
    for _ in range(1, n):
        s = next_number(s)
    return s


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("look_and_say.py", "look_and_say.tsv",
                                       look_and_say))
