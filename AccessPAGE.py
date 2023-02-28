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
import getpass

class Access:

    def login(self):
        count=0
        while True:
            flag=True
            if count>=3:
                print("Too many attempts!")
                return
            ch=input("Continue Log in? (y/n):")
            if ch!="y":
                return
            userid=input("Enter username: ")
            pw=getpass.getpass(prompt="Enter password: ")
            with open('Users.csv',"r") as users:
                read=csv.reader(users,delimiter=",")
                for r in read:
                    try:
                        if r[0]==userid and r[1]==pw:
                            print("Valid credentials!!!\n")
                            flag=False
                            h.Menu(r[0])
                            break
                    except:
                        continue
            if flag:
                print("Incorrect username or password!!!")
                count+=1
                print("TRY AGAIN!!!\n")

    def clr_blank(self):
        with open('temp.csv', newline='') as in_file:
            with open('Users.csv', 'a', newline='') as out_file:
                writer = csv.writer(out_file)
                for row in csv.reader(in_file):
                    if row:
                        writer.writerow(row)                
                        
    def verify(self,u):
        with open('Users.csv','r') as f:
            read=csv.reader(f,delimiter=",")
            for i in read:
                if i:
                    if i[0]==u:
                        return True

    def register(self):
        new_user=[]
        while True:
            temp=input("Enter user id(The username should be globally unique!!!):")
            if re.match(r"[A-Za-z\s]+",temp):
                check=self.verify(temp)
                if check:
                    print("Username already exists try again!!!\n")
                    continue
                print("Valid username")
                new_user.append(temp)
                break
            else:
                print("Invalid username try again!!!\n")
        while True:
            temp=input("Enter new password: ")
            if re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{6,12}$", temp):
                print("Valid password")
                new_user.append(temp)
                break
            else:
                print("Invalid password try again!!!\n")
                print("Password should contain atleast one Upper case, one number and one special character")
        while True: 
            temp=input("Enter address:")
            if re.match(r"[A-Za-z\s]+",temp):
                new_user.append(temp)
                print("Valid address")
                break
            else:
                print("Invalid address try again!!!\n")
        try:
            with open('temp.csv',"w") as users:
                writer=csv.writer(users)
                writer.writerow(new_user)
        except Exception:
            print("An error occured, please try again\n")
            return
        else:
            self.clr_blank()
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