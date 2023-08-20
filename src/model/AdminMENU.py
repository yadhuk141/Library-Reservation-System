import csv
import mysql.connector
from tabulate import tabulate
class Admin_menu:    
    def __init__(self):
        database_config  = {}
        with open("C:/Users/user/OneDrive/Desktop/LMS/Database_connection.txt", 'r') as file:
            lines = file.readlines()
            database_config['Host'] = lines[0].strip()
            database_config['User'] = lines[1].strip()
            database_config['Password'] = lines[2].strip()
            database_config['Database'] = lines[3].strip()
        try:
            self.connection = mysql.connector.connect(
                host=database_config['Host'],
                user=database_config['User'],
                password=database_config['Password'],
                database=database_config['Database']
            )
        except Exception:
            print("Error with database connection")
            return
        else:
            self.cursor = self.connection.cursor() 

    def Search(self,title):
        select_query = "SELECT * FROM books WHERE title = %s"
        self.cursor.execute(select_query, (title,))
        row = self.cursor.fetchone()
        return row

    def remove_user(self):
        username=input("Enter username to be deleted:")
        select_query = "SELECT * FROM users WHERE name = %s"
        self.cursor.execute(select_query, (username,))
        row = self.cursor.fetchone()
        if row is not None:
            delete_query = "DELETE FROM users WHERE name = %s"
            self.cursor.execute(delete_query, (username,))
            self.connection.commit()
            print("User deleted successfully!")
        else:
            print("User not found.")
        return

    def add_books(self):
        title=input("Enter book title:")
        author=input("Enter book author:")
        reservation=input("Enter reservation status:")
        insert_query = "INSERT INTO books (title, author, reservation) VALUES (%s, %s, %s)"
        values = (title, author, reservation)
        self.cursor.execute(insert_query, values)
        self.connection.commit()
        print("Book added successfully!\n")
        return

    def remove_books(self):
        title=input("Enter book title to be removed:")    
        delete_query = "DELETE FROM books WHERE title = %s"
        self.cursor.execute(delete_query, (title,))
        self.connection.commit()
        print("Book deleted successfully!\n")
        return

    def Return_books(self):
        title=input("Enter book title to be removed:")
        select_query = "SELECT reservation FROM books WHERE title = %s"
        self.cursor.execute(select_query, (title,))
        row = self.cursor.fetchone()
        if row:
            current_reservation = row[0]
            if current_reservation == "Yes":
                update_query = "UPDATE books SET reservation = 'No' WHERE title = %s"
                self.cursor.execute(update_query, (title,))
                self.connection.commit()
                print("Reservation status updated: Book is now unreserved.")
            else:
                print("This book is already unreserved.")
        else:
            print("Book not found.")
        return

    def view_users(self):
        select_query = "SELECT * FROM users"
        self.cursor.execute(select_query)
        rows = self.cursor.fetchall()
        if rows:
            columns = [desc[0] for desc in self.cursor.description]
            print(tabulate(rows, headers=columns, tablefmt="psql"))
            print("\n")
        else:
            print("No  users found\n")
        return

    def Book_manage(self):
        print("------BOOK MANAGEMENT--------")
        while True:
            print("1.Add books\n2.Remove books\n3.Return book\n4.Go back")
            try:
                ch=int(input("Enter choice:"))
            except Exception:
                print("Invalid choice try again")
                continue
            if ch==1:
                self.add_books()
            elif ch==2:
                self.remove_books()
            elif ch==3:
                self.Return_books()
            elif ch==4:
                return
            else:
                print("\nInvalid choice try again\n")

    def User_manage(self):
        print("------USER MANAGEMENT--------")
        while True:
            print("1.Remove user\n2.Go back")
            try:
                ch=int(input("Enter choice:"))
            except Exception:
                print("Invalid choice try again")
                continue
            if ch==1:
                self.remove_user()
            elif ch==2:
                return
            else:
                print("\nInvalid choice try again\n")


    def mainMenu(self):
        print("------ADMIN MENU--------")
        while True:
            print("1.Books management\n2.Users management\n3.View Users\n4.Go back")
            try:
                choice=int(input("Enter choice:"))
            except Exception:
                print("Invalid choice try again")
                continue
            if choice==1:
                self.Book_manage()
            elif choice==2:
                self.User_manage()
            elif choice==3:
                self.view_users()
            elif choice==4:
                return
            else:
                print("\nInvalid choice try again\n")
                
admin_Menu=Admin_menu() 