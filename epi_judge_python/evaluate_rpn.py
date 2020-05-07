from test_framework import generic_test


def evaluate(expression):
    operators = {
    "+": lambda y, x: x + y, "-": lambda y, x: x - y,
    "*": lambda y, x: x*y, "/": lambda y, x: int(x/y)
    }
    stack = []
    for char in expression.split(","):
        if char in operators:
            stack.append(operators[char](stack.pop(), stack.pop()))
        else:
            stack.append(int(char))
    return stack.pop()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
