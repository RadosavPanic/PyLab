from library import Library


def main():
    while True:
        print(f"Welcome to the {library.name}. Following are options:")
        choice = """
        1. Display Books
        2. Lend a Book
        3. Add a Book
        4. Return a Book
        """
        print(choice)

        userInput = input("Press Q to quit and C to continue: ")
        if userInput == "C":
            userChoice = int(input("Select an option to continue: "))
            if userChoice == 1:
                library.displayBooks()
            elif userChoice == 2:
                book = input("Enter the name of the book you want to lend: ")
                user = input("Enter the name of the user: ")
                library.lendBook(book, user)
            elif userChoice == 3:
                book = input("Enter the name of the book you want to add: ")
                library.addBook(book)
            elif userChoice == 4:
                book = input("Enter the name of the book you want to return: ")
                library.returnBook(book)
            else:
                print("Please choose a valid option")
        elif userInput == "Q":
            break
        else:
            print("Please enter a valid option")


if __name__ == "__main__":
    booksList = []
    databaseName = input("Enter the name of database file with extension: ")
    bookDatabase = open(databaseName, "r")
    for book in bookDatabase:
        book = book.replace("\n", "")
        booksList.append(book)
    library = Library(booksList, "Arcadia Archives", databaseName)
    main()