class OutOfStockError(Exception):
    pass


class Book:
    def __init__(self, title, copies):
        if copies < 0:
            raise ValueError("Copies cannot be negative")

        self.title = title
        self.__copies = copies

    def borrow(self):
        if self.__copies == 0:
            raise OutOfStockError("Book is out of stock")

        self.__copies -= 1
        print(f"You borrowed {self.title}")

    def return_book(self):
        self.__copies += 1
        print(f"You returned {self.title}")

    def get_copies(self):
        return self.__copies

    def show(self):
        print(f"Book: {self.title}")
        print(f"Available copies: {self.__copies}")


class EBook(Book):
    def __init__(self, title, copies, file_size_mb):
        super().__init__(title, copies)
        self.file_size_mb = file_size_mb

    def show(self):
        super().show()
        print(f"File size: {self.file_size_mb} MB")


book1 = Book("Python Basics", 2)
book2 = EBook("Learn Programming", 3, 5.5)

books = [book1, book2]

print("Library Books")

for book in books:
    book.show()
    print()

print("Borrowing Books")

try:
    book1.borrow()
    book1.borrow()
    book1.borrow()

except OutOfStockError as e:
    print(f"Sorry! {e}")

print("\nReturning Book")

book1.return_book()
print("Available copies:", book1.get_copies())

print("\nTesting Invalid Copies")

try:
    invalid_book = Book("Invalid Book", -2)

except ValueError as e:
    print(f"Error: {e}")
