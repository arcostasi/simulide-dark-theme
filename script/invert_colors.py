from PIL import Image, ImageOps
import os

def invert_image_color(image_path, output_path):
    # Load the image
    img = Image.open(image_path)

    # Convert the image to RGBA if not already
    if img.mode != 'RGBA':
        img = img.convert('RGBA')

    # Invert the colors, preserving transparency
    r, g, b, a = img.split()
    rgb_image = Image.merge('RGB', (r, g, b))

    inverted_image = ImageOps.invert(rgb_image)

    r, g, b = inverted_image.split()
    inverted_image = Image.merge('RGBA', (r, g, b, a))

    # Save the inverted image
    inverted_image.save(output_path)

def invert_colors_in_directory(directory_path, output_directory):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # List all PNG files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith('.png'):
            # Full path of the original file and the output file
            original_path = os.path.join(directory_path, filename)
            output_path = os.path.join(output_directory, filename)

            # Invert the colors of the image
            invert_image_color(original_path, output_path)
            print(f"Image processed: {filename}")

# Path of the input and output directory
input_directory = 'C:\\Temp\\images'
output_directory = 'C:\\Temp\\images2'

# Process all PNG files in the directory
invert_colors_in_directory(input_directory, output_directory)
