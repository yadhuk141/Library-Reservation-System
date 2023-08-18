from controller.Homedelivery import HD
from model.AdminMENU import admin_Menu as am
import mysql.connector
from tabulate import tabulate

class Home:
    def __init__(self):
        db_config  = {}
        with open("C:/Users/user/OneDrive/Desktop/LMS/Database_connection.txt", 'r') as file:
            lines = file.readlines()
            db_config['Host'] = lines[0].strip()
            db_config['User'] = lines[1].strip()
            db_config['Password'] = lines[2].strip()
            db_config['Database'] = lines[3].strip()
        try:
            self.connection = mysql.connector.connect(
                host=db_config['Host'],
                user=db_config['User'],
                password=db_config['Password'],
                database=db_config['Database']
            )
        except Exception:
            print("Error with database connection")
            return
        else:
            self.cursor = self.connection.cursor() 
       
    def Search(self,title):
        select_query = "SELECT reservation FROM books WHERE title = %s"
        self.cursor.execute(select_query, (title,))
        rows = self.cursor.fetchall()
        if rows:
            print("Reservation status for book", title, ":")
            print(rows[0][0])
            print("\n")
        else:
            print("Book not found\n")
        self.cursor.close()
        self.connection.close()


    def Reserve(self):
        cursor=self.connection.cursor()
        title=input("Enter title: ")
        select_query = "SELECT * FROM books WHERE title = %s"
        cursor.execute(select_query, (title,))
        row = cursor.fetchone()
        if row is None:
            print("Book not found\n")
        else:
            reserve_value = row[2]
            if reserve_value == "No":
                update_query = "UPDATE books SET reservation = 'Yes' WHERE title = %s"
                cursor.execute(update_query, (title,))
                self.connection.commit()
                print("Reserved successfully\n")
            elif reserve_value == "Yes":
                print("Book is already reserved\n")
        return

    
    def BookList(self):
        cursor=self.connection.cursor()
        select_query = "SELECT * FROM books"
        cursor.execute(select_query)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        print(tabulate(rows, headers=columns, tablefmt="psql"))
        print("\n")
        cursor.close()
        self.connection.close()
        return


    def Menu(self,username):
        count=0
        print("Please select required operation\n")
        while True:
            print("1.Search\n2.Reserve\n3.Book list\n4.Log out\n")
            try:
                choice=int(input("Enter choice:"))
            except Exception:
                print("Invalid choice try again")
                continue
            if choice==1:
                title=input("Enter title: ")
                self.Search(title) 
            elif choice==2:
                count+=1
                if count<=2:
                    self.Reserve()
                else:
                    print("You can only reserve two books!!!")
            elif choice==3:
                self.BookList()

            elif choice==4:
                hd=input("Go for home delivery?(y/n): ")
                if hd=='y':
                    HD.verify(username)                                       
                else:
                    print("Please collect the books from library!!!\n")
                return
            else:
                print("\nInvalid choice try again\n")
home=Home()