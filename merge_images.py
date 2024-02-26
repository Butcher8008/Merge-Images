import numpy as np
from PIL import Image

def merge_images(image_filenames, output_filename, direction='horizontal', merging_option='expand'):
    imgs = [Image.open(i).convert('RGB') for i in image_filenames]
    
    # Find the maximum dimensions among the images
    max_width = max(i.width for i in imgs)
    max_height = max(i.height for i in imgs)
    
    if merging_option == 'expand':
        resized_imgs = [img.resize((max_width, max_height), Image.LANCZOS) for img in imgs]
        
        if direction == 'horizontal':
            imgs_comb = np.hstack([np.array(i) for i in resized_imgs])
        elif direction == 'vertical':
            imgs_comb = np.vstack([np.array(i) for i in resized_imgs])
        else:
            raise ValueError("Invalid direction. Please specify 'horizontal' or 'vertical'.")
        
        imgs_comb = Image.fromarray(imgs_comb)
        imgs_comb.save(output_filename)
    elif merging_option == 'retain size':
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
    
        new_img.save(output_filename)

# Prompt the user to enter image filenames as a list
image_filenames = input('Enter image filenames as a list (e.g., ["image1.jpg", "image2.png"]): ')
image_filenames = eval(image_filenames)

# Prompt the user to enter merge option
merging_option = input("Enter merge option (expand/retain size): ")

output_filename_horizontal = 'horizontal_merge.webp'
output_filename_vertical = 'vertical_merge.webp'

merge_images(image_filenames, output_filename_horizontal, direction='horizontal', merging_option=merging_option)
merge_images(image_filenames, output_filename_vertical, direction='vertical', merging_option=merging_option)
