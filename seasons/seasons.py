from datetime import date
import sys
from num2words import num2words


class DateOfBirth:
    def __init__(self, date_of_birth):
        try:
            year, month, day = map(int, date_of_birth.split("-"))
            self.birth_date = date(year, month, day)
        except (ValueError, IndexError):
            sys.exit("Invalid date")

    def __str__(self):
        return self.birth_date.isoformat()


def calculate_minutes(dob):
    """Calculate the total minutes from the date of birth to today."""
    today = date.today()
    delta = today - dob.birth_date
    return delta.days * 24 * 60  # Convert days to minutes


def main():
    dob_input = input("Date of Birth (YYYY-MM-DD): ")
    dob = DateOfBirth(dob_input)
    total_minutes = calculate_minutes(dob)
    minutes_in_words = (
        num2words(total_minutes, to="number").replace(" and", "").lower() + " minutes"
    )
    print(minutes_in_words.capitalize())


if __name__ == "__main__":
    main()
