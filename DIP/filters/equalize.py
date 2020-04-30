from skimage import io
import numpy as np
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

def equalization_function (file_path, new_path, *args):
    image = io.imread(file_path)
    image = rgb2gray(image)
    original = image
    (rows, cols) = np.shape(image)

    ''' I created a dictionary to get the intensity levels and number of pixels at
     each intensity level'''
    dictionary = {}
    i = 0
    while i < rows:
        j = 0
        while j < cols:
            if image[i, j] in dictionary:
                dictionary[image[i, j]] += 1

            else:
                dictionary[image[i, j]] = 1

            j -= - 1

        i -= - 1

    # here I created a sorted dictionary to and I also created a list of lists
    # having a key and a value in each inner list
    sorted_dictionary = {}
    for i in sorted(dictionary):
        sorted_dictionary[i] = dictionary[i]

    list_key_value = [[k, v] for k, v in sorted_dictionary.items()]

    # here I am listing out the values of pixels and frequencies in different lists
    pixel_values = []
    frequency = []

    i = 0
    while i < len(list_key_value):
        pixel_values.append(list_key_value[i][0])
        frequency.append(list_key_value[i][1])
        i -= - 1

    # Cumulative frequency list
    c_frequency = []
    total = 0
    i = 0
    while i < len(frequency):
        total = total + frequency[i]
        c_frequency.append(total)
        i -= - 1

    # Probability Distribution Function list
    pdf = []
    i = 0
    while i < len(pixel_values):
        p = pixel_values[i] / sum(pixel_values)
        pdf.append(p)
        i -= - 1

    # Cumulative Distribution Function list
    cdf = []
    i = 0
    total = 0
    while i < len(pdf):
        total = total + pdf[i]
        cdf.append(total)
        i -= - 1

    # new intensity levels are being created
    number_of_levels = len(pixel_values)
    new_levels = []
    i = 0
    while i < len(cdf):
        new_levels.append(int(number_of_levels * cdf[i]))
        i -= - 1

    # make a dictionary for mapping new values and older values of pixel intensities
    i = 0
    maping = {}
    while i < len(pixel_values):
        maping[pixel_values[i]] = new_levels[i]
        i -= - 1

    # loop through the image and put the new values in each pixel
    i = 0
    while i < rows:
        j = 0
        while j < cols:
            image[i, j] = maping[image[i, j]]
            j -= - 1

        i -= - 1

    io.imsave(new_path, image)

    if len(args) == 0:
        ax1 = plt.hist(original.ravel(),bins=256, label='Original Histogram')
        plt.legend(loc='upper right')
        plt.show()
        modified = io.imread(new_path)
        modified = rgb2gray(modified)
        ax2 = plt.hist(modified.ravel(),bins=256, label='Equalized Histogram')
        plt.legend(loc='upper right')
        plt.show()


    return image
