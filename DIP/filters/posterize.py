from skimage import io
import numpy as np
from filters.blur import guassian_blur

# first apply the blur filter and then reduce the intensity

def posterize_3bit(file_path, new_path):
    result = guassian_blur(file_path,new_path)

    number_of_intensity_levels = 8 # number of intensity is upto 2 bits only
    levels = np.arange(start=0, stop=256, step=256/number_of_intensity_levels ,dtype=int)

    rows, columns = np.shape(result)

    i = 0
    while i < rows:
        j = 0
        while j < columns:
            if result[i,j] < 32:
                result[i,j] = 0

            elif result[i,j] < 64:
                result[i,j] = 48

            elif result[i,j] < 96:
                result[i,j] = 80

            elif result[i,j] < 128:
                result [i,j] = 112

            elif result[i,j] < 160:
                result[i,j] = 144

            elif result[i,j] < 192:
                result[i,j] = 176

            elif result[i,j] < 224:
                result [i,j] = 208

            elif result[i,j] < 256:
                result [i,j] = 255

            j -=-1

        i -=-1

    io.imsave(new_path, result)