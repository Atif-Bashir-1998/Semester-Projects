from skimage import io
import numpy as np
from skimage.color import rgb2gray

def border_20px(file_path, new_path):
    image = io.imread(file_path)
    image = rgb2gray(image)
    rows, columns = np.shape(image)

    result = np.zeros((rows + 40, columns + 40), dtype=int)
    result[20:-20, 20:-20] = image

    io.imsave(new_path, result)