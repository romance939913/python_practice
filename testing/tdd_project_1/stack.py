class Stack: 
    def __init__(self):
        self._values = []

    def __len__(self):
        return len(self._values)

    def push(self, value):
        return self._values.append(value)

    def peek(self):
        return self._values[-1]

    def pop(self):
        return self._values.pop()
