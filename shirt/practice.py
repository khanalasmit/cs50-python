from PIL import Image
im=Image.open("nbefore.png")
cropped_image=im.crop((600,600,600,580))
cropped_image.save("nnbefore.png")
