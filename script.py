# from PIL import Image
# import os

# def crop_images_in_directory(input_directory, output_directory, crop_area, quality=40):
#     # Create the output directory if it doesn't exist
#     if not os.path.exists(output_directory):
#         os.makedirs(output_directory)

#     # Iterate through all files in the input directory
#     for filename in os.listdir(input_directory):
#         if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
#             input_image_path = os.path.join(input_directory, filename)
#             output_image_path = os.path.join(output_directory, filename)

#             # Open the image
#             img = Image.open(input_image_path)

#             # Crop the image based on the crop_area tuple (x1, y1, x2, y2)
#             cropped_img = img.crop(crop_area)

#             # Save the cropped image with 70% quality
#             cropped_img.save(output_image_path, quality=quality)
#             print(f"Image '{filename}' cropped and saved to {output_image_path} with {quality}% quality")

# # Define the input directory containing images to be cropped
# input_directory = 'input_images/'

# # Define the output directory to save cropped images
# output_directory = 'output_images/'

# # Define the coordinates for cropping in the format (x1, y1, x2, y2)
# # Replace these values with the desired coordinates
# crop_area_coordinates = (233, 130, 969, 713)

# # Crop all images in the input directory using the same coordinates and 70% quality
# crop_images_in_directory(input_directory, output_directory, crop_area_coordinates, quality=40)
from PIL import Image
import os

def crop_images_in_directory(input_directory, output_directory, crop_area, quality=70):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Iterate through all files in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
            input_image_path = os.path.join(input_directory, filename)
            output_image_path = os.path.join(output_directory, os.path.splitext(filename)[0] + '.jpg')

            # Open the image
            img = Image.open(input_image_path)

            # Convert image to RGB mode if it's RGBA
            if img.mode == 'RGBA':
                img = img.convert('RGB')

            # Crop the image based on the crop_area tuple (x1, y1, x2, y2)
            cropped_img = img.crop(crop_area)

            # Save the cropped image as .jpg with 70% quality
            cropped_img.save(output_image_path, quality=quality)
            print(f"Image '{filename}' cropped and saved to {output_image_path} with {quality}% quality")

# Define the input directory containing images to be cropped
input_directory = 'input_images/'

# Define the output directory to save cropped images
output_directory = 'output_images/'

# Define the coordinates for cropping in the format (x1, y1, x2, y2)
# Replace these values with the desired coordinates
# crop_area_coordinates = (233, 130, 969, 713)
crop_area_coordinates = (553,380,2012,1564)

# Crop all images in the input directory using the same coordinates and save as .jpg with 70% quality
crop_images_in_directory(input_directory, output_directory, crop_area_coordinates, quality=70)
