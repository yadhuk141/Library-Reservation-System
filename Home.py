import csv
from Hdelivery import HD
from AdminMENU import admin_Menu as am
import mysql.connector
from tabulate import tabulate

class Home:
       
    def Search(self,title):
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="yadhuafr141",
            database="library"
        )
        cursor = conn.cursor()
        select_query = "SELECT reservation FROM books WHERE title = %s"
        cursor.execute(select_query, (title,))
        rows = cursor.fetchall()
        if rows:
            print("Reservation status for book", title, ":")
            print(rows[0][0])
            print("\n")
        else:
            print("Book not found\n")
        cursor.close()
        conn.close()


    def Reserve(self):
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="yadhuafr141",
            database="library"
        )
        cursor = conn.cursor()
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
                conn.commit()
                print("Reserved successfully\n")
            elif reserve_value == "Yes":
                print("Book is already reserved\n")
        return

    
    def BookList(self):
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="yadhuafr141",
            database="library"
        )
        cursor = conn.cursor()
        select_query = "SELECT * FROM books"
        cursor.execute(select_query)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        print(tabulate(rows, headers=columns, tablefmt="psql"))
        print("\n")
        cursor.close()
        conn.close()
        return


    def Menu(self,username):
        count=0
        print("Please select required operation\n")
        while True:
            print("1.Search\n2.Reserve\n3.Book list\n4.Log out\n")
            try:
                ch=int(input("Enter choice:"))
            except Exception:
                print("Invalid choice try again")
                continue
            if ch==1:
                title=input("Enter title: ")
                self.Search(title) 
            elif ch==2:
                count+=1
                if count<=2:
                    self.Reserve()
                else:
                    print("You can only reserve two books!!!")
            elif ch==3:
                self.BookList()

            elif ch==4:
                hd=input("Go for home delivery?(y/n): ")
                if hd=='y':
                    HD.verify(username)                                       
                else:
                    print("Please collect the books from library!!!\n")
                return
            else:
                print("\nInvalid choice try again\n")
h=Home()