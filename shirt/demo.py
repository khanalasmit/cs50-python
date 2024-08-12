from PIL import Image
img=Image.open("shirt.png")
img1=Image.open("before1.jpg")
new=img1.resize(img.size)
print(new.size)
new.save("nbefore1.png")
if img.mode!=new.mode:
    img=img.convert(new.mode)
new.paste(new,(0,0),img)
new.save("final.png")

