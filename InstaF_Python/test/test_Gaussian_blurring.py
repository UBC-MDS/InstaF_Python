# Feb 5th, 2019
# this script tests the function for GaussianBlur.py
# this function blurs an image using GaussianBlur
# Copy right: You may not use this file or copy the codes without noticing us.

# for the original program waiting to be tested
# input: image in .png format
# output: a blured image in .png format

import numpy as np
import pandas as pd
import os
import pytest
from skimage.color import rgb2gray
from skimage.transform import resize
from InstaF_Python import GaussianBlur

# input for test one, see if the function is able to correctly blur an ordinary image
# We use Milad's photo as an test example
# to test the output is now defined as a matrix, just to make the testing easier, in the future, the output will be converted to a image

# first we define a function to process the image
def preprocess_image(filename):
    img = plt.imread(filename) # read in the image
    img = resize(img, (100,100), mode='reflect') # resize it to simplify the case
    return img


# the first part we want to test if our function is able to convert regular RBG channel image
# we can then calculate the expected output image by matrix multiplication in python by hand for sigma = 1, filter_shape=(3,3)
expected_output_1 = preprocess_image("test_image/test.png.png")


# test normal picture with RBG channel
def test_normal_pic_rbg(self):
    assert np.arrat_equal(gaussian_blur("test_py/test_image/carnovsky_RGB_1.png", "test_py/test_image/test.png", sigma = 1, filter_shape = (3,3)), expectied_output_1), "GaussianBlur not working on RBG image"


# test non-image input
def test_wrong_input_type():
    with pytest.raises(AttributeError):
        gaussian_blur("This is not an image","test_py/test_image/test.png", sigma = 1, filter_shape = (3,3))

# test missing input arguments
def test_input_path_not_exist():
    with pytest.raises(FileNotFoundError):
        laplacian_filter("./1234/123.png", "test_py/test_image/test.png", sigma = 1, filter_shape = (3,3))
