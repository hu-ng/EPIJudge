from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    if not tree:
        return []

    # Two queues:
    # 1 to track nodes at the current level, 1 to store nodes at next lev
    # Queue to track node at current level

    current_level = [tree]
    result = []
    while current_level:
        next_level = []
        level_result = []
        
        # Process from front to back
        for node in current_level:
            # Add current node to result
            level_result.append(node.data)

            # Find next nodes to explore
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
                
        current_level = next_level
        result.append(level_result)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
