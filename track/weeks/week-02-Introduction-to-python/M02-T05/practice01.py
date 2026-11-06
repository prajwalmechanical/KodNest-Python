# Create a Book class

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

title = input()
author = input()
price = int(input())

book = Book(title, author, price)

print(book.title)
print(book.author)
print(book.price)
