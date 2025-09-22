__author__ = 'Mihail Mihaylov'

from src.algorithms.oop_examples.class_inheritance import Book, BookShelf, Printer


def test_printer_print_reduces_remaining_pages() -> None:
    printer = Printer("HP", "USB", 100)
    printer.print_pages(10)
    assert printer.remaining_pages == 90


def test_printer_disconnect_sets_connected_false() -> None:
    printer = Printer("HP", "USB", 100)
    printer.disconnect()
    assert not printer.connected


def test_bookshelf_str_counts_books() -> None:
    shelf = BookShelf(Book("Harry Potter"), Book("Python 101"))
    assert str(shelf) == "BookShelf with 2 books"
