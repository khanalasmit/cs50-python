import pyfiglet
import sys
try:
    if len(sys.argv)>=2:
        f=pyfiglet.figlet_format(input("Input: "), font=sys.argv[2])
        if sys.argv[1]=="-f":
            print("Output:")
            print(f)
        else:
            sys.exit("Invalid usage")
    else:
        f=pyfiglet.figlet_format(string)
        print("Output: ")
        print(f)
except (pyfiglet.FontNotFound,IndexError):
    sys.exit("Invlaid usage")
