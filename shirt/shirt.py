import PIL as pil
import sys
if len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
if len(sys.argv)<3:
    sys.exit("Too few command-line arguments")
li=["png","jpg","jpeg"]
first,second=sys.argv[2].split(".").lower()
one,two=sys.argv[3].split(".").lower()
if two not in li and second not in li:
    sys.exit("")


