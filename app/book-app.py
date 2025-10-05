from app.models.Book import Book
from app.models.Library import Library

if __name__ == "__main__":
    # create a library object
    library = Library("Rohits Library")

    # addinga book to library
    book_list = []
    for i in range(1, 5):
        book = Book("jungle book", "kupling", i)
        library.add_book(book)


    # display all the books
    library.show_all_books()