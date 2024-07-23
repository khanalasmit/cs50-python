from PIL import Image
import sys
for argument in sys.argv[1:]:
    image=Image.open(argument)
    size=image.size
    print(size)

