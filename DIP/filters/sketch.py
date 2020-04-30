from skimage import io
import numpy as np
from skimage.filters import sobel,sobel_v,sobel_h
from skimage.color import rgb2gray
import math
import matplotlib.pyplot as plt
from filters.equalize import equalization_function

def findSum(arr):
    total = 0
    i = 0
    while i < 3:
        j = 0
        while j < 3:
            total += arr[i][j]
            j += 1

        i += 1

    return total

def sketching_function (file_path, new_path):
    image = equalization_function(file_path,new_path, 1)
    v_kernel = np.zeros((3, 3), dtype=int)
    v_kernel[0, 0] = 1
    v_kernel[0, 2] = -1
    v_kernel[1, 0] = 2
    v_kernel[2, 0] = 1
    v_kernel[2, 2] = -1
    v_kernel[1, 2] = -2
    h_kernel = np.transpose(v_kernel)

    (end_row, end_col) = np.shape(image)
    g_x = np.zeros((end_row, end_col), dtype=int)
    g_y = np.zeros((end_row, end_col), dtype=int)

    i = 0
    while i < end_row - 2:
        j = 0
        while j < end_col - 2:
            matrix = image[i:i + 3, j:j + 3]
            matrix_multiplication = np.multiply(matrix, v_kernel)
            value = float(findSum(matrix_multiplication) / 9)
            g_x[i + 1][j + 1] = value
            j -= -1

        i -= -1

    i = 0
    while i < end_row - 2:
        j = 0
        while j < end_col - 2:
            matrix = image[i:i + 3, j:j + 3]
            matrix_multiplication = np.multiply(matrix, h_kernel)
            value = float(findSum(matrix_multiplication) / 9)
            g_y[i + 1][j + 1] = value
            j -= -1

        i -= -1

    result = np.zeros((end_row, end_col), dtype=int)

    i = 0
    while i < end_row:
        j = 0
        while j < end_col:
            result[i, j] = int(math.sqrt(math.pow(g_x[i, j], 2) + math.pow(g_y[i, j], 2)))
            j -= -1

        i -= - 1

    result = 255 - result
    io.imsave(new_path, result)


