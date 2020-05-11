from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    if not L:
        return L

    # Reuse the existing nodes
    # The reference is maintained
    even_head, odd_head = ListNode(0), ListNode(0)

    # values in the list do not affect the values outside the lists
    tails, turn = [even_head, odd_head], 0
    while L:
        tails[turn].next = L
        L = L.next
        tails[turn] = tails[turn].next
        turn ^= 1
    tails[0].next = odd_head.next
    tails[1].next = None
    return even_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
