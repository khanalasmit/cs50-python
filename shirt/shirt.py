from PIL import Image
import sys
if len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
if len(sys.argv)<3:
    sys.exit("Too few command-line arguments")
li=["png","jpg","jpeg"]
first,second=sys.argv[1].lower().split(".")
one,two=sys.argv[2].lower().split(".")
if two not in li and second not in li:o
    sys.exit("Invalid input")
if two!=second:
    sys.exit("Inputs and output have different extensions")
img=Image.open(sys.argv[2])
img.show()


