#......................................................................
# kohen johnsotn
# 2024-05-03
# simple poop
#.......................................................................

#imports
import time 



# Classes
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")
        time.sleep(2)

class Bookstore:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' to the bookstore.")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Removed '{title}' from the bookstore.")
                return
        print(f"Book with title '{title}' not found in the bookstore.")

    def show_books(self):
        if self.books:
            print("Books available in the bookstore:")
            for book in self.books:
                book.display_info()
                print()
        else:
            print("No books available in the bookstore.")


# main code 
if __name__ == "__main__":



    # Books names and information
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction")
    book3 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "Fantasy")

    # Making the bookstore
    bookstore = Bookstore()

    # Adding the books we made in the bookstore
    bookstore.add_book(book1)
    bookstore.add_book(book2)
    bookstore.add_book(book3)

    # Shows all books in the bookstore
    bookstore.show_books()

    # Taking books from the bookstore
    bookstore.remove_book("To Kill a Mockingbird")
    bookstore.remove_book("The Great Gatsby")
    bookstore.remove_book("Harry Potter and the Sorcerer's Stone")


    # Shows the leftover books in the bookstore which is none
    bookstore.show_books()
