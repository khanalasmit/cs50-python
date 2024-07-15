import csv
import tabulate
import sys
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if len(sys.argv)<3:
    sys.exit("Too few command-line arguments")
if ".csv" not in sys.argv[1]:
    sys.exit("Not a CSV file")
students=[]
try:
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

# Try to write to the output CSV file
try:
    with open(sys.argv[2], "w", newline='') as fp:
        writer = csv.DictWriter(fp, fieldnames=['first', 'last', 'house'])
        writer.writeheader()
        for row in students:
            last, first = row["name"].split(",")
            pupil = {"first": first.strip(), "last": last.strip(), "house": row["house"]}
            writer.writerow(pupil)
except Exception as e:
    sys.exit(f"Could not write to {sys.argv[2]}")
