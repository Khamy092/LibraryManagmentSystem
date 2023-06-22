from Book import Book


def test_check_availability():
    book = Book("The Hobbit", "J.R.R. Tolkien", 1937, "9780007525492", 2)
    assert book.check_availability() == True

def test_update_availability():
    book = Book("The Hobbit", "J.R.R. Tolkien", 1937, "9780007525492", 2)
    book.update_availability(book)
    assert book.check_availability() == False

def test_display_info():
    book = Book("The Hobbit", "J.R.R. Tolkien", 1937, "9780007525492", 2)
    assert book.display_info() == f'Title: {book.title}\nAuthor: {book.author}\nYear: {book.year}\nISBN: {book.isbn}\nAvailable: {book.isAvailable}\nNumber of copies: {book.numberOfCopies}'