from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:

    # Store location of inorder nodes in hash table to save time
    inorder_node_to_idx = {data: i for i, data in enumerate(inorder)}

    # Build the tree recursively
    def tree_helper(preorder_start, preorder_end, inorder_start, inorder_end):
        if preorder_end <= preorder_start or inorder_end <= inorder_start:
            return None
        
        # Find the index of the root in the inorder array
        root_inorder_idx = inorder_node_to_idx[preorder[preorder_start]]

        # Calculate size of left subtree
        left_subtree_size = root_inorder_idx - inorder_start
        return BinaryTreeNode(
            preorder[preorder_start],

            # Build left subtree
            tree_helper(preorder_start + 1, preorder_start + 1 + left_subtree_size,
                        inorder_start, root_inorder_idx),

            # Build right subtree
            tree_helper(preorder_start + 1 + left_subtree_size, preorder_end,
                        root_inorder_idx + 1, inorder_end)
        )
    return tree_helper(0, len(preorder), 0, len(inorder))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
