import pyfiglet
import sys
string=input("Input: ")
try:
    f=pyfiglet.figlet_format(string, font=sys.argv[2])
    print(f)
except pyfiglet.FontNotFound:
    print("Invalid usage")
