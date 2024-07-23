from PIL import Image
import sys
im=Image.open("shirt.png").convert("RGBA")
base=Image.open("nbefore.png").convert("RGBA")
im.paste(base,(0,0),base)
im.save("new.jpg")
