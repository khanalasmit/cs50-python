from datetime import date
import sys
import calendar
from num2words import num2words

class DateOfBirth:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth
        try:
            year, month, day = map(int, date_of_birth.split("-"))
            if not (1 <= month <= 12) or not (1 <= day <= 31):
                raise ValueError
            if day > calendar.monthrange(year, month)[1]:
                raise ValueError
            self.year = year
            self.month = month
            self.day = day
        except (ValueError, IndexError):
            sys.exit("Invalid date")

    def __str__(self):
        return self.date_of_birth

def calculate_minutes(dob):
    today = date.today()
    birth_date = date(dob.year, dob.month, dob.day)
    delta = today - birth_date
    return delta.days * 24 * 60

def main():
    dob_input = input("Date of Birth (YYYY-MM-DD): ")
    dob = DateOfBirth(dob_input)
    total_minutes = calculate_minutes(dob)
    minutes_in_words = num2words(total_minutes).replace(" and", "").lower() + " minutes"
    print(minutes_in_words.capitalize())

if __name__ == "__main__":
    main()
