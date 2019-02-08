# InstaF in Python Proposal

## Contributors:

Betty Zhou     
Linyang Yu    
Reza Bagheri    
Simon Chiu    

## Overview

Image processing uses computer algorithms to enhance an image or to extract useful information from it. In this package, we have implemented some Python functions for image processing. These functions perform Gaussian blurring, Laplacian edge detection, and color changing.

## Functions

1. **Gaussian Blur**    
   This function performs convolution to de-emphasize differences in adjacent pixel values with a Gaussian distribution. The blurring effect removes detail and noise in the input image.
2. **Laplacian Edge Detecting**    
   This function performs convolution to emphasize differences in adjacent pixel values. The function detects edges by sharpening/highlighting the edges of an image.
3. **RBG Manipulation**    
   This function adjusts the red, blue and green intensity of an image by applying different weights for each RBG channel. This is similar to a colour filter in Instagram.


## Python Ecosystem

[InstaPy](https://github.com/UBC-MDS/InstaPy) is a Python package that contains the three functions: blur, flip and greyscale to transform images. In this project, we plan to implement three more image processing functions in Python by exploring additional filters.


## Repo structure (will keep updating):


InstaF_Python
    - [CONTRIBUTING.md](CONTRIBUTING.md)
    - [Code_of_CONDUCT.md](Code_of_CONDUCT.md)
    - README.md
    - [test_py](test_py)
          - [test_image](test_py/test_image)
          - [test_Gaussian_blurring.py](test_py/test_Gaussian_blurring.py)
          - [test_Laplacian_edge_detecting.py](test_py/test_Laplacian_edge_detecting.py)
          - [test_RGB_Manipulation.py](test_py/test_RGB_Manipulation.py)
