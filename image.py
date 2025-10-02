import os
from PIL import Image
input_folder="images"
output_folder="resize_images"

os.makedirs(output_folder, exist_ok=True)
new_size=(350,350)
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".webp")):
        image_path=os.path.join(input_folder,filename)
        image=Image.open(image_path)
        image_resize=image.resize(new_size)
        new_filename = os.path.splitext(filename)[0] + ".jpg"
        save_path = os.path.join(output_folder, new_filename)

        image_resize.save(save_path, "JPEG")
        print(f"Resized & saved: {save_path}")

print("\n All images have been resized and saved in 'resized_images' folder!")
