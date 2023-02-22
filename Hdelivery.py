import csv


class Hd:
    def verify(self,userid):
        cities=['chennai','siruseri']
        flag=True
        with open("Users.csv","r") as inp:
            read=csv.reader(inp)
            for r in read:
                if r:
                    print(r[0])
                    if r[0]==userid:
                        if r[2] in cities:
                            print("Home delivery is available in your location!!!")
                            print("A delivery fee of Rs.30 will be charged!!!")
                            flag=False
                            return
        if flag:
            print("Home delivery option is not present at your location!!!\n")
            print("Please visit the nearest library to collect reserved books\n")
            return
HD=Hd()
