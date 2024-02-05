class BaseStack():
    def __init__(self):
        self.data = []


class AddStack(BaseStack):
    def push(self, element):
        self.data.append(element)

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"

class RemoveStack(BaseStack):
    def pop(self):
        return self.data.pop()

class TopStack(BaseStack):
    def top(self):
        return self.data[-1]

class IsEmpty(BaseStack):
    def is_empty(self):
        if self.data:
            return False
        return True

class Stack(AddStack, RemoveStack, TopStack, IsEmpty):
    pass

a = Stack()
a.push("carrot")
a.push("zele")
print(a.__str__())