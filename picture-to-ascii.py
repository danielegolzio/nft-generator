from PIL import Image, ImageDraw, ImageFont

img = Image.open("duck-1.png")
width, height = img.state
pixel = img.load()

for i in range(height):
    for j in range(width):
        r, g, b = pixel[j, i]
        print(r)


