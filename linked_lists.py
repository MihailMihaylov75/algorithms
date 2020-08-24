__author__ = 'Mihail Mihaylov'


# Singly linked list
class Node(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None

    @staticmethod
    def cycle_check(node):
        """Check if linked list contains cycle"""
        marker1, marker2 = node, node
        # If link is None break -> it is not cycle
        while marker1 and marker1.next_node:
            marker1 = marker1.next_node
            # Check if previous link is the same
            if marker1 == marker2:
                return True
            marker1 = marker1.next_node
            marker2 = marker2.next_node
        return False

    @staticmethod
    def reverse(head):
        current = head
        previous = None

        while current:
            nextnode = current.next_node
            current.next_node = previous

            previous = current
            current = nextnode
        return previous

    @staticmethod
    def get_nth_to_last_node(n, head):
        left_pointer, right_pointer = head, head

        for i in range(n-1):
            if not right_pointer.next_node:
                raise Exception('Error: n is larger than size of the linked list.')
            right_pointer = right_pointer.next_node

        while right_pointer.next_node:
            left_pointer = left_pointer.next_node
            right_pointer = right_pointer.next_node

        return left_pointer


a = Node(1)
b = Node(2)
c = Node(3)
# a.next_node.value has value 2
a.next_node = b
# b.next_node.value has value 3
b.next_node = c
"""
Linked Lists have constant-time insertions and deletions in any position,
in comparison, arrays require O(n) time to do the same thing.

Linked lists can continue to expand without having to specify their size ahead
of time.

To access an element in a linked list, you need to take O(k) time to go from the head
of the list to the kth element. In contrast, arrays have constant time operations to access elements in an array
"""


class DoublyLinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None


a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)

a.next_node = b
b.prev_node = a
b.next_node = c
c.prev_node = b
