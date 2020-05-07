from test_framework import generic_test


def binary_tree_depth_order(tree):
    if not tree:
        return []

    # Two queues:
    # 1 to track nodes at the current level, 1 to store nodes at next lev
    # Queue to track node at current level

    current_level = [tree]
    result = []
    while current_level:
        result.append([node.data for node in current_level])
        next_level = []
        # Figure out which node to list in the next level
        for node in current_level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        # Replace with next level
        current_level = next_level
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
