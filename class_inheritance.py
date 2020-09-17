__author__ = 'Mihail Mihaylov'


# Simple inheritance
class Device(object):

    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def disconnect(self):
        self.connected = False


class Printer(Device):

    def __init__(self, name, connected_by, capacity):
        super(Printer, self).__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def print_pages(self, pages):
        if not self.connected:
            print('The device is not connected')
            return
        else:
            print('Printing {} pages'.format(pages))
            self.remaining_pages -= pages


# Composition
class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Book {}'.format(self.name)


class BookShelf:
    def __init__(self, *book):
        self.book = book

    def __str__(self):
        return 'BookShelf with {} books'.format(len(self.book))


book1 = Book('Harry Potter')
book2 = Book('Python')
shelf = BookShelf(book1, book2)
