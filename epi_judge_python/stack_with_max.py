from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:
    def __init__(self):
        self.stack = []
        self.max_list = []

    def empty(self):
        return len(self.stack) == 0


    def max(self):
        return 0 if self.empty() else self.max_list[-1]

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        else:
            elem = self.stack.pop()
            self.max_list.pop()
        return elem

    def push(self, x):
        self.stack.append(x)
        if len(self.max_list) == 0:
            self.max_list.append(x)
        elif x > self.max_list[-1]:
            self.max_list.append(x)
        else:
            self.max_list.append(self.max_list[-1])


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("stack_with_max.py",
                                       'stack_with_max.tsv', stack_tester))
