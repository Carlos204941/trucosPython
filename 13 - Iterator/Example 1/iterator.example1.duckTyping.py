class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class BookIterator:
    def __init__(self, books):
        self.books = books
        self.index = 0

    def next(self):
        book = self.books[self.index]
        self.index += 1
        return book

    def has_next(self):
        return self.index < len(self.books)
    
class Library:    
    def __init__(self):
        self.books = [
            Book("1984", "George Orwell"),
            Book("To Kill a Mockingbird", "Harper Lee"),
            Book("Moby-Dick", "Herman Melville")
        ]

    def create_iterator(self):
        return BookIterator(self.books)
    

library = Library()
iterator = library.create_iterator()    

while iterator.has_next():
        book = iterator.next()
        print(f"Title: {book.title}, Author: {book.author}")
        