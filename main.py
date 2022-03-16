from hashlib import new
from turtle import width
from PIL import Image
from matplotlib import widgets
image_path = "isim.png"
img = Image.open(image_path)

width, height = img.size
aspect_ratio = width/height
new_width = 120
new_height = aspect_ratio * new_width * 0.48
img = img.resize((new_width, int(new_height)))

img = img.convert('L')

pixels =  img.getdata()

chars = ["B", "S", "#", "$", "%", "@", "&", "*", "!", ":", "."]
new_pixels = [chars[pixel//25] for pixel in pixels]
new_pixels = ''.join(new_pixels)

new_pixels_count = len(new_pixels)
ascii_image = [new_pixels[index:index + new_width]
for index in range (0, new_pixels_count, new_width)]
ascii_image = "\n".join(ascii_image)

txt_path = "cikti.txt"
with open("cikan.txt", "w") as f:
    f.write(ascii_image)