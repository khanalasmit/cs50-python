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
    with open(sys.argv[1],"r") as file:
        reader=csv.reader(file)
        for one,two,three in reader:
            break
        for first,second,third in reader:
            pizza.append({one:first,two:second,three:third})
    pizza.pop(0)
    table=tabulate.tabulate(pizza, headers="keys", tablefmt="grid")
except FileNotFoundError:
    sys.exit("File does not exists")
print(table)
