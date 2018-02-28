#Aninda Aminuzzaman

#1001018367



import matplotlib.pyplot as plt
import matplotlib.image as pimg

import numpy as np

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

print(len(arr_1))
print(len(arr_2))
print(len(arr_3))
print(len(arr_4))

#10 .1 low passes
low_pass = [0.1]*10


#convolve every element in the list then display the new image
for i in range(0, len(arr_1)):
	arr_1[i] = np.convolve(arr_1[i], low_pass)

plt.figure(5)
plt.imshow(arr_1)
plt.title("Boat Low Pass Filter")

for i in range(0, len(arr_2)):
	arr_2[i] = np.convolve(arr_2[i], low_pass)

plt.figure(6)
plt.imshow(arr_2)
plt.title("Clock Low Pass Filter")

for i in range(0, len(arr_3)):
	arr_3[i] = np.convolve(arr_3[i], low_pass)

plt.figure(7)
plt.imshow(arr_3)
plt.title("Man Low Pass Filter")

for i in range(0, len(arr_4)):
	arr_4[i] = np.convolve(arr_4[i], low_pass)	

plt.figure(8)
plt.imshow(arr_4)
plt.title("Boat Low Pass Filter")








plt.show()
