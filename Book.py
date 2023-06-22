# Book class


class Book:
    def __init__(self, title, author, year, isbn, NumberOfCopies=0):
        self._title = title
        self._author = author
        self._year = year
        self._isbn = isbn
        self.isAvailable = True
        self.numberOfCopies = NumberOfCopies

    
    # Getters and setters using the @property decorator

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if title == "":
            raise ValueError("Title cannot be empty.")
        self._title = title

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if author == "":
            raise ValueError("Author cannot be empty.")
        self._author = author

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, year):
        if year == "" or type(year) != int:
            raise ValueError("Year cannot be empty and must be a number.")
        self._year = year

    @property
    def isbn(self):
        return self._isbn
    
    @isbn.setter
    def isbn(self, isbn):
        if isbn == "":
            raise ValueError("ISBN cannot be empty.")
        self._isbn = isbn

    
    # Methods

    def check_availability(self):
        pass

    def update_availability(self):
        pass

    def display_info(self):
        pass