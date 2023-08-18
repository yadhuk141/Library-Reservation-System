'''
Title: Online library reservation system  
Author: Yadhu krishnan S 
Created on: 02/02/2023 
Last Modified Date: 25/07/2023 
Reviewed by:  
Reviewed on:
'''

import sys
sys.path.append('C:/Users/user/OneDrive/Desktop/LMS/src')
from model.LoginPage import object
flag=True
print("----------------Welcome-----------------")
while flag:
    print("\n1.Login\n2.Register\n3.Admin Login\n4.Exit\n")
    try:
        choice=int(input("Enter choice:"))
    except Exception:
        print("Invalid choice try again")
        continue
    if choice==1:
        object.login()
    elif choice==2:
        object.register()
    elif choice==3:
        object.admin()
    elif choice==4:
        flag=False
    else:
        print("\nInvalid choice try again\n")