# Library main file

class Library:
    def __init__(self):
        self._books = []
        self._patrons = []
        self._transactions = []

    def add_book(self, book):
        self._books.append(book)

    def remove_book(self, book):
        self._books.remove(book)

    def add_patron(self, patron):
        self._patrons.append(patron)
    
    def remove_patron(self, patron):
        self._patrons.remove(patron)
    
    def add_transaction(self, transaction):
        self._transactions.append(transaction)

    def remove_transaction(self, transaction):
        self._transactions.remove(transaction)
    
    def get_books(self):
        return self._books
    
    def get_patrons(self):
        return self._patrons
    