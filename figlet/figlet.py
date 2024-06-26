import pyfiglet
import sys
string=input("Input: ")
try:
    if len(sys.argv)>=2:
        f=pyfiglet.figlet_format(string, font=sys.argv[2])
        if sys.argv[1]=="-f":

            print(f)
        else:
            sys.exit("Invalid usage")
    else:
        f=pyfiglet.figlet_format(string)
        print(f)
except (pyfiglet.FontNotFound,IndexError):
    sys.exit("Invlaid usage")
