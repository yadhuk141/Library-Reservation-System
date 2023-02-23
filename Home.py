import csv
from Hdelivery import HD
from random import randrange
from AdminMENU import admin_Menu as am
class Home:


    def Report(self,reserved,userid):
        print("\n")
        print("RESERVATION REPORT")
        for i in reserved:
            print("Title: ",i[0])
            print("Author: ",i[1])
            print("--------------")
       


    def Search(self,title):
        flag=True 
        """ with open('Books.csv',"r") as books:
            read=csv.reader(books,delimiter=",") """

        for r in am.books:
            if r[0]==title:
                print("Book found!!\n")
                print("TITLE: ",r[0])
                print("AUTHOR: ",r[1])
                if r[2]=='r':
                    print("STATUS: RESERVED\n")
                else:
                    print("STATUS: UNRESERVED\n")
                flag =False
                return flag
        return flag
           

    def Reserve(self,userid):
        """ TEXTFILE = open("temp.csv", "w")
        TEXTFILE.truncate()
        TEXTFILE.close() """
        
        reserved=[]    
        title=input("Enter title: ")
        flag=self.Search(title)
        if flag:
            print("Book does not exist in the library")
            return
        else:
            """ with open("Books.csv",'r') as books:
                with open("temp.csv","a") as temp:
                    read=csv.reader(books,delimiter=",")
                    writer = csv.writer(temp) """

            for r in am.books:
                if r[0]==title and r[2]=="r":
                    print("The book is already reserved!")
                    return
                elif r[0]==title and r[2]=='u':
                    r[2]='r'
                    #writer.writerow(r)
                    print("Book is Reserved!!!!")
                    reserved.append(r)
                    
                """ else:
                    if r:
                        writer.writerow(r) """      

        self.Report(reserved,userid)
        #self.clr_blank()
        return
    def BookList(self):
        """ with open("Books.csv",'r') as books:
            read=csv.reader(books,delimiter=",") """
        for i in am.books:
            print("Book title:",i[0])
            print("Author: ",i[1])
            print("\n")
        print("---------------------------------\n")
        return




    def Menu(self,userid):
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
                flag=self.Search(title) 
                if flag:
                    print("Book not found")
            elif ch==2:
                count+=1
                if count<=2:
                    self.Reserve(userid)
                else:
                    print("You can only reserve two books!!!")
            elif ch==3:
                self.BookList()

            elif ch==4:
                hd=input("Go for home delivery?(y/n): ")
                if hd=='y':
                    HD.verify(userid)                                       
                else:
                    print("Please collect the books from library!!!\n")
                print("\nUse the otp to confirm order at the library or with the delivery personnel:")
                print(randrange(1000,10000),"\n")
                return
            else:
                print("\nInvalid choice try again\n")
h=Home()