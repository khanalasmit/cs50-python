import sys
from PIL import Image, ImageOps

def main():
    # Check for correct number of arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py <input> <output>")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # Validate file extensions
    valid_extensions = (".jpg", ".jpeg", ".png")
    if not input_path.lower().endswith(valid_extensions):
        sys.exit("Invalid input")
    if not output_path.lower().endswith(valid_extensions):
        sys.exit("Invalid output")

    # Check if input and output have the same extension
    if input_path.split(".")[-1].lower() != output_path.split(".")[-1].lower():
        sys.exit("Input and output have different extensions")

    # Try opening the input file
    try:
        input_image = Image.open(input_path)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    # Open shirt.png
    try:
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("shirt.png not found")

    # Resize and crop input image to fit the shirt
    input_image = ImageOps.fit(input_image, shirt.size, method=Image.Resampling.LANCZOS)

    # Overlay the shirt onto the input image
    input_image.paste(shirt, mask=shirt)

    # Save the output
    try:
        input_image.save(output_path)
    except Exception as e:
        sys.exit(f"Could not save output: {e}")

if __name__ == "__main__":
    main()
