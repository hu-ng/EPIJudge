from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    # reverse inorder, only go k elements in
    result = []
    def reverse_inorder(tree):
        if tree:
            reverse_inorder(tree.right)
            if len(result) < k:
                result.append(tree.data)
                reverse_inorder(tree.left)
    
    reverse_inorder(tree)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
