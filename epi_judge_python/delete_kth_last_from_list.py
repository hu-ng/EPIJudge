from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    # Create a dummy head that points to the first node
    # Offset the list by 1 so that it can deal with deleting the first node
    dummy_head = ListNode(0, L)

    # Advance a pointer ahead
    advanced = dummy_head.next
    for _ in range(k):
        advanced = advanced.next
    
    # Find kth + 1 to last node
    start = dummy_head
    while advanced:
        start, advanced = start.next, advanced.next

    # Delete the kth to last node
    start.next = start.next.next
    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
