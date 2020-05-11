from typing import List

from test_framework import generic_test


# Recursive approach
def get_valid_ip_address(s: str) -> List[str]:
    def part_valid(part):
        return len(part) == 1 or (part[0] != "0" and int(part) <= 255)


    def generate(idx, segment, partial, storage):
        if segment == 4:
            if idx == len(s):
                storage.append(".".join(partial))
            return
        
        for segment_size in range(1, 4):
            segment_end = idx + segment_size

            if segment_end > len(s):
                break

            part = s[idx:segment_end]
            partial.append(part)
            if part_valid(part):
                generate(segment_end, segment + 1, partial, storage)
            partial.pop()
    
    storage = []
    generate(0, 0, [], storage)
    return storage


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('valid_ip_addresses.py',
                                       'valid_ip_addresses.tsv',
                                       get_valid_ip_address,
                                       comparator=comp))
