from typing import Optional

from bst_node import BstNode
from test_framework import generic_test


def find_first_greater_than_k(tree: BstNode, k: int) -> Optional[BstNode]:
    subtree, first = tree, None
    while subtree:
        # If current node value is bigger than k, than we know that the right answer must be in the tree rooted at the current node.
        if subtree.data > k:
            first, subtree = subtree, subtree.left
        # Else, go right
        else:
            subtree = subtree.right
    return first


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'search_first_greater_value_in_bst.py',
            'search_first_greater_value_in_bst.tsv',
            find_first_greater_than_k_wrapper))
