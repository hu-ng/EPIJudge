import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    def list_length(node):
        length = 0
        while node:
            length += 1
            node = node.next
        return length
    
    # Make l0 the larger list always, for simplicity
    if list_length(l0) < list_length(l1):
        l0, l1 = l1, l0
    
    # Advance the head of the longer list forward
    for _ in range(list_length(l0) - list_length(l1)):
        l0 = l0.next

    # Move at the same pace and see if we find any common node.
    while l0 != l1 and (l0 and l1):
        l0 = l0.next
        l1 = l1.next

        if l0 is l1:
            return l0
    return None


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
