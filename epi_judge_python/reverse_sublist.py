from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from list_node import ListNode


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    dummy_head = sublist_head = ListNode(0, L)

    # Predecessor of the node to swap
    for _ in range(1, start):
        sublist_head = sublist_head.next


    # The tail of the reversed sublist is going to be the first node in the original sublist
    sublist_tail = sublist_head.next
    for _ in range(finish - start):
        # Current node to change the pointer of
        current_node = sublist_tail.next

        # Next node to update, update the tail to point to that node
        next_node = current_node.next
        sublist_tail.next = next_node

        # Point to the next node after sublist head
        current_node.next = sublist_head.next
        sublist_head.next = current_node

        # Though out the entire process, the next pointers for sublist head and tails change

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
