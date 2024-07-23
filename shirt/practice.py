from PIL import Image
import sys
im=Image.open("shirt.png")
base=Image.open("nbefore.png")
base.paste(im,(0,0),im)
base.save("new.jpg")
