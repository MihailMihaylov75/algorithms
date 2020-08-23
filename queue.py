__author__ = 'Mihail Mihaylov'


class Queue(object):
    """Queue class"""

    def __init__(self):
        """Initialize"""
        self.items = []

    def enqueue(self, item):
        """Set the item in the first index"""
        return self.items.insert(0, item)

    def dequeue(self):
        """Returns the first added item"""
        return self.items.pop()

    def is_empty(self):
        """Check whether queue is empty"""
        return self.items == []

    def size(self):
        """Get number of items in the queue"""
        return len(self.items)
