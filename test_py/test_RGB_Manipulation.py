# Copyright 2018 Betty Zhou
# This script contains tests for the RGB_manipulation function

# input: image in .png format, weights for adjusting R,G,B
# output: a RBG adjusted image in .png format

import numpy as np
import pytest
import skimage.io

# test input: colour image
test_img_RBG_input = np.array([[[ 12.,  18.,  28.],[ 24.,  36.,   7.],[ 48.,   9.,  14.]],
                      [[ 48.,  72., 112.],[ 96., 144.,  28.],[192.,  36.,  56.]],
                      [[ 72., 108., 168.],[144., 216.,  42.],[255.,  54.,  84.]]], dtype = "uint8")

skimage.io.imsave("test_py/test_image/test_img_RBG_input.png", test_img_RBG_input)
# test output: expected RGB Manipulated image with RGB weights = (1, 2, 3 )
test_img_RGB_ex_output = np.array([[[  3,   2,  51],[  6,   6,  12],[ 12,   0,  24]],
                         [[ 12,  12, 213],[ 24,  24,  51],[ 48,   6, 105]],
                         [[ 18,  18, 255],[ 36,  38,  78],[  8,   8, 159]]], dtype="uint8")

skimage.io.imsave("test_py/test_image/test_img_RGB_ex_output.png", test_img_RGB_ex_output)

# Check whether RGB_manipulation function is working properly
def test_RGB():
    RGB_manipulation("test_py/test_image/test_img_RBG_input.png", "test_py/test_image/RBG_output.png", R= 1, G=2, B=3)
    output = skimage.io.imread("test_py/test_image/RBG_output.png")
    expected_output = skimage.io.imread("test_py/test_image/test_img_RGB_ex_output")
    assert np.array_equal(output, expected_output), "RGB_manipulation not working"

# Check edge cases
# Wrong input type
def test_wrong_input_type():
    with pytest.raises(AttributeError):
        RGB_manipulation(12345, "test_py/test_image/test_img_RGB_ex_output.png", R= 1, G=2, B=3)

# Wrong output type
def test_wrong_output_type():
    with pytest.raises(AttributeError):
        RGB_manipulation("test_py/test_image/test_img_RBG_input.png", 12345, R= 1, G=2, B=3)

# Too many arguments
def test_wrong_input_arg():
    with pytest.raises(AttributeError):
        RGB_manipulation(12345, "test_py/test_image/test_img_RGB_ex_output.png", R= 1, G=2, B=3, 123)
