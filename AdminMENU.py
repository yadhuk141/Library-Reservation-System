import csv
from Home import h 

class admin_menu:
    def __init__(self):
        pass

    def clr_blank(self):
        with open('temp.csv', newline='') as in_file:
            with open('Books.csv', 'a', newline='') as out_file:
                writer = csv.writer(out_file)
                for row in csv.reader(in_file):
                    if row:
                        writer.writerow(row)

    def remove_user(self):
        with open("Users.csv","r") as inp,open('temp.csv','w') as out:
            csv_inp=csv.reader(inp)
            csv.writer(out).writerows(csv_inp)
        user_name=input("Enter username to be removed: ")
        
        reader = csv.reader(open("temp.csv", "r"), delimiter=',')
        f = csv.writer(open("Users.csv", "w"))
        flag=True
        for line in reader:
            
            if user_name not in line:
                if line:
                    f.writerow(line)
            flag=False
                #print line
        if flag:
            print("User not present in database\n")
        else:
            print("User Removed\n")
        return

    def add_books(self):
        books=[]

        temp=input("Enter book title:")
        books.append(temp)
        temp=input("Enter book author:")
        books.append(temp)
        temp=input("Enter reservation status:")
        books.append(temp)

        try:
            with open('temp.csv',"w") as users:
                writer=csv.writer(users)
                writer.writerow(books)
        except Exception:
            print("An error occured, please try again\n")
            return
        else:
            self.clr_blank()
            print("\nBook added succesfully!!!\n")
            return

    def remove_books(self):
        with open("Books.csv","r") as inp,open('temp.csv','w') as out:
            csv_inp=csv.reader(inp)
            csv.writer(out).writerows(csv_inp)

        book=input("Enter title of book to be removed:")
        reader = csv.reader(open("temp.csv", "r"), delimiter=',')
        f = csv.writer(open("Books.csv", "w"))
        for line in reader:
            flag=True
            if book not in line:
                f.writerow(line)
                flag=False
                #print line
        if flag:
            print("Book not present in database\n")
        else:
            print("\nBook Removed\n")
            self.clr_blank()
        return

    def Return_books(self):
        TEXTFILE = open("temp.csv", "w")
        TEXTFILE.truncate()
        TEXTFILE.close()
        title=input("Enter title: ")
        flag=h.Search(title)
        if flag:
            print("Book does not exist in the library")
            return
        else:
            flag =True
            with open("Books.csv",'r') as books:
                with open("temp.csv","a") as temp:
                    read=csv.reader(books,delimiter=",")
                    writer = csv.writer(temp)
                    for r in read:
                        if r:
                            if r[0]==title and r[2]=="u" and flag:
                                print("The book is unreserved\n")
                                return
                            elif r[0]==title and r[2]=='r' and flag:
                                r[2]="u"
                                writer.writerow(r)
                                print("Book is returned!!!")
                                flag=False
                            else:
                                writer.writerow(r)  
                h.clr_blank()                    


    def view_users(self):
        print("\nUsername\tCity")
        print("-------------------")
        with open("Users.csv","r")as u:
            read=csv.reader(u)
            for r in read:
                if r:
                    print(r[0],"\t",r[2])
        print("\n")
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
                ch=int(input("Enter choice:"))
            except Exception:
                print("Invalid choice try again")
                continue
            if ch==1:
                self.Book_manage()
            elif ch==2:
                self.User_manage()
            elif ch==3:
                self.view_users()
            elif ch==4:
                return
            else:
                print("\nInvalid choice try again\n")
                
Admin_Menu=admin_menu() 