from PIL import Image
import sys
im=Image.open("before1.jpg")
im_n=im.resize((600,600))
im_n.save("nbefore.jpg")


