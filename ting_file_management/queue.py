from collections import deque


class Queue:
    def __init__(self):
        self._data = deque()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        return self._data.popleft()

    def search(self, index):
        tam = len(self._data) - 1
        if (0 <= index <= tam):
            return self._data[index]
        else:
            raise IndexError('IndexError: deque index out of range')


# classe = Queue()

# classe.enqueue(1)
# classe.enqueue(2)
# classe.enqueue(3)

# print(classe.search(-1))
