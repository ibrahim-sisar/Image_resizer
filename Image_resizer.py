from PIL import Image
import sys
import os


SUPPORTED_EXTENSIONS = Image.registered_extensions().keys()

def is_image(file_path):
    return file_path.lower().endswith(tuple(SUPPORTED_EXTENSIONS))

argc = len(sys.argv)
argv=sys.argv

if argc != 5:
    print("Usage: python resize_images.py <directory_path> <output_directory> <image_h> <image_w>")
    sys.exit(1)

directory_path = argv[1]

if not os.path.exists(directory_path):
    print(f"Directory '{directory_path}' does not exist.")
    sys.exit(1)

output_directory = argv[2]

if not os.path.exists(output_directory):
    os.makedirs(output_directory)
    print(f"Created directory '{output_directory}'")

    if not os.path.isdir(output_directory):
        print(f"Error creating directory '{output_directory}'.")
        sys.exit(1)

image_height = int(argv[3])

if image_height <= 0:
    print("Invalid image height. It must be a positive integer.")
    sys.exit(1)

image_width = int(argv[4])

if image_width <= 0:
    print("Invalid image width. It must be a positive integer.")
    sys.exit(1)

for filename in os.listdir(directory_path):
    if is_image(filename):
        image_path = os.path.join(directory_path, filename)
        output_path = os.path.join(output_directory, os.path.splitext(filename)[0] + "_resized_" + str(image_height) + "x" + str(image_width) + os.path.splitext(filename)[1])
        image = Image.open(image_path)
        resized_image = image.resize((image_width, image_height))
        resized_image.save(output_path)
        print(f"Resized '{image_path}' to '{output_path}'")
        

