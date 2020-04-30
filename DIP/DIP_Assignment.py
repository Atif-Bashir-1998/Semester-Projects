# importing the libraries
from skimage import io, img_as_int
import matplotlib.pyplot as plt
import numpy as np
from reciever import incomming
import time

# loading the image
path = input("Enter the complete path of your image file: ")
try:
    image = io.imread(path, as_gray=True)
except FileNotFoundError:
    print("Sorry ! The path specified is not correct")
    exit()




image = img_as_int(image)
(rows, cols) = np.shape(image)
time.sleep(2)

# taking the message from the user
message = input("Enter your message :").upper()

# encoding the message of the user into ASCII code
coded_message = []
i = 0
while i < len(message):
    coded_message.append(ord(message[i]))
    i -=- 1
print("coded_message :", coded_message)

# Converting the image into a desired data structure so that it can be transmitted
packet = []

i = 0
while i < rows:
    j = 0
    while j < cols:
        packet.append(bin(image[i, j]))
        j -=- 1

    i -=- 1
# image has been successfully converter into a list of strings of binary


# I will be preparing the meta-data in this block
md_rows = str(rows)
md_cols = str(cols)
md_msg = str(len(message))

# I will be hiding the data in 4 LSBs, so to make sure my metadata is formated accordingly
md_rows = md_rows.zfill(4)
md_cols = md_cols.zfill(4)
md_msg = md_msg.zfill(4)

''' here, I am adding the metadata to the packet which has been encoded into binary.
metadata is about the rows, cols and the length of the message of the user
the metadata will be having 4 LSBs in each pixel'''
row_pixel = packet[0]
col_pixel = packet[1]
msg_size_pixel = packet[2]

row_pixel = row_pixel[0:-4]
row_pixel = row_pixel + md_rows

col_pixel = col_pixel[0:-4]
col_pixel = col_pixel + md_cols

msg_size_pixel = msg_size_pixel[0:-4]
msg_size_pixel = msg_size_pixel + md_msg

# metadata will be added to the packet
packet[0] = row_pixel
packet[1] = col_pixel
packet[2] = msg_size_pixel

'''Letters of my message will have 2 LSBs
here I will be adding my coded message into the packet and will also indicate the start & terminate the message'''
message_start_pixel = packet[3]
message_start_pixel = message_start_pixel[0:-2]
message_start_pixel = message_start_pixel + "AB"
packet[3] = message_start_pixel

i = 0
while i < len(message):
    packet[i+4] = packet[i+4][0:-2]
    packet[i+4] = packet[i+4] + str(coded_message[i])
    i -=- 1

message_end_pixel = packet[4+len(message)]
message_end_pixel = message_end_pixel[0:-2]
message_end_pixel = message_end_pixel +"HA"
packet[4+len(message)] = message_end_pixel

# here I am sending the packet to the reciever side
print("\n\nSENDING THE MESSAGE NOW ...\n\n")
incomming(packet)