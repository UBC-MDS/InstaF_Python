# Copyright 2019 Betty Zhou

import numpy as np
import skimage.io

def RGB_manipulation(input_path, output_path, R = 1.5, G = 1.5, B = 1.5):
    '''
    Manipulates the RGB intensity of an image
    Inputs
    -----
    input_path: string, path for an image file in .png format
    output_path: string, path for the output image in .png format
    R, G, B: float, the weights we want to adjust for each channel, all with default 1.5

    Returns
    ----------

    .png format image to the output path
    '''
    converted_matrix = plt.imread(input_path)

    return converted_matrix
