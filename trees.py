__author__ = 'Mihail Mihaylov'


# Tree as list of lists
def binary_tree(r):
    return [r, [], []]


def insert_left(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root


def insert_right(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root


def get_root_value(root):
    return root[0]


def set_root_value(root, value):
    root[0] = value


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


"""
r = binary_tree(3)

insert_left(r, 4)
print(r)
"""

# Nodes and References Implementation of a Tree


class BinaryTree(object):
    """Binary tree class"""
    def __init__(self, new_node):
        self.key = new_node
        self.left_node = None
        self.right_node = None

    def insert_left(self, new_node):
        if self.left_node is None:
            self.left_node = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_node = self.left_node
            self.left_node = t

    def insert_right(self, new_node):
        if self.right_node is None:
            self.right_node = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_node = self.right_node
            self.right_node = t

    def get_left_node(self):
        return self.left_node

    def get_right_node(self):
        return self.right_node

    def get_root_value(self):
        return self.key

    def set_root_value(self, value):
        self.key = value
