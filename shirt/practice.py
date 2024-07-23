from PIL import Image
import sys
im=Image.open("shirt.png")
base=Image.open("nbefore.jpg")
im.paste(base,(0,0),base)
im.save("new.jpg")
