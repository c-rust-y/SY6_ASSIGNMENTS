#Design a Library Management System using object-oriented programming 
# principles in Python. This system should manage books and patrons (library users), allowing for basic operations 
# such as adding new books, registering patrons, borrowing books, and returning books.

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"[{self.book_id}] {self.title} by {self.author} - {status}"


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"[{self.patron_id}] {self.name}"


class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    
    def add_book(self, book):
        if book.book_id in self.books:
            print("Book ID already exists.")
        else:
            self.books[book.book_id] = book
            print(f'Book "{book.title}" added successfully.')

    
    def register_patron(self, patron):
        if patron.patron_id in self.patrons:
            print("Patron ID already exists.")
        else:
            self.patrons[patron.patron_id] = patron
            print(f'Patron "{patron.name}" registered successfully.')

    
    def borrow_book(self, patron_id, book_id):
        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        if book_id not in self.books:
            print("Book not found.")
            return

        patron = self.patrons[patron_id]
        book = self.books[book_id]

        if book.is_borrowed:
            print(f'"{book.title}" is already borrowed.')
        else:
            book.is_borrowed = True
            patron.borrowed_books.append(book)
            print(f'{patron.name} borrowed "{book.title}".')

    
    def return_book(self, patron_id, book_id):
        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        if book_id not in self.books:
            print("Book not found.")
            return

        patron = self.patrons[patron_id]
        book = self.books[book_id]

        if book in patron.borrowed_books:
            patron.borrowed_books.remove(book)
            book.is_borrowed = False
            print(f'{patron.name} returned "{book.title}".')
        else:
            print(f"{patron.name} did not borrow this book.")

    
    def display_books(self):
        print("\nLibrary Books:")
        if not self.books:
            print("No books available.")
        else:
            for book in self.books.values():
                print(book)

    
    def display_patrons(self):
        print("\nRegistered Patrons:")
        if not self.patrons:
            print("No patrons registered.")
        else:
            for patron in self.patrons.values():
                borrowed = (
                    ", ".join(book.title for book in patron.borrowed_books)
                    if patron.borrowed_books
                    else "No books borrowed"
                )
                print(f"{patron} | Borrowed: {borrowed}")

library = Library()

library.add_book(Book(101, "Python Programming", "John Smith"))
library.add_book(Book(102, "Data Structures", "Alice Brown"))
library.add_book(Book(103, "Machine Learning", "Tom Wilson"))

library.register_patron(Patron(1, "Bunty"))
library.register_patron(Patron(2, "Bablu"))

library.display_books()
library.display_patrons()

library.borrow_book(1, 101)
library.borrow_book(2, 102)

library.display_books()
library.display_patrons()

library.return_book(1, 101)

library.display_books()
library.display_patrons()
        
