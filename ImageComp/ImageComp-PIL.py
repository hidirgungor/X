from PIL import Image

# Open the image
image = Image.open("original.jpg")

# Set the compression level (0-100)
image.save("compressed.jpg", quality=50)
