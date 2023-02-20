import datetime

def from_dob_to_age(born):
        today = datetime.date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))



year=int(input("Enter year: "))
month=int(input("Enter month: "))
day=int(input("Enter day: "))
dob = datetime.date(year,month,day)
print(from_dob_to_age(dob))