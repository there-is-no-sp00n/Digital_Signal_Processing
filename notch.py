#Aninda Aminuzzaman

#1001018367


import numpy as np
import matplotlib.pyplot as plt

my_file = open('notchData.csv', 'r')

result = my_file.readlines()


for line in result:
	from_file = line.split(",")

for i in range(0, len(from_file)):
	from_file[i] = float(from_file[i])


#original
plt.figure(1)
plt.xlim(-25, 625)
plt.plot(from_file)
plt.title("Original")


f = 17
fs = 500
w = f/fs


#the input signal modified using the equation from part a
a = []

#y[n] = x[n] - 2cos(w)x[n-1] + x[n-2] + 1.8744cos(w)y[n-1] - y[n-2]
for i in range(0, len(from_file)):
	if i - 1 < 0: #for i = 0
		temp = from_file[i]
		a.append(temp)
	elif i - 2 < 0: #for i = 1
		temp = from_file[i] - (2 * np.cos(w) * from_file[i-1] + 0) + (1.8744 * np.cos(w) * a[i-1])
		a.append(temp)
	else: #for i >= 2
		temp = from_file[i] - (2 * np.cos(w) * from_file[i-1] + 0) + (1.8744 * np.cos(w) * a[i-1]) - a[i-2]
		a.append(temp)


b = np.convolve(from_file, a)


plt.figure(4)
#plt.ylim(-2.25, 2.25)
plt.plot(b)
plt.title("Filtered")


x10 = np.arange(fs)

y10 = np.sin(2 * np.pi * 10 * x10/fs)
y33 = np.sin(2 *np.pi * 33 * x10/fs)

# 10Hz + 33Hz
added = y10 + y33
plt.figure(5)
plt.plot(added)
plt.title("10 Hz + 33 Hz")

plt.show()
