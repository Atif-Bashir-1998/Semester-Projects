from skimage import io
import numpy as np
from skimage.color import rgb2gray

def intensity_2bit(file_path, new_path):
    image = io.imread(file_path)
    image = rgb2gray(image)
    result = image

    number_of_intensity_levels = 4 # number of intensity is upto 2 bits only
    levels = np.arange(start=0, stop=256, step=256/number_of_intensity_levels ,dtype=int)

    rows, columns = np.shape(result)

    i = 0
    while i < rows:
        j = 0
        while j < columns:
            if result[i,j] < 64:
                result[i,j] = 0

            elif result[i,j] < 128:
                result[i,j] = 96

            elif result[i,j] < 192:
                result[i,j] = 160

            elif result[i,j] < 256:
                result [i,j] = 255

            j -=-1

        i -=-1

    io.imsave(new_path, result)