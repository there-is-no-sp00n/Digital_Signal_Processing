#Aninda Aminuzzaman


#1001018367


import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile


my_file = open('shelvingConfig.txt', 'r')

result = my_file.readlines()

#print(result)
#print(len(result))

for i in range(0,len(result)):
	result[i] = result[i].strip()

result[1] = int(result[1])
result[2] = int(result[2])

#print(result)
#print(len(result))


my_audio_file = scipy.io.wavfile.read(result[0])

#print(my_audio_file)

aud_portion = my_audio_file[1]

plt.subplot(2, 2, 1)
plt.plot(aud_portion)

aud_portion = np.fft.fft(aud_portion)

plt.subplot(2, 2, 2)
plt.plot(aud_portion)
plt.title('FFT')

#plt.show()
aud_portion = my_audio_file[1]

fs = 44100

theta = 2 * np.pi * (result[2]/fs)
mu = 10**(result[1]/20)

gamma_top = 1 - ((4/(1+mu)) * np.tan(theta/2))
gamma_bottom = 1 + ((4/(1+mu)) * np.tan(theta/2))

gamma = gamma_top/gamma_bottom

alpha = (1 - gamma)/2

u = []

for i in range(0, len(aud_portion)):
	if i - 1 < 0:
		temp = (alpha * aud_portion[i])
		u.append(temp)
	else:
		temp = (alpha * (aud_portion[i] + aud_portion[i-1])) + (gamma * u[i-1])
		u.append(temp)

#print(len(aud_portion))
#print(u)
#print(len(u))

y = []


for i in range(0, len(aud_portion)):
	temp = aud_portion[i] + ((mu - 1) * u[i])
	y.append(temp)	


#print(len(y))

plt.subplot(2, 2, 3)
plt.plot(y)
plt.title('Y')

#scipy.io.wavfile.write('shelvingOutput.wav', my_audio_file[0], y.astype(my_audio_file[1].dtype))

y_arr = np.asarray(y)

scipy.io.wavfile.write('shelvingOutput.wav', my_audio_file[0], y_arr.astype(my_audio_file[1].dtype))


y = np.fft.fft(y)

plt.subplot(2, 2, 4)
plt.plot(y)
plt.title('FFT Y')

plt.show()

