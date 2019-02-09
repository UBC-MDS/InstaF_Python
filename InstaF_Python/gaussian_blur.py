import numpy as np
import skimage.io

def gaussian_blur(input_image, output_image, sigma = 1):
    '''
    Perform gaussian blur on the image based on the defined input path

    Inputs
    -----
    input_image: string, path to an image file in .png format
    output_image: string, path to an image file in .png format
    sigma: int, standard deviation of the gaussian distribution that we will use to construct the filter, default values to be 1

    Returns
    ----------
    the current return is a matrix, which is the image matrix after filtering, just to make the test easier. In the future, the output will be an Image

    '''
    converted_matrix = plt.imread(input_image)

    return converted_matrix
