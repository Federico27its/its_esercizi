from Excercise3_Book import Book

if __name__ == "__main__":
    book_str : str = "La Divina Commedia, Dante Alighieri, 999000666"
    b: Book = Book.from_string(book_str)
    print(b)