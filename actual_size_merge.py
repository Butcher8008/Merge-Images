import numpy as np
from PIL import Image

def merge_images(image_filenames, output_filename, direction='horizontal'):
    # Load images
    imgs = [Image.open(i).convert('RGB') for i in image_filenames]
    
    # Find the maximum dimensions among the images
    max_width = max(i.width for i in imgs)
    max_height = max(i.height for i in imgs)
    
    # Create a blank canvas to merge images onto
    if direction == 'horizontal':
        new_img = Image.new('RGB', (max_width * len(imgs), max_height))
        offset = 0
        for img in imgs:
            new_img.paste(img, (offset, 0))
            offset += img.width
    elif direction == 'vertical':
        new_img = Image.new('RGB', (max_width, max_height * len(imgs)))
        offset = 0
        for img in imgs:
            new_img.paste(img, (0, offset))
            offset += img.height
    else:
        raise ValueError("Invalid direction. Please specify 'horizontal' or 'vertical'.")
    
    # Save the merged image
    new_img.save(output_filename)

# Prompt the user to input image filenames as a list
image_filenames = input('Enter image filenames as a list (e.g., ["image1.jpg", "image2.png"]): ')
image_filenames = eval(image_filenames)  # Convert input string to a list
print(image_filenames)
# Specify the output filename
output_filename_horizontal = 'Horizontal_merged.webp'
output_filename_vertical='vertical_merge.webp'

# Call the merge_images function
merge_images(image_filenames, output_filename_horizontal, direction='horizontal')
merge_images(image_filenames, output_filename_vertical, direction='vertical')
