#Importing sqlite3 and os
import sqlite3
import os

#Checking if the database ebookstore.db already exists, if it does, means that the table has already been created, so skip.
file_name = "ebookstore.db"

if os.path.exists(file_name):
    print(f"The file {file_name} already exists in the current directory, skipping...")
    
else:
    conn = sqlite3.connect('ebookstore.db')

    #getting a cursor object
    cursor = conn.cursor()

    #creating a table
    cursor.execute('''
        CREATE TABLE books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Title TEXT NOT NULL,
        Author TEXT NOT NULL,
        Qty INTEGER
    )
    ''')

    #Creating a list with all the books to insert into the table
    books_list = [
        (3001, 'A tale of two cities', 'Charles Dickens', 30),
        (3002, 'Harry Potter', 'J.K. Rowling', 40),
        (3003, 'The Lion, the witch and the wardrobe', 'C.S Lewis', 25),
        (3004, 'The Lord of the Rings', 'J.R.R. Tolkien', 37),
        (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)
    ]

    #Inserting the books inside the books_list to the table
    cursor.executemany('INSERT INTO books VALUES (?,?,?,?)', books_list)

    conn.commit()
    conn.close()


___________________________________________________________________________________________________________________________________________________________________________________________



#Creating a function to enter a new book to the table:
def enter_book():
    conn = sqlite3.connect("ebookstore.db")
    cursor = conn.cursor()

    #Asking the user for the books information
    title = input("Enter the title of the book: ")
    author = input('Enter the author of the book: ')
    
    #Using try/except to prevent value errors
    while True:
        try:
            qty = int(input('Enter the quantity of books: '))
            break
        except ValueError:
            print('Please make sure you are entering a number')
    
    #inserting the data in the table
    cursor.execute("""
        INSERT INTO books (Title, Author, Qty)
    VALUES (?, ?, ?)
    """, (title, author, qty))
    print('Book inserted')
    
    conn.commit()
    conn.close()
    return

#Creating a function to update a book information:
def update_book():
    conn = sqlite3.connect("ebookstore.db")
    cursor = conn.cursor()
    
    while True:
        
        #asking the user for the id of the book he wants to update
        id_check = int(input('Enter the id of the book you want to update: '))

        #retrieve all items from the column in the table
        cursor.execute("SELECT id FROM books")
        items = cursor.fetchall()

        #iterate through the items and check if any of them match with the input
        for item in items:
            if item[0] == id_check:
                #Asking for the new quantity of books
                new_qty = int(input('Enter the new quantity of books: '))
    
                #updating the qty
                cursor.execute("UPDATE books SET qty = ? WHERE id = ?", (new_qty, id_check))
            
                conn.commit()
                conn.close()
                return
    
        print('The ID you entered does not match any of the IDs in the system, please try again..')

#Creating a function to delete a book from the table:
def delete_book():
    conn = sqlite3.connect("ebookstore.db")
    cursor = conn.cursor()
    
    while True:
        
        #asking the user the id of the book to be deleted
        delete = int(input('Enter the ID of the book you would like to delete: '))
        
        #retrieve all items from the column in the table
        cursor.execute("SELECT id FROM books")
        items = cursor.fetchall()

        #iterate through the items and check if any of them match with the input
        for item in items:
            if item[0] == delete:
                cursor.execute("DELETE FROM books WHERE id = ?", (delete,));
                print('Book deleted')
                
                conn.commit()
                conn.close()
                return
        
        print('The ID you entered does not match any of the IDs in the system, please try again..')
        
def search_book():
    conn = sqlite3.connect("ebookstore.db")
    cursor = conn.cursor()
    
    while True:
        
        #asking the user if wants to use name or id to search for the book
        option = input('Enter "id" if you want to use ID to search, or "title" if you want to use the title of the book: ').lower()
            
        if option == 'id':
            
            #asking for the book id
            book_id = int(input('Enter the ID of the book you would like to search: '))
            
            #retrieve all items from the column in the table
            cursor.execute("SELECT id FROM books")
            items = cursor.fetchall()

            #iterate through the items and check if any of them match with the input
            for item in items:
                if item[0] == book_id:
                    
                    #selecting all items from the row where the id matches and printing them
                    cursor.execute("SELECT * FROM books WHERE id = ? """, (book_id,))
                    result = cursor.fetchone()                   
                    print(result)
                    
                    conn.commit()
                    conn.close()
                    return

            print('The ID you entered does not match any of the IDs in the system, please try again..')
        
        elif option == 'title':
            
            #asking for the book id
            book_title = input('Enter the title of the book you would like to search: ')
            
            #retrieve all items from the column in the table
            cursor.execute("SELECT Title FROM books")
            items = cursor.fetchall()

            #iterate through the items and check if any of them match with the input
            for item in items:
                if item[0] == book_title:
                    
                    #selecting all items from the row where the title matches and printing them
                    cursor.execute("SELECT * FROM books WHERE Title = ?", (book_title,))
                    result = cursor.fetchone()                   
                    print(result)
                    
                    conn.commit()
                    conn.close()
                    return
            print('The title you entered does not match any of the books in the system, please try again..')
        
        else:
            print('Please enter "id" or "title"..')

___________________________________________________________________________________________________________________________________________________________________________________________

#Creating a menu
while True:
    menu = input('''Please choose one of the following:
e = Enter book
u = Update book
d = Delete book
s = Search book
exit = exit the code
''')
    
    if menu == 'e':
        enter_book()
        
    elif menu == 'u':
        update_book()
    
    elif menu == 'd':
        delete_book()
        
    elif menu == 's':
        search_book()
    
    elif menu == 'exit':
        print('Goodbye!')
        break
    
    else: 
        print('Input invalid, please try again..')
