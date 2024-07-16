import PIL as pil
import sys
if len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
if len(sys.argv)<3:
    sys.exit("Too few command-line arguments")
li=["png","jpg","jpeg"]
first,second=sys.argv[1].lower().split(".")
one,two=sys.argv[2].lower().split(".")
if two not in li and second not in li:
    sys.exit("Invalid input")
if two!=second:
    sys.exit("Inputs and output have different extensions")
img=pil.Image(sys.argv[2])
img.show()


