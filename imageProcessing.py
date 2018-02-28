#Aninda Aminuzzaman

#1001018367



import matplotlib.pyplot as plt
import matplotlib.image as pimg

import numpy as np

from scipy import ndimage



#reading the tiff images
my_image_1 = pimg.imread('boat.512.tiff')
plt.figure(1)
plt.imshow(my_image_1)
plt.title("Boat Original")

my_image_2 = pimg.imread('clock-5.1.12.tiff')
plt.figure(2)
plt.imshow(my_image_2)
plt.title("Clock Original")

my_image_3 = pimg.imread('man-5.3.01.tiff')
plt.figure(3)
plt.imshow(my_image_3)
plt.title("Man Original")

my_image_4 = pimg.imread('tank-7.1.07.tiff')
plt.figure(4)
plt.imshow(my_image_4)
plt.title("Tank Original")



#convert the image into an array and then the array to a list
arr_1 = np.array(my_image_1).tolist()
arr_2 = np.array(my_image_2).tolist()
arr_3 = np.array(my_image_3).tolist()
arr_4 = np.array(my_image_4).tolist()


#10 .1 low passes
low_pass = [0.1]*10


#lists to hold the convolved info of the images
arr_1_lp = []
arr_2_lp = []
arr_3_lp = []
arr_4_lp = []

#low pass filter
#convolve every element in the list then display the new image
for i in range(0, len(arr_1)):
	arr_1_lp.append(np.convolve(arr_1[i], low_pass))

plt.figure(5)
plt.imshow(arr_1_lp)
plt.title("Boat Low Pass Filter")

for i in range(0, len(arr_2)):
	arr_2_lp.append(np.convolve(arr_2[i], low_pass))

plt.figure(6)
plt.imshow(arr_2_lp)
plt.title("Clock Low Pass Filter")

for i in range(0, len(arr_3)):
	arr_3_lp.append(np.convolve(arr_3[i], low_pass))

plt.figure(7)
plt.imshow(arr_3_lp)
plt.title("Man Low Pass Filter")

for i in range(0, len(arr_4)):
	arr_4_lp.append(np.convolve(arr_4[i], low_pass))	

plt.figure(8)
plt.imshow(arr_4_lp)
plt.title("Tank Low Pass Filter")



#part g high pass filter

high_pass = [1, -1]

arr_1_hp = []
arr_2_hp = []
arr_3_hp = []
arr_4_hp = []

for i in range(0, len(arr_1)):
	arr_1_hp.append(np.convolve(arr_1[i], high_pass))

plt.figure(9)
plt.imshow(arr_1_hp)
plt.title("Boat High Pass Filter")

for i in range(0, len(arr_2)):
	arr_2_hp.append(np.convolve(arr_2[i], high_pass))

plt.figure(10)
plt.imshow(arr_2_hp)
plt.title("Clock High Pass Filter")

for i in range(0, len(arr_3)):
	arr_3_hp.append(np.convolve(arr_3[i], high_pass))

plt.figure(11)
plt.imshow(arr_3_hp)
plt.title("Man High Pass Filter")

for i in range(0, len(arr_4)):
	arr_4_hp.append(np.convolve(arr_4[i], high_pass))	

plt.figure(12)
plt.imshow(arr_4_hp)
plt.title("Tank High Pass Filter")



#part h

my_image_5 = pimg.imread('darinGrayNoise.jpg')
plt.figure(13)
plt.imshow(my_image_5)
plt.title("Dr. Brezeale OG")

arr_5 = np.array(my_image_5).tolist()
arr_5_lp = []

for i in range(0, len(arr_5)):
	arr_5_lp.append(np.convolve(arr_5[i], low_pass))

plt.figure(14)
plt.imshow(arr_5_lp)
plt.title("Dr. Brezeale Low Pass Filter")


output_image = ndimage.median_filter(my_image_5, 5)
plt.figure(15)
plt.imshow(output_image)
plt.title("Dr. Brezeale Medium Filter")


plt.show()
