from PIL import Image
img=Image.open("shirt.png")
print(img.size)
img1=Image.open("before1.jpg")
print(img1.size)
new=img1.resize(1200,1200)
new.save("nbefore1.png")
