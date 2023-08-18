'''
Title: Online library reservation system  
Author: Yadhu krishnan S 
Created on: 02/02/2023 
Last Modified Date: 25/07/2023 
Reviewed by:  
Reviewed on:
'''
import re
from model.AdminMENU import admin_Menu 
from model.Home import home 
import mysql.connector

class Access:
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

    

    def verify_username(self,username):
        select_query = "SELECT name FROM users WHERE name = %s"
        self.cursor.execute(select_query, (username,))
        row = self.cursor.fetchone()
        return row is not None
    
    def verify_login(self, username, password):
        select_query = "SELECT name FROM users WHERE name = %s AND password = %s"
        self.cursor.execute(select_query, (username, password))
        row = self.cursor.fetchone()
        return row is not None

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        if self.verify_login(username, password):
            print("Login successful!\n")
            home.Menu(username)
        else:
            print("Invalid username or password.")
            
              
    def register(self):
        while True:
            username=input("Enter user id:")
            if self.verify_username(username):
                print("Username already exists try again!!!\n")
                continue
            print("Valid username")
            new_user=username
            break
        while True:
            temp=input("Enter new password:")
            pattern = r"^(?=.*[\d])(?=.*[A-Z])(?=.*[@#$])[\w\d@#$]{6,12}$"
            if re.match(pattern, temp):
                print("Valid password")
                new_pw=temp
                break
            else:
                print("Invalid password try again!!!\n")
                print("Password should contain atleast one Upper case, one number and one special character")
        while True: 
            temp=input("Enter address:")
            if re.match(r"[A-Za-z\s]+",temp):
                new_addr=temp
                print("Valid address")
                break
            else:
                print("Invalid address try again!!!\n")    
        insert_query = "INSERT INTO users (name, password, address) VALUES (%s, %s, %s)"
        values = (new_user, new_pw, new_addr)
        self.cursor.execute(insert_query, values)
        self.connection.commit()
        print("User registered succesfully!!!\n")
        return

    def admin(self):
        count=0
        credentials = {}
        with open("C:/Users/user/OneDrive/Desktop/LMS/admin_credentials.txt", 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 2):
                username = lines[i].strip()
                password = lines[i+1].strip()
                credentials[username] = password
        while True:
            if count>=3:
                print("Too many attempts!!!\n")
                return
            choice1=input("Continue? (y/n):")
            if choice1=='n' or choice1=='n':
                return
            adminid=input("Enter admin ID: ")
            adminpass=input("Enter admin password:")
            if adminid in credentials and credentials[username] == adminpass:
                print("Valid credentials!!!\n")
                admin_Menu.mainMenu()
                break
            else:
                print("Invalid Credentials try again!!!\n")
                count+=1
object=Access()
