import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0, node1):
    # Find depth difference
    def get_depth(node):
        depth = 0
        while node:
            depth += 1
            node = node.parent
        return depth
    
    node0_depth, node1_depth = get_depth(node0), get_depth(node1)
    # Node 1 refers to the deeper node
    if node0_depth > node1_depth:
        node1, node0 = node0, node1
    
    # Raise deeper node up
    for _ in range(abs(node0_depth - node1_depth)):
        node1 = node1.parent
    
    # Move both nodes up together
    while node1 is not node0:
        node0, node1 = node0.parent, node1.parent
    
    # Return node
    return node0


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor_with_parent.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
