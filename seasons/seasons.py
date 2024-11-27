from datetime import date
import sys
from num2words import num2words  # To convert numbers to words

def main():
    birth_date = get_birth_date()
    minutes = calculate_minutes(birth_date)
    minutes_in_words = convert_to_words(minutes)
    print(minutes_in_words)

def get_birth_date():
    try:
        birth_date_str = input("Enter your birth date (YYYY-MM-DD): ").strip()
        year, month, day = map(int, birth_date_str.split("-"))
        return date(year, month, day)
    except ValueError:
        sys.exit("Invalid date format. Please enter the date in YYYY-MM-DD format.")

def calculate_minutes(birth_date):
    today = date.today()
    delta = today - birth_date
    return round(delta.total_seconds() / 60)

def convert_to_words(number):
    return num2words(number, to="cardinal", lang="en").replace(",", "").replace("-", " ")

if __name__ == "__main__":
    main()
