import pyfiglet
import sys
string=input("Input: ")
try:
    f=pyfiglet.figlet_format(string, font=sys.argv[2])
    if sys.argv[1]=="-f":

        print(f)
    else:
        sys.exit("Invalid usage")
except pyfiglet.FontNotFound:
    sys.exit("Invlaid usage")
