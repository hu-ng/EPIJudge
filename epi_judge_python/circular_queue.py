from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity: int) -> None:
        self._entries = [None] * capacity
        self._head = self._tail = self._num_elements = 0
        return

    def enqueue(self, x: int) -> None:
        if self.size() == len(self._entries):
            self._entries = (
                self._entries[self._head:] + self._entries[:self._head]
            )
            self._head, self._tail = 0, self._num_elements
            self._entries += [None] * (len(self._entries) * 2 - len(self._entries))

        self._entries[self._tail] = x
        self._tail = (self._tail + 1) % len(self._entries)
        self._num_elements += 1

    def dequeue(self) -> int:
        if self._num_elements == 0:
            raise IndexError("Empty Queue")
        elem = self._entries[self._head]
        self._head = (self._head + 1) % len(self._entries)
        self._num_elements -= 1
        return elem

    def size(self) -> int:
        return self._num_elements


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
