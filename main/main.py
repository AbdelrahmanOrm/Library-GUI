import json

class Library:

    def __init__(self):
        # Load the JSON data when creating an instance of the Library class
        self.data = self.load_json_data()

    # Load the JSON data from the file (books.json)
    def load_json_data(self):
        filename = "books.json"
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            return {}

    # Search for a book by its title
    def searchBookByTitle(self, title):
        if title in self.data:
            return self.data[title]
        else:
            return None

    # Search for books by author name
    def  searchBookByAuthor(self, author):
        books_by_author = {}
        for title, book_info in self.data.items():
            if book_info["author"] == author:
                books_by_author[title] = book_info
        return books_by_author


class Section():
    def __init__(self, title):
        self.__title = title
        self.__books = []

    def getTitle(self):
        return self.__title

    def addBook(self, book):
        self.books.append(book)

class Book:
    def __init__(self, title, author, cost):
        self.__title = title
        self.__author = author
        self.__cost = cost

    def getTitle(self):
        return self.__title

    def getAuthor(self):
        return self.__author

    def getCost(self):
        return self.__cost

library_instance = Library()
