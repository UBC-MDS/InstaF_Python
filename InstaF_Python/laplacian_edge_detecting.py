import numpy as np
import skimage.io

def laplacian_edge_detecting(input_image,  output_image):
    '''
    Perform laplacian filtering on the image to get the secondary derivitive of the image matrix, based on the defined input path

    Inputs
    -----
    input_path: string, path for an image file in .png format
    output_path: string, path for the output image in .png format

    Returns
    ----------
    the current return is a matrix, which is the image matrix after filtering, just to make the test easier. In the future, the output will be an Image

    '''
    converted_matrix = plt.imread(input_image)

    return converted_matrix
