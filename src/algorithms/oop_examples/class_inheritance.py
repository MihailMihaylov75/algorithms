"""
Problem:
Demonstrates object-oriented programming concepts:
1. Inheritance (Device → Printer)
2. Composition (Book → BookShelf)

This module is not an algorithm but an example of OOP principles.
"""


class Device:
    """
    Represents a generic device with a name and connection type.
    """

    def __init__(self, name: str, connected_by: str) -> None:
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def disconnect(self) -> None:
        """Disconnects the device."""
        self.connected = False


class Printer(Device):
    """
    Represents a printer device, derived from Device, with capacity for pages.
    """

    def __init__(self, name: str, connected_by: str, capacity: int) -> None:
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def print_pages(self, pages: int) -> None:
        """
        Prints the specified number of pages if connected.

        :param pages: Number of pages to print.
        """
        if not self.connected:
            print("The device is not connected")
            return
        print(f"Printing {pages} pages")
        self.remaining_pages -= pages


class Book:
    """Represents a single book."""

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"Book {self.name}"


class BookShelf:
    """Represents a bookshelf that holds multiple books (composition)."""

    def __init__(self, *books: Book) -> None:
        self.books = books

    def __str__(self) -> str:
        return f"BookShelf with {len(self.books)} books"
