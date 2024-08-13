from PIL import Image

# Open the base image and the image to paste
shirt_img = Image.open("shirt.png")
nbefore_img = Image.open("before1.jpg")
nbefore_img.crop((0,1000,0,1000))
print(nbefore_img.size)
# Make sure both images are in the same mode
if nbefore_img.mode != shirt_img.mode:
    nbefore_img = nbefore_img.convert(shirt_img.mode)

# Optionally resize the image to paste if it's too large for the base image
if nbefore_img.size != shirt_img.size:
    nbefore_img = nbefore_img.resize(shirt_img.size)

# Ensure the image has an alpha channel for transparency
shirt_img = shirt_img.convert("RGBA")

# Create a new image with the same size as the base image
new_img = Image.new("RGBA", nbefore_img.size)

# Paste the base image onto the new image
new_img.paste(nbefore_img, (0, 0))

# Paste the overlay image onto the new image with transparency mask
new_img.paste(shirt_img, (0, 0), shirt_img)

# Save or display the result
new_img.show()  # To display the image
new_img.save("output.png")  # To save the image
