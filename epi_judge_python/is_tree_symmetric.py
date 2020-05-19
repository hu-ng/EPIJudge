from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:

    if not tree:
        return True

    def check_symmetry(left_subtree, right_subtree):
        # If both are null nodes, return True
        if not left_subtree and not right_subtree:
            return True

        # If one of the subtree is not null -> not symmetric
        if not left_subtree or not right_subtree:
            return False

        # If data is not the same -> not symmetric
        if left_subtree.data != right_subtree.data:
            return False
        
        return check_symmetry(left_subtree.right, right_subtree.left) and check_symmetry(left_subtree.left, right_subtree.right) 

    return check_symmetry(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
