import sys
import tabulate
import csv

# Check for correct number of command-line arguments
if len(sys.argv) != 2:
    sys.exit("Usage: python pizza.py <filename>.csv")

# Check if the provided file is a CSV file
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

pizza = []

try:
    with open(sys.argv[1], "r") as file:
        reader = csv.reader(file)
        headers = next(reader)  # Read the first row as headers
        for row in reader:
            if row:  # Avoid processing empty rows
                pizza.append(dict(zip(headers, row)))

    if not pizza:
        sys.exit("No data in CSV file")

    table = tabulate.tabulate(pizza, headers="keys", tablefmt="grid")
    print(table)
except FileNotFoundError:
    sys.exit("File does not exist")
except csv.Error:
    sys.exit("Error reading CSV file")
