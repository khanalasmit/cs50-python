from PIL import Image
import sys
im=Image.open("shirt.png")
base=Image.open("nbefore.jpg")
im.paste(base,base)
im.save("new.jpg")
