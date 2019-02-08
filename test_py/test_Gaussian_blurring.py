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

# first we define a function to process the image
def preprocess_image(filename):
    img = plt.imread(filename) # read in the image
    img = resize(img, (100,100), mode='reflect') # resize it to simplify the case
    return img


# the first part we want to test if our function is able to convert regular RBG channel image
input_img_1 = preprocess_image("test_image/milad_cropped.png")
# we can then calculate the expected output image by matrix multiplication in python by hand for sigma = 1
expected_output_1 = preprocess_image("test_image/milad_gaussian.png")

# the second part we want to test if our function is able to convert regular grayscale channel image
input_img_2 = preprocess_image("test_image/milad_gray.png")
# we can then calculate the expected output image by matrix multiplication in python by hand for sigma = 1
expected_output_2 = preprocess_image("test_image/milad_gray_gaussian.png")


# test normal picture with RBG channel
def test_normal_pic_rbg(self):
    assert np.arrat_equal(gaussian_blur(input_img_1, sigma = 1), expectied_output_1), "GaussianBlur not working on RBG image"

# test normal picture with gray scale
def test_normal_pic_gray_scale(self):
    assert np.arrat_equal(gaussian_blur(input_img_2, sigma = 1), expectied_output_2), "GaussianBlur not working on grayscale image"


# test non-image input
def test_wrong_input_type():
    with pytest.raises(AttributeError):
        gaussian_blur("This is not an image", sigma = 1)

# test missing input arguments
def test_input_path_not_exist():
    with pytest.raises(FileNotFoundError):
        laplacian_filter("./1234/123.png", sigma = 1)
