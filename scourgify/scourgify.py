import csv
import sys

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

students = []
try:
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

try:
    with open(sys.argv[2], "w") as fp:
        writer = csv.DictWriter(fp, fieldnames=['first', 'last', 'house'])
        writer.writeheader()  # Write header outside the loop
        for row in students:
            one, two = row["name"].split(", ")
            pupil = {"first": two.strip(), "last": one.strip(), "house": row["house"]}
            writer.writerow(pupil)
except Exception as e:
    sys.exit(f"An error occurred: {e}")
