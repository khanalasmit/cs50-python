from datetime import date
import sys
import calendar
from num2words import num2words
class Validation:
    def __init__(self, dateofbirth):
        self.dateofbirth = dateofbirth
        if "-" not in dateofbirth:
            sys.exit("Invalid date")
        year,month,day=dateofbirth.strip().split("-")
        if not year.isdigit() or not month.isdigit() or not day.isdigit():
            sys.exit("Invalid date")
        if len(year)!=4 or len(month)!=2 or len(day)!=2:
            sys.exit("Invalid date")
        if int(month)>12 or int(month)<1 and int(day)>31 or int(day)<1:
            sys.exit("Invalid date")




    def __str__(self):
        return self.dateofbirth

def main():
    dateofbirth=DOB()
    today=date.today()
    year,month,day=dateofbirth.dateofbirth.strip().split("-")
    age=today.year
    total_min=0
    for i in range(int(year)+1,age):
        if calendar.isleap(i):
            total_min+=366*24*60
        else:
            total_min+=365*24*60
    days=[]
    for i in range(int(month),13):
        days.append(calendar.monthrange(int(year),i)[1])
    for i in range(0,len(days)):
        if i==0:
            total_min+=days[i]*24*60-int(day)*24*60
        else:
            total_min+=days[i]*24*60
    days2=[]
    for i in range(today.month,13):
        days2.append(calendar.monthrange(age,i)[1])
    for i in range(0,len(days2)):
        if i==0:
            total_min+=days2[i]*24*60-int(today.day)*24*60
        else:
            total_min+=days2[i]*24*60

    print(num2words(total_min))





def DOB():
    dateofbirth = input("Date of Birth: ")
    return Validation(dateofbirth)
main()
