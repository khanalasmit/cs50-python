from PIL import Image
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
shirt_img = Image.open(sys.argv[1])
nbefore_img = Image.open(sys.argv[2])

# Make sure both images are in the same mode
if nbefore_img.mode != shirt_img.mode:
    nbefore_img = nbefore_img.convert(shirt_img.mode)

# Optionally resize the image to paste if it's too large for the base image
if nbefore_img.size != shirt_img.size:
    nbefore_img = nbefore_img.resize(shirt_img.size)

# Ensure the image has an alpha channel for transparency
shirt_img = shirt_img.convert("RGBA")

# Create a new image with the same size as the base image
new_img = Image.new("RGBA", nbefore_img.size)

# Paste the base image onto the new image
new_img.paste(nbefore_img, (0, 0))

# Paste the overlay image onto the new image with transparency mask
new_img.paste(shirt_img, (0, 0), shirt_img)

new_img.save("output.png")  # To save the image


