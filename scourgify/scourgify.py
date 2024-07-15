import csv
import tabulate
import sys
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if len(sys.argv)<3:
    sys.exit("Too few command-line arguments")
if ".csv" not in sys.argv[1] and ".csv" not in sys.argv[2]:
    sys.exit("Not a CSV file")
students=[]
try:
    with open(sys.argv[1],"r") as file:
        reader=csv.DictReader(file)
        for row in reader:
            students.append(row)
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
try:
    with open(sys.argv[2],"a") as fp:
        writer=csv.DictWriter(fp,fieldnames=['first','last','house'])
        for row in students:
            one,two=row["name"].split(",")
            pupil=({"first":one,"second":two,"house":row["house"]})
            writer.writeheader()
            writer.writerow(pupil)
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[2]}")
