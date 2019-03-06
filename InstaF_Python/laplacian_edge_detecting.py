import numpy as np
import matplotlib.pyplot as plt
import skimage

def laplacian_edge_detecting(input_image,  output_image):
    '''
    Perform laplacian filtering on the image to get the secondary derivitive of the image matrix, based on the defined input path

    The function applys a Laplacian filter to each color chanel of the input image. The filter is [[0, -1, 0],[-1,4,-1],[0,-1,0]]. Before applying the filter
    The matrix. The filtered image will be saved on the output_image path.
.
    Inputs
    -----
    input_path: string, path for an image file in .png format
    output_path: string, path for the output image in .png format
    '''

    # Handling the exceptions
    try:
        # Reading the image matrix
        image = skimage.io.imread(input_image)
    except AttributeError:
        print("Not a valid file name or path!")
        raise
    except FileNotFoundError:
        print("FileNotFound!")
        raise

    for k in range(3):

        # Separating the color chanels
        chanel = image[:,:,k]

        # Padding the matrix
        chanel = np.pad(chanel, [(1, 1), (1, 1)], mode='edge')
        result = np.zeros(chanel.shape)

        # Applying the convolution filter
        for i in range(1,chanel.shape[0]-1):
            for j in range(1,chanel.shape[1]-1):
                result[i,j] = 4*chanel[i,j]-chanel[i+1,j]-chanel[i-1,j]-chanel[i,j+1]-chanel[i,j-1]

        # Removing non-valied colors
        result[result<0]=0
        result[result>255]=255

        # Removing the pads
        result=np.delete(result, result.shape[0]-1, 0)
        result=np.delete(result, 0, 0)
        result=np.delete(result, result.shape[1]-1, 1)
        result=np.delete(result, 0, 1)

        # Copying the result
        image[:,:,k] = result

    # Saving the image at output_path
    skimage.io.imsave(output_image, image)
