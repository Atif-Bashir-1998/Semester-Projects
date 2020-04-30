from skimage import io
import numpy as np
from skimage.color import rgb2gray

def findSum(arr):
    total = 0
    i = 0
    while i < 3:
        j = 0
        while j < 3:
            total += arr[i][j]
            j +=1

        i +=1

    return total

def sharpen(file_path, new_path):
    image = io.imread(file_path)
    image = rgb2gray(image)
    result = image

    # We will have Gaussian Blur on the photo
    kernel = np.ones((3, 3), dtype=int)
    kernel[:, :] = -1
    kernel[1, 1] = 17

    (end_row, end_col) = np.shape(image)
    i = 0
    while i < end_row - 2:
        j = 0
        while j < end_col - 2:
            matrix = image[i:i + 3, j:j + 3]
            matrix_multiplication = np.multiply(matrix, kernel)

            value = int(findSum(matrix_multiplication) / 9)
            result[i + 1][j + 1] = value
            j -= -1

        i -= -1

    io.imsave(new_path, result)


