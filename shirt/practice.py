from PIL import Image
import sys
im=Image.open("shirt.png")
base=Image.open("nbefore.jpg")
base.paste(im,im)
base.save("new.jpg")
