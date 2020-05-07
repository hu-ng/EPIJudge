from test_framework import generic_test


def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
    # Check the BST property at every node
    if not tree:
        return True
    # If not in this range: return False
    elif not low_range <= tree.data <= high_range:
        return False
    else:
        return is_binary_tree_bst(tree.left, low_range, tree.data) and is_binary_tree_bst(tree.right, tree.data, high_range)
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_a_bst.py", 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
