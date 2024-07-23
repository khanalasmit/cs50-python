from PIL import Image
import sys
im=Image.open("shirt.png")
base=Image.open("new.png")
base.paste(im,im)
base.save("new.jpg")
