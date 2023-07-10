import csv
import mysql.connector
from random import randrange
class Hd:
    def __init__(self) -> None:
        try:
            self.conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="yadhuafr141",
                database="library"
            )
        except Exception:
            print("Error with database connection")
            return
        else:
            self.cursor = self.conn.cursor() 

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def verify(self,username):
        select_query = "SELECT address FROM users WHERE username = %s"
        self.cursor.execute(select_query, (username,))
        row = self.cursor.fetchone()
        if row is not None:
            address = row[0]
            if address.lower() == "chennai" or address.lower() == "siruseri":
                print("Home delivery is available in your location!!!")
                print("A delivery fee of Rs.30 will be charged!!!")
            else:
                print("Home delivery is not available in your location.")
                print("Please visit the nearest library to collect reserved books\n")
                print("\nUse the otp to confirm order at the library or with the delivery personnel:")
                print(randrange(1000,10000),"\n")
        else:
            print("User not found.")
HD=Hd()
