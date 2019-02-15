# This script contains tests for the Laplacian_edge_detecting function

# input: image in .png format
# output: a RBG adjusted image in .png format

import numpy as np
import pytest
import skimage.io
from InstaF_Python import laplacian_filter

# test input: colour image
test_img_laplacian_input = np.array([[[12, 79, 15],[171, 55, 63],[48, 90, 14]],
                                    [[36, 72, 80],[ 96, 144, 28],[215, 36, 40]],
                                    [[92, 32, 168],[144, 216, 209],[112, 54, 60]]], dtype = "uint8")

skimage.io.imsave("test_py/test_image/test_img_laplacian_input.png", test_img_laplacian_input)
# test output: Image with the Laplacian filter applied on it
# filter is [[0,-1,	0],[-1,4,-1],[0,-1,	0]] and boundary is symm

test_img_laplacian_ex_output = np.array([[[  0,  31,   0], [255,   0, 132], [  0,  89,   0]],
                                         [[  0,   0,  29], [  0, 197,   0], [255,   0,  18]],
                                         [[  4,   0,  47], [132, 255, 255], [  0,   0,   0]]], dtype="uint8")

skimage.io.imsave("test_py/test_image/test_img_laplacian_exp_output.png", test_img_laplacian_ex_output)

# Check whether laplacian_filter function is working properly
def test_laplacian():
    laplacian_filter("test_py/test_image/test_img_laplacian_input.png", "test_py/test_image/laplacian_output.png")
    output = skimage.io.imread("test_py/test_image/laplacian_output.png")
    expected_output = skimage.io.imread("test_py/test_image/test_img_laplacian_exp_output.png")
    assert np.array_equal(output, expected_output), "Laplacian filter is not working properly"

#Handling the exceptions with laplacian_filter()
def test_bad_input():
    with pytest.raises(AttributeError):
        laplacian_filter(1234, "test_py/test_image/laplacian_output.png")

def test_input_file_no_image():
    with pytest.raises(OSError):
        laplacian_filter("test_py/test_image/test.txt", "test_py/test_image/laplacian_output.png")

def test_input_path_not_exist():
    with pytest.raises(FileNotFoundError):
        laplacian_filter("./1234/123.png", "test_py/test_image/laplacian_output.png")

def test_bad_output():
    with pytest.raises(AttributeError):
        laplacian_filter("test_py/test_image/test_img_laplacian_input.png", 1234)


