__author__ = 'Mihail Mihaylov'


class Stack(object):
    """Simple implementation of stack"""

    def __init__(self):
        """Initialize"""
        self.items = []

    def is_empty(self):
        """Returns if stack is empty"""
        return self.items == []

    def push(self, item):
        """"Push item into stack"""
        return self.items.append(item)

    def pop(self, item):
        """Returns the last item of the stack and remove it from the stack"""
        if item > len(self.items):
            raise IndexError('Index out of range.')
        return self.items.pop(item)

    def peek(self):
        """Returns the last item of the stack without remove it from the stack"""
        if not len(self.items):
            raise IndexError('Index out of range.')
        return self.items[-1]

    def size(self):
        """Returns the number of elements in the stack"""
        return len(self.items)
