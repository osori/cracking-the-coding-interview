class Stack:
    def __init__(self):
        self.items = []
        self.num_items = 0

    def push(self, obj):
        self.items.append(obj)
        self.num_items += 1

    def pop(self):
        if self.is_empty():
            raise Exception("EmptyStackException")
        popped = self.items[self.num_items-1];
        del self.items[self.num_items-1];
        self.num_items -= 1
        return popped

    def peek(self):
        if self.is_empty():
            raise Exception("EmptyStackException")
        return self.items[self.num_items-1]

    def is_empty(self):
        return self.num_items == 0


s = Stack()

print(s.is_empty())
s.push("A")
s.push("B")
print(s.pop())
print(s.peek())
print(s.pop())
print(s.pop())

