#Aninda Aminuzzaman

#1001018367


from scipy import signal
import scipy.io.wavfile
import glob
import numpy as np

song_db = glob.glob('song-*.wav');

test_song = scipy.io.wavfile.read('testSong.wav')

x = test_song[1]
fs = test_song[0]
f, t, Sxx = signal.spectrogram(x, fs=fs, nperseg=0.5*fs)

freq = Sxx.argmax(axis=0)

for j in range(0, len(freq)):
	freq[j] = f[freq[j]]

song_norms = {}

for i in song_db:
	b = scipy.io.wavfile.read(i)
	x = b[1]
	fs = b[0]
	f, t, Sxx = signal.spectrogram(x, fs=fs, nperseg=0.5*fs)

	freq_ind = Sxx.argmax(axis=0)
	for j in range(0, len(freq_ind)):
		freq_ind[j] = f[freq_ind[j]]
	norm = np.linalg.norm(freq_ind - freq, ord=1)
	song_norms[i] = norm

fin = sorted(song_norms.items(), key=lambda x: x[1])

for i in fin:
	print(i[1], "  ", i[0])
