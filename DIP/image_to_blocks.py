from skimage import io
import matplotlib.pyplot as plt
import numpy as np
import time
from skimage.color import rgb2gray


def splitting_function (image, row, col, block, index):
    (r,c) = np.shape(block)
    block[:, :] = image [row:row+r, col: col+c]
    io.imsave(f'C:\\Users\\Atif\\Pictures\\lock{index}.jpg', block)
    if index == 2:
        return (r, col+c)
    return (row + r, col + c)

def combine_function(combined_image,s_row,s_col, index):
    block = io.imread(f'C:\\Users\\Atif\\Pictures\\lock{index}.jpg')
    (r, c) = np.shape(block)
    combined_image [s_row:s_row +r, s_col:s_col+c] = block[:,:]

    if index == 2:
        return (combined_image,r, s_col+c)
    return (combined_image,s_row+r,s_col+c)



image = io.imread(r'C:\Users\Atif\Pictures\Jinnah_filtered.jpg')
image = rgb2gray(image)
#io.imshow(image)
#plt.show()

# now we will divide the image into 4 blocks
(rows,columns)=np.shape(image)

rows_modified = False
columns_modified = False

#if either rows or columns are odd we will have to do some manipulations
if rows % 2 != 0 and columns % 2 != 0:
    new_image = np.zeros((rows+1, columns+1), dtype=int)
    new_image [0:-1, 0:-1] = image
    rows_modified = True
    columns_modified = True


if rows % 2 != 0:
    new_image = np.zeros((rows+1, columns), dtype=int)
    new_image [0:-1,:] = image
    rows_modified = True


if columns % 2 != 0:
    new_image = np.zeros((rows, columns + 1), dtype=int)
    new_image [:, 0:-1] = image
    columns_modified = True

else:
    new_image = image

block_rows = int(rows/2)
block_columns = int(columns/2)

i = 0
s_row = 0
s_col = 0

index_array = [(0,0), (0,1), (1,0), (1,1)]

while i < 4:
    (x,y) = index_array [i]
    s_row = x*s_row
    s_col = y*s_col
    block = np.zeros((block_rows, block_columns), dtype=int)
    if s_row == rows:
        s_row = int(s_row/2)
    (s_row, s_col) = splitting_function(new_image,s_row, s_col,block,index= i)

    i -=- 1

#code from here will deal with the combining function
total_rows = 2 * block_rows
total_columns = 2 * block_columns
combined_image = np.zeros((total_rows, total_columns), dtype=int)

i = 0
s_row = 0
s_col = 0
while i < 4:
    (x,y) = index_array [i]
    s_row = x*s_row
    s_col = y*s_col
    if s_row == rows:
        s_row = int(s_row/2)
    (combined_image,s_row,s_col) = combine_function(combined_image,s_row, s_col, index=i)
    i += 1

if rows_modified:
    combined_image = combined_image[0:-2,:]

elif columns_modified:
    combined_image = combined_image[:, 0:-2]

elif rows_modified and columns_modified:
    combined_image = combined_image[0:-2, 0:-2]


io.imsave(r'C:\Users\Atif\Pictures\combined.jpg', combined_image)