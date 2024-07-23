from PIL import Image
im=Image.open("nbefore.png")
cropped=im.crop((0,0,im.width,im.height-80))
cropped.save("new.png")
