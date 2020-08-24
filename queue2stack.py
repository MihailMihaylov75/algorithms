__author__ = 'Mihail Mihaylov'


class Queues2Stack(object):
    """"Queue2Stack class"""

    def __init__(self):
        """"Initialization"""
        self.instack = []
        self.oustack = []

    def enqueue(self, element):
        """"Set the element in the last index"""
        self.instack.append(element)

    def dequeue(self):
        """"Returns first added element"""
        if not self.oustack:
            while self.instack:
                self.oustack.append(self.instack.pop())

        return self.oustack.pop()
