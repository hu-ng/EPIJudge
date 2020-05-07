from test_framework import generic_test
from list_node import ListNode


def reverse_sublist(L, start, finish):
    dummy_head = sublist_head = ListNode(0, L)

    # Predecessor of the node to swap
    for _ in range(1, start):
        sublist_head = sublist_head.next

    # Swap
    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_iter.next
        (print("temp", temp))
        sublist_iter.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
