from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    path_stack = []
    path_lst = path.split("/")

    if not path:
        raise ValueError

    if path[0] == "/":
        path_stack.append("/")

    for folder in path_lst:
        if folder == "..":
            if not path_stack or path_stack[-1] == "..":
                path_stack.append(folder)
            else:
                if path_stack[-1] == "/":
                    raise ValueError
                path_stack.pop()
        elif folder in [".", ""]:
            continue
        else:
            path_stack.append(folder)
    result = "/".join(path_stack)
    return result[result.startswith("//"):]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
