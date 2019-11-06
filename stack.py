class Stack:
    def __init__(self, lst=[]):
        self.storage = lst if type(lst) == list else [] # just a 'list'

    def push(self, item):
        self.storage.append(item)

    def pop(self):
        return self.storage.pop(-1) if not self.empty() else None

    def peek(self):
        return self.storage[-1] if not self.empty() else None

    def empty(self):
        return len(self) == 0

    def clear(self):
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def __str__(self):
        return f'{self.storage} <->'
