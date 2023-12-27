from utils import database

def prompt_add_book():
    name= input("Enter name of the book to add: ")
    author= input("Enter author of the book: ")
    
    database.add_book(name,author)

def list_books():
    books=database.get_all_books()
    for book in books:
        read = "Yes" if book['read'] else "No"
        print(f"{book['name']} by {book['author']}, read: {read}")
        
def prompt_read_book():
    name = input("Enter name of the book to make it read: ")
    database.read_book(name)

def prompt_delete_book():
    name = input("Enter name of the book to delete: ")
    database.delete_book(name)

user_options = {
    "a": prompt_add_book,
    "l": list_books,
    "d": prompt_delete_book,
    "r": prompt_read_book
    }

def menu():
    Prompt= "\nEnter 'a' to add a book, 'l' to list all the books,'d' to delete a book, 'r' to change the book to already read, or 'q' to quit:"
    selection = input(Prompt)
    database.create_book_table()
    while selection!="q":
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print("Unknown command,please try again")
            
        selection = input(Prompt)
menu()