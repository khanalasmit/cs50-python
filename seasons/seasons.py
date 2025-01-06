from datetime import date, datetime
import inflect
import sys

class AgeInMinutes:
    def __init__(self, dob):
        try:

            self.dob = datetime.strptime(dob, "%Y-%m-%d").date()
        except ValueError:
            print("Error: Invalid date format. Please enter the date in 'YYYY-MM-DD' format.")
            sys.exit(1)

        self.today = date.today()
        self.p = inflect.engine()

    def calculate_age_in_minutes(self):

        delta = self.today - self.dob
        age_in_minutes = delta.total_seconds() // 60

        words = self.p.number_to_words(int(age_in_minutes), andword=" ")


        return words
    def __str__(self):
        return f"{self.calculate_age_in_minutes()}"

def main():
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    age_in_minutes = AgeInMinutes(dob)
    age_in_minutes_ = str(age_in_minutes).capitalize()
    print(f"{age_in_minutes_} minutes" )

if __name__ == "__main__":
    main()
