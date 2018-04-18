from scipy import signal

import scipy.io.wavfile

import glob

import numpy as np

song_db = glob.glob('song-*.wav');

print(song_db, len(song_db))

#for i in song_db:
	

b = scipy.io.wavfile.read('song-winds.wav')

print(b)

x = b[1]
fs = b[0]

f, t, Sxx = signal.spectrogram(x, fs=fs, nperseg=0.5*fs)

print(f, len(f))

print(t, len(t))

print(Sxx, len(Sxx[0]))


temp = 0
final = 0
arr = []

d = Sxx.argmax(axis=0)

print(d, len(d))

for i in range(0, len(d)):
	d[i] = f[d[i]]

print(d, len(d))

total = 0
for i in d:
	total = total + i

print(total)

print(np.linalg.norm(d, ord=1))
