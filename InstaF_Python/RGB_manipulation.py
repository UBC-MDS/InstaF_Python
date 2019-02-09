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

    Returns
    ----------

    .png format image to the output path
