#Aninda Aminuzzaman

#1001018367


import numpy as np

import matplotlib.pyplot as plt

import scipy.io.wavfile

from scipy.signal import freqz


my_file = scipy.io.wavfile.read('P_9_2.wav')


print(len(my_file))
print(my_file)


aud_portion = my_file[1]


plt.figure(1)
plt.plot(aud_portion)
plt.title('Original')

print(len(aud_portion))
print(aud_portion)

aud_portion = np.fft.fft(aud_portion)

print(len(aud_portion))
print(aud_portion)

plt.figure(2)
plt.plot(abs(aud_portion))
plt.title('FFT Values')


mid = int(len(aud_portion)/2)
offset = 20000


aud_portion[mid] = 0

for i in range(mid, mid + offset):
	aud_portion[i+1] = 0

for i in range(mid - offset, mid):
	aud_portion[i] = 0


plt.figure(3)
plt.plot(abs(aud_portion))
plt.title('No Noise')


aud_portion = np.fft.ifft(aud_portion)



plt.figure(4)
plt.plot(abs(aud_portion))
plt.title('IFFT Values')

#print(mid)

#plt.show()

#a = my_file.dtype()
#print(my_file[1].dtype)
#print("a is", a);


scipy.io.wavfile.write('cleanMusic.wav', my_file[0], aud_portion.astype(my_file[1].dtype))
