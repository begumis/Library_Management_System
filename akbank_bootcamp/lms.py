class Library:
    def __init__(self, file_name="books.txt"):
        self.file_name = file_name
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()
        print(f"File '{self.file_name}' closed.")

    def list_book(self):
        self.file.seek(0) 
        books = self.file.read().splitlines()
        for book in books:
            book_info= book.split(',')
            book_title = book_info[0]
            book_author = book_info[1]
            print(f"Book name: '{book_title}'\nAuthor: '{book_author}'")

    def add_book(self):
        book_title = input("Enter the book title: ")
        book_author = input("Enter the book author: ")
        first_release_year = input("Enter the first release year: ")
        number_of_pages = input("Enter the number of pages: " )

        book_info  = f"{book_title},{book_author},{first_release_year},{number_of_pages}\n"
        self.file.write(book_info)
        print("Book added successfully")
    
    def remove_book(self):
        book_title = input("Enter the book title which you want to remove: ")
        self.file.seek(0)
        books = self.file.read().splitlines()
        new_books= []
        found=False
        for book in books:
            book_info= book.split(',')
            if book_title != book_info[0]:
                new_books.append(book)
            else:
                found =True
        self.file.seek(0)
        self.file.truncate()
        for book in new_books:
            self.file.write(book+'\n')
        if found:
            print("Book removed successfully")
        else:
            print("Book not found in the library")

lib= Library()

while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("Press Q to Quit")

    choice = input("\nEnter your choice: ")
    if choice == "1":
        lib.list_book()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice.lower() == "q":
        print("See you again, have a nice day...")
        exit()
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")  