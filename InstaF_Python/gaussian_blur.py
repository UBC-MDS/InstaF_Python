
# Copyright 2019 Linyang Yu
# 2019-02-12
# you may not use this file or copy the codes without noticing us.
#
# the function is designed to perform gaussian blurring on RGB image with adjustable filter constomize



import numpy as np
import skimage.io
from PIL import Image
import matplotlib as plt




def gaussian_blur(input_image_path, output_image_path, filter_shape = (3,3), sigma = 1):

    '''
    This is the function we use to create a gaussian filter and perform the gaussian blurring on any RGB images
    we can use this function to customize the size/shape, and sigma value for the filter when we do blurring

    Input:
    -----------------------------------------------
    input_image_path: string, the directory path to the input file/image
    output_image_path: string, the directory path to the output file/image
    filter_shape: tuple, include the row number and col number of the filter, default value (3,3), the row number and col number shoud all be odd.
    * we add this argument to make our function different from the already exsit gaussian filter in python

    sigma: float, the standard diviation of the gaussian distribution we want to use for our filter


    '''
    # tests and warning message to garentee the right input
    try:
        input_image = skimage.io.imread(input_image_path)
    except AttributeError:
        print("Please provide the valid directory path for the input image")
        raise
    except TypeError:
        print("Please provide the valid directory path for the input image: input type should be string")
        raise
    except FileNotFoundError:
        print("Please provide the valid directory path for the input image: FileNotFound")
        raise
    except OSError:
        print("Please provide the valid directory path for the input image: input file shoud be image .png")
        raise
    except Exception as e:
        print("Unknown general error for input")
        print(e)
        raise
    
    if(filter_shape[0] %2 == 0 | filter_shape[1]%2 == 0):
        print("InputError: the shape of the filter should be odd")
        return

    # create the gaussian filter based on the input
    m,n = [(ss-1.)/2. for ss in filter_shape]
    y,x = np.ogrid[-m:m+1,-n:n+1]
    g_filt = np.exp( -(x*x + y*y) / (2.*sigma*sigma) )
    g_filt[g_filt < np.finfo(g_filt.dtype).eps*g_filt.max()] = 0
    sum_filt = g_filt.sum()
    if sum_filt != 0:
        g_filt /= sum_filt


    # define the symmetry of the filter
    row_gap = int((filter_shape[0]-1)/2)
    col_gap = int((filter_shape[1]-1)/2)


    # define the size and data type for the output image, the data type should be set as 'unit8'
    output_image = np.ones((len(input_image)-(row_gap*2), len(input_image[0])-(col_gap*2), 3), dtype="uint8")


    # iterate all the pixel in the original image
    for i in range(row_gap, len(input_image) - row_gap):
        for j in range(col_gap, len(input_image[i])-col_gap):
            for channel in range(0, len(input_image[i][j])): # we can process both RGB or grayscale
                
                # define the array around the pixel that we want to perform the gaussian blurring
                pixel_rec = [] # create an empty list to record the pixel

                for section_row in range(i - row_gap, i + row_gap+1):
                    for section_col in range(j - col_gap, j + col_gap+1):
                        pixel_rec.append(input_image[section_row][section_col][channel])

                pixel_array = np.array(pixel_rec).reshape(filter_shape[0], filter_shape[1])
                
                
                # calculate the value for the new pixel using gaussian filer matrix
                new_pix_rec = 0
                for row in range(filter_shape[0]):
                    for col in range(filter_shape[1]):
                        new_pix_rec += pixel_array[row][col] * g_filt[row][col]

                output_image[i-row_gap][j-col_gap][channel] = new_pix_rec

    # convert the np.array to image and save the image
    img = Image.fromarray(output_image, 'RGB')
    img.save(output_image_path)



    return output_image
