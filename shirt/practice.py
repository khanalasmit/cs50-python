from PIL import Image
im=Image.open("nbefore.png")
cropped_image=im.crop((0,0,0,20))
cropped_image.save("nnbefore.png")
