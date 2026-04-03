from abc import ABC, abstractmethod


# SRP
class Book:
    def __init__(self, title: str, author: str, year: str):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


# ISP + DIP:
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book):
        pass

    @abstractmethod
    def remove_book(self, title: str):
        pass

    @abstractmethod
    def show_books(self):
        pass

class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, title: str):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f'Book "{title}" removed.')
                return
        print(f'Book "{title}" not found.')

    def show_books(self):
        if not self.books:
            print("Library is empty.")
            return

        for book in self.books:
            print(book)


# OCP
class SearchableLibrary(Library):
    def find_book_by_author(self, author: str):
        found_books = [book for book in self.books if book.author.lower() == author.lower()]

        if not found_books:
            print(f'No books found for author "{author}".')
            return

        for book in found_books:
            print(book)


# DIP
class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def run(self):
        while True:
            command = input(
                "Enter command (add, remove, show, search_author, exit): "
            ).strip().lower()

            if command == "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()

                book = Book(title, author, year)
                self.library.add_book(book)

            elif command == "remove":
                title = input("Enter book title to remove: ").strip()
                self.library.remove_book(title)

            elif command == "show":
                self.library.show_books()

            elif command == "search_author":
                if isinstance(self.library, SearchableLibrary):
                    author = input("Enter author name: ").strip()
                    self.library.find_book_by_author(author)
                else:
                    print("Search by author is not supported in this library.")

            elif command == "exit":
                print("Goodbye!")
                break

            else:
                print("Invalid command. Please try again.")


if __name__ == "__main__":
    library = SearchableLibrary()
    manager = LibraryManager(library)
    manager.run()