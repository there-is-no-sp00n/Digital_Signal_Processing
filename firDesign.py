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


#low pass filtered
x1 = list(range(0,len(final)))
plt.figure(3)
plt.plot(x1, final)
plt.title("Low Pass Filter")


#
#part d
#


#orginal #2
x3 = list(range(0,100))
y3 = sets[:100]
plt.figure(4)
plt.plot(x3, y3)
plt.title("Original (PART D)")


#330 Hz
x4 = np.arange(2000)
y4 = np.sin(2 * np.pi * 330 * x4/2000)
plt.figure(5)
plt.plot(x4[:100], y4[:100])
plt.title("330 Hz")

w = []
#high pass filter weight
fc = 280

ft = fc/fs

for i in range(0,20):
	if(M/2 != i):
		n = np.sin(2*np.pi*ft*(i-(M/2)))/(np.pi * (i-(M/2)))
		n = n * -1
		w.append(n)
	else:
		n = 1 - (2*ft)
		w.append(n)

final = np.convolve(sets, w)

#high pass filtered
x5 = list(range(0, len(final)))
plt.figure(6)
plt.plot(x5[:100], final[:100])
plt.title("High Pass Filter")


plt.show()
