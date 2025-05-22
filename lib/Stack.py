class Stack:

    def __init__(self, items = None, limit = 100):
        self.items = list(items) if items else []
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if not self.full():
            self.items.append(item)
        else:
            raise IndexError("stack is full")

    def pop(self):
        if self.items:
            return self.items.pop()

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        return self.limit is not None and len(self.items) >= self.limit

    def search(self, target):
        try:
            return len(self.items) - self.items.index(target) - 1
        except ValueError:
            return -1
