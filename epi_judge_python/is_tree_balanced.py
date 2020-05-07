from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    
    def check_balance(tree):
        # Doing a preorder traversal
        # If any of the left or right subtree is not balanced, return False
        # Base case: the leaf is always balanced
        if not tree:
            return (True, -1)

        left_result = check_balance(tree.left)
        if not left_result[0]:
            # Does not matter what we put in the height if it False
            return (False, 0)
        
        right_result = check_balance(tree.right)
        if not right_result[0]:
            return (False, 0)

        is_balanced = abs(left_result[1] - right_result[1]) <= 1
        helght = max(left_result[1], right_result[1]) + 1

        return (is_balanced, helght)
    return check_balance(tree)[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
