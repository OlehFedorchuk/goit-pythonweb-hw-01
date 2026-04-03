from __future__ import annotations

import logging
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


# SRP
class Book:
    def __init__(self, title: str, author: str, year: str) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


# ISP + DIP
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def show_books(self) -> None:
        pass


class Library(LibraryInterface):
    def __init__(self) -> None:
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        logger.info('Book "%s" added.', book.title)

    def remove_book(self, title: str) -> None:
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                logger.info('Book "%s" removed.', title)
                return

        logger.info('Book "%s" not found.', title)

    def show_books(self) -> None:
        if not self.books:
            logger.info("Library is empty.")
            return

        for book in self.books:
            logger.info("%s", book)


# OCP
class SearchableLibrary(Library):
    def find_book_by_author(self, author: str) -> None:
        found_books: list[Book] = [
            book for book in self.books if book.author.lower() == author.lower()
        ]

        if not found_books:
            logger.info('No books found for author "%s".', author)
            return

        for book in found_books:
            logger.info("%s", book)


# DIP
class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library = library

    def run(self) -> None:
        while True:
            command: str = (
                input("Enter command (add, remove, show, search_author, exit): ")
                .strip()
                .lower()
            )

            if command == "add":
                title: str = input("Enter book title: ").strip()
                author: str = input("Enter book author: ").strip()
                year: str = input("Enter book year: ").strip()

                book = Book(title, author, year)
                self.library.add_book(book)

            elif command == "remove":
                title: str = input("Enter book title to remove: ").strip()
                self.library.remove_book(title)

            elif command == "show":
                self.library.show_books()

            elif command == "search_author":
                if isinstance(self.library, SearchableLibrary):
                    author: str = input("Enter author name: ").strip()
                    self.library.find_book_by_author(author)
                else:
                    logger.info("Search by author is not supported in this library.")

            elif command == "exit":
                logger.info("Goodbye!")
                break

            else:
                logger.info("Invalid command. Please try again.")


if __name__ == "__main__":
    library: LibraryInterface = SearchableLibrary()
    manager = LibraryManager(library)
    manager.run()
