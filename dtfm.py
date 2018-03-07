#Aninda Aminuzzaman

#1001018367


import numpy as np

import matplotlib.pyplot as plt

#my_file = open('tones-7481414.csv', 'r')
#my_file = open('tones-8675309.csv', 'r')
#my_file = open('tones-7.csv', 'r')
#my_file = open('tones-123456789star0pound.csv', 'r')
#my_file = open('tones-pound0star987654321.csv', 'r')
#my_file = open('tones-poundstarpoundstarpoundstar.csv', 'r')
my_file = open('tones.csv', 'r')

result = my_file.readlines()

for line in result:
	sets = line.split(",")

for i in range(0, len(sets)):
	sets[i] = float(sets[i])
print(len(sets))

#a = sets[:4000]
#b = sets[4000:8000]
fs = 8000
L = 64
h = []


size = len(sets)/4000
size = int(size)

print(size)
keys = {
	'1' : [697, 1209],
	'2' : [697, 1336],
	'3' : [697, 1477],
	'4' : [770, 1209],
	'5' : [770, 1336],
	'6' : [770, 1477],
	'7' : [852, 1209],
	'8' : [852, 1336],
	'9' : [852, 1477],
	'0' : [941, 1336],
	'*' : [941, 1209],
	'#' : [941, 1477]
}


avg_list = []



for i in range(len(sets)):
	sets[i] = np.sin(2 * np.pi * sets[i] / fs)

num_freq = [697, 770, 852, 941, 1209, 1336, 1477]

for j in num_freq:
	for i in range(0, L):
		n = (2* (np.cos((2 * np.pi * j * i)/fs))) / L
		h.append(n)

print('h', len(h));

for k in range(0, size):
	a = sets[k*4000:(k+1)*4000]
	#print(a)
	print(len(a))
	for i in range (0, len(num_freq)):
		f = np.convolve(a, h[i*L:(i+1)*L])
		avg = np.mean(f**2)
		avg_list.append(avg)
		#avg.sort()
		#print(avg)
		#break
ind = []
for k in range(0, size):
	b = avg_list[k* len(num_freq): (k+1)*len(num_freq)]
	#print
#b = avg_list[:7]
	p = b.index(max(b))
	ind.append(b.index(max(b)))
	b.remove(max(b))
	b.insert(p, -9999999999999999)
	ind.append(b.index(max(b)))

print(ind)
print(len(avg_list))

for i in range(0, len(ind)):
	ind[i] = num_freq[ind[i]]
print(ind)
#print(avg_list[7:14])
#print(keys['1'])
plt.plot(f)

ans = ""


for j in range(0, len(ind)):
	a = ind[j * 2: (j+1) *2]
	for i in keys:
	#print (a)
		if len(set(keys[i]) & set(a)) == 2 :
			ans = ans + i
		#break
	#print (keys[i])

print(ans)
#print(a)
#plt.show()

