import mysql.connector
from random import randrange
class Hd:
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
            
    def verify(self,username):
        select_query = "SELECT address FROM users WHERE name = %s"
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
