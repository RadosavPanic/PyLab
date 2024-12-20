class Library:
    def __init__(self, bookslist, name, databaseName):
        self.booksList = bookslist
        self.name = name
        self.databaseName = databaseName
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.booksList:
            print(book)
        print("\n")

    def addBook(self, book):
        if book in self.booksList:
            print("Book already exists")
        else:
            self.booksList.append(book)
            bookDatabase = open(self.databaseName, "a")
            bookDatabase.write(f"\n{book}")
            print("Book added")

    def lendBook(self, book, user):
        if book in self.booksList:
            if book not in self.lendDict.keys():
                self.lendDict.update({book: user})
                print("Book has been lended. Database updated.")
            else:
                print(f"Book is already being used by {self.lendDict[book]}")
        else:
            print("Apologies! We don't have this book in our library.")

    def returnBook(self, book):
        if book in self.lendDict.keys():
            self.lendDict.pop(book)
            print("Book returned successfully")
        else:
            print("The book does not exist in the book lending database.")
