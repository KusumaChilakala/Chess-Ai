import os
from PIL import Image

input_folder = "images/"
output_folder = "processed_images/"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(".png"):
        img = Image.open(os.path.join(input_folder, filename))
        img = img.resize((64, 64))  # Resize to 64x64 pixels
        img.save(os.path.join(output_folder, filename))

print("Image conversion complete!")
