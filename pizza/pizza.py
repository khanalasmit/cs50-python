import sys
import tabulate
import csv
pizza=[]
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if len(sys.argv)<2:
    sys.exit("Too few command-line arguments")
if ".csv" not in sys.argv[1]:
    sys.exit("Not a CSV file")
try:
    with open(sys.argv[1], "r") as file:
        reader = csv.reader(file)
        headers = next(reader)  # Read the first row as headers
        for row in reader:
            if row:  # Avoid processing empty rows
                pizza.append(row)
    table = tabulate.tabulate(pizza, headers="keys", tablefmt="grid")
    print(table)
except FileNotFoundError:
    sys.exit("File does not exists")
