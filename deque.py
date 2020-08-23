__author__ = 'Mihail Mihaylov'


class Deque(object):
    """Class Deque"""

    def __init__(self):
        """Initialize"""
        self.items = []

    def is_empty(self):
        """Returns whether dequeue is empty"""
        return self.items == []

    def add_front(self, item):
        """Add item in the end of the deque"""
        self.items.append(item)

    def add_rear(self, item):
        """Add item at the beginning of the deque"""
        self.items.insert(0, item)

    def remove_front(self):
        """Removes the last item of the deque"""
        return self.items.pop()

    def remove_rear(self):
        """Removes the first added item of the deque"""
        return self.items.pop(0)

    def size(self):
        """Returns number of the items in the deque"""
        return len(self.items)

