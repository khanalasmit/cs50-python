import pyfiglet
import sys
try:
    if len(sys.argv)>=2:
        f=pyfiglet.Figlet(font=sys.argv[2])
        if sys.argv[1]=="-f":
            string=input("Input: ")
            print("Output:")
            print(f.renderText(string))
        else:
            sys.exit("Invalid usage")
    else:
        f=pyfiglet.figlet_format(input("Input: "))
        print("Output: ")
        print(f)
except (pyfiglet.FontNotFound,IndexError):
    sys.exit("Invlaid usage")
