class Library:
    """
    represesent a library of books
    will have list of books
    add a book

    """

    def __init__(self, name):
        self.name = name
        self.books = [] # list of books to store

    # add a book
    def add_book(self, book):
        """ADDing a book to the collection of books"""
        self.books.append(book)
        print(f"Added {book.title} to the library")

    def show_all_books(self):
        """ Display all the books """
        print("inside show_all_books")
        for book in self.books:
            print(f"title is {book.display_info()}")


