# Copyright 2019 Betty Zhou
# This script contains tests for the RGB_manipulation function

# RGB_manipulation(input_path, output_path, R = 2, G = 2, B = 2)
# input_path: string, path for an image file in .png format
# output_path: string, path for the output image in .png format
# R: int, the weight to adjust intensity for red channel, all with default 2
# G: int, the weight to adjust intensity for green channel, all with default 2
# B: int, the weight to adjust intensity for blue channel, all with default 2

import numpy as np
import pytest
import skimage.io
from InstaF_Python.RGB_manipulation import RGB_manipulation

# test input: colour image
test_img_RBG_input = np.array([[[ 12.,  18.,  28.],[ 24.,  36.,   7.],[ 48.,   9.,  14.]],
                      [[ 48.,  72., 112.],[ 96., 144.,  28.],[192.,  36.,  56.]],
                      [[ 72., 108., 168.],[144., 216.,  42.],[32.,  54.,  84.]]], dtype = "uint8")

skimage.io.imsave("InstaF_Python/test/test_image/test_img_RBG_input.png", test_img_RBG_input)
# test output: expected RGB Manipulated image with RGB weights = (1, 2, 3 )
test_img_RGB_ex_output = np.array([[[ 12,  36,  84],[ 24,  72,  21],[ 48,  18,  42]],
                                   [[ 48, 144, 255],[ 96, 255,  84],[192,  72, 168]],
                                   [[ 72, 216, 255],[144, 255, 126],[ 32, 108, 252]]], dtype="uint8")

# Check whether RGB_manipulation function is working properly
def test_RGB():
    RGB_manipulation("InstaF_Python/test/test_image/test_img_RBG_input.png", "InstaF_Python/test/test_image/test_img_RBG_output.png", R = 1, G = 2, B = 3)
    output = skimage.io.imread("InstaF_Python/test/test_image/test_img_RBG_output.png")[:,:,:3]
    assert np.array_equal(output, test_img_RGB_ex_output), "RGB_manipulation not working"

# exception handling tests
## Wrong input type
def test_wrong_input_type():
    with pytest.raises(AttributeError):
        RGB_manipulation(12345, "InstaF_Python/test/test_image/test_img_RBG_output.png", R= 1, G=2, B=3)

## Wrong output type
def test_wrong_output_type():
    with pytest.raises(AttributeError):
        RGB_manipulation("InstaF_Python/test/test_image/test_img_RBG_input.png", 12345, R= 1, G=2, B=3)

## Not .png file input_path
def test_not_png_input():
    with pytest.raises(OSError):
        RGB_manipulation("InstaF_Python/test/test_image/not_image.Rmd", "InstaF_Python/test/test_image/test_img_RBG_output.png", R= 1, G=2, B=3)

## test for valid input input_path
def test_invalid_input_path():
    with pytest.raises(FileNotFoundError):
        RGB_manipulation("No_path.png", "InstaF_Python/test/test_image/test_img_RBG_output.png", R= 1, G=2, B=3)
