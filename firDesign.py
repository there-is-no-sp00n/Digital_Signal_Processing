#Aninda Aminuzzaman

#1001018367


import numpy as np
import matplotlib.pyplot as plt


my_file = open('data-filtering.csv', 'r')

result = my_file.readlines()

for line in result:
	sets = line.split(",")

#convert to float
for i in range (0, len(sets)):
	sets[i] = float(sets[i])

print(len(sets))



x = list(range(0,2000))

fs = 2000
fc = 50
L = 21
M = L - 1
ft = fc/fs

w = []
#original
plt.figure(1)
plt.plot(x, sets)
plt.title("Original")

#4 Hz
x2 = np.arange(fs)
y = np.sin(2 * np.pi * 4 * x2/fs)
plt.figure(2)
plt.plot(x2, y)
plt.title("4 Hz")

#low pass filter weight
for i in range(0,20):
	if(M/2 != i):
		n = np.sin(2*np.pi*ft*(i-(M/2)))/(np.pi * (i-(M/2)))
		w.append(n)

	else:
		n = 2 * ft
		w.append(n)	

#convolve to apply
final = np.convolve(sets, w)

print (len(final))

#filtered
x1 = list(range(0,len(final)))
plt.figure(3)
plt.plot(x1, final)
plt.title("Filtered")

plt.show()
