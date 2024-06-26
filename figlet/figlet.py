import pyfiglet
import sys
string=input("Input: ")
try:
    if(sys.argv[1]=="-f"):
        f=pyfiglet.figlet_format(string, font=sys.argv[2])
        print(f)
    else:
        sys.exit("Invalid usage")
except pyfiglet.FontNotFound:
    sys.exit("Invlaid usage")
