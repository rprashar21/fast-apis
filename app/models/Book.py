class Book:
    """
    represent one book definition
    """
    def __init__(self, title, author, book_id):
        self.title= title
        self.author = author
        self.book_id = book_id
        self.is_borrowed = False  # Avialbe by default

    def display_info(self):
        status ="Borrowed" if self.is_borrowed else "Available"
        print(f"book_id is :: {self.book_id} status is {status}")
