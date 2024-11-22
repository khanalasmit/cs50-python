from datetime import date
import sys
import calendar
from num2words import num2words

class Validation:
    def __init__(self, dateofbirth):
        self.dateofbirth = dateofbirth
        if "-" not in dateofbirth:
            sys.exit("Invalid date")
        year, month, day = dateofbirth.strip().split("-")
        if not year.isdigit() or not month.isdigit() or not day.isdigit():
            sys.exit("Invalid date")
        if len(year) != 4 or len(month) != 2 or len(day) != 2:
            sys.exit("Invalid date")

        # Fix logical error in validation
        if int(month) > 12 or int(month) < 1 or int(day) > 31 or int(day) < 1:
            sys.exit("Invalid date")

        # Validate the day against the month
        if int(day) > calendar.monthrange(int(year), int(month))[1]:
            sys.exit("Invalid date")

    def __str__(self):
        return self.dateofbirth

def main():
    dateofbirth = DOB()
    today = date.today()
    year, month, day = dateofbirth.dateofbirth.strip().split("-")
    year, month, day = int(year), int(month), int(day)

    total_min = 0
    age = today.year

    # Calculate total minutes from years between birth year and current year
    for i in range(year + 1, age):
        if calendar.isleap(i):
            total_min += 366 * 24 * 60
        else:
            total_min += 365 * 24 * 60

    # Calculate remaining minutes from the birth year
    days_in_birth_year = 0
    for i in range(month, 13):
        days_in_birth_year += calendar.monthrange(year, i)[1]
    days_in_birth_year -= day
    total_min += days_in_birth_year * 24 * 60

    # Calculate minutes for the current year up to today
    days_in_current_year = 0
    for i in range(1, today.month):
        days_in_current_year += calendar.monthrange(age, i)[1]
    total_min += days_in_current_year * 24 * 60

    in_word=num2words(total_min).replace(" and","")
    in_word=in_word+" minutes"
    print(in_word.capitalize())



def DOB():
    dateofbirth = input("Date of Birth: ")
    return Validation(dateofbirth)

main()
