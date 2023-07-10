'''
Title: Online library reservation system  
Author: Yadhu krishnan S 
Created on: 02/02/2023 
Last Modified Date: 22/02/2023 
Reviewed by:  
Reviewed on:
'''
import csv
import re
from AdminMENU import admin_Menu as am
from Home import h 
import mysql.connector

class Access:
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
            h.Menu()
        else:
            self.login_attempts += 1
            print("Invalid username or password.")
            if self.login_attempts >= 3:
                print("Maximum login attempts reached. Exiting the program.")
                exit()
              
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
        self.conn.commit()
        print("User registered succesfully!!!\n")
        return

    def admin(self):
        count=0
        admin="admin"
        password="12345"
        while True:
            if count>=3:
                print("Too many attempts!!!\n")
                return
            ch=input("Continue? (y/n):")
            if ch=='n' or ch=='n':
                return
            adminid=input("Enter admin ID: ")
            adminpass=input("Enter admin password:")
            if admin==adminid and password==adminpass:
                print("Valid credentials!!!\n")
                am.mainMenu()
                break
            else:
                print("Invalid Credentials try again!!!\n")
                count+=1
                

#MAIN
obj=Access()
flag=True
print("----------------Welcome-----------------")
while flag:
    print("\n1.Login\n2.Register\n3.Admin Login\n4.Exit\n")
    try:
        ch=int(input("Enter choice:"))
    except Exception:
        print("Invalid choice try again")
        continue
    if ch==1:
        obj.login()
    elif ch==2:
        obj.register()
    elif ch==3:
        obj.admin()
    elif ch==4:
        flag=False
    else:
        print("\nInvalid choice try again\n")