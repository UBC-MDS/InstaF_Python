# Copyright 2019 Betty Zhou

import numpy as np
import skimage.io

def RGB_manipulation(input_path, output_path, R = 2, G = 2, B = 2):
    '''
    Manipulates the RGB intensity of an image

    Inputs
    ------
    input_path: string, path for an image file in .png format
    output_path: string, path for the output image in .png format
    R: int, the weight to adjust intensity for red channel, all with default 2
    G: int, the weight to adjust intensity for green channel, all with default 2
    B: int, the weight to adjust intensity for blue channel, all with default 2

    Returns
    -------
    .png format image at the output path
    '''

    # Read in .png as np.array
    img = skimage.io.imread(input_path)[:,:,:3]

    # construct filter based on user input of RGB weights
    filter = np.array([[[R, G, B]]])

    # Adjust RGB intensity with filter
    output = img * filter

    # Adjust RGB intenity above 255 to 255 and ensure output is uint8 type
    output[output > 255] = 255
    output_img = output.astype(np.uint8)

    # output RGB manipulated img at output input_path
    skimage.io.imsave(output_path, output_img)
