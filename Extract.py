from PIL import Image
import numpy as np

"""
Here there are four functions.

extract_rgb_matrix takes an image in colour and gives three matrix with the intensities of red, green and blue.
combine_rgb_matrix takes three matrix with the colour intensities and gives an image.
extract_intensities takes an image and gives a matrix with the intensity of each pixel.
create_image_from_intensity takes a matrix with the intensity of each pixel and gives an image in black and white
"""

def extract_rgb_matrix(image_path):
    # Load the image
    img = Image.open(image_path)
    
    # Convert the image in an array
    img_array = np.array(img)

    # Extract red, green and blue
    R = img_array[:,:,0]  # Canal rojo
    G = img_array[:,:,1]  # Canal verde
    B = img_array[:,:,2]  # Canal azul
    
    return R, G, B

def combine_rgb_matrix(R, G, B):
    # Verify that the three matrix have the same shape
    if R.shape != G.shape or R.shape != B.shape:
        raise ValueError("R ,G and B need to have the same shape.")
    
    # Combine the three matrix in one array
    img_array = np.stack((R, G, B), axis=-1)
    
    # Convert the array to uint8
    img_array = img_array.astype(np.uint8)
    
    # Create the image
    img = Image.fromarray(img_array)
    
    return img


def extract_intensities(image_path):
    # Load the image in black and white
    img = Image.open(image_path).convert('L')  # 'L' to have the intensity like an image in black and white
    
    # Convert the image in an array
    intensity_array = np.array(img)

    return intensity_array

def create_image_from_intensity(intensity_array):
    # Convert the matrix to uint8
    intensity_array = intensity_array.astype(np.uint8)
    
    # Create an image from an array
    img = Image.fromarray(intensity_array, mode='L') # 'L' to have the intensity like an image in black and white
    
    return img


