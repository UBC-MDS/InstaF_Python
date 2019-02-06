# Feb 5th, 2019
# this script tests the function for GaussianBlur.py
# this function blurs an image using GaussianBlur
# Copy right: You may not use this file or copy the codes without noticing us.

# for the original program waiting to be tested
# input: image in .png format
# output: a blured image in .png format

import unittest
import numpy as np
import pandas as pd
import os
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


# the third part we want to test if the function can correctly recognize if an input is an image or not
input_img_3 = "This is not a image but a string"
expected_output_3 = "The input is not a image"


# Define the test units

class TestUM(unittest.TestCase):

    def setup(self):
        pass

    # test normal picture with RBG channel
    def test_normal_pic(self):
        self.assertEqual(GaussianBlur(input_img_1, sigma = 1), expectied_output_1)

    # test normal picture with gray scale
    def test_normal_pic(self):
        self.assertEqual(GaussianBlur(input_img_2, sigma = 1), expectied_output_2)

    # test non-image input
    def test_normal_pic(self):
        self.assertEqual(GaussianBlur(input_img_3, sigma = 1), expectied_output_3)
