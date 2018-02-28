#Aninda Aminuzzaman
#1001018367

import numpy as np


my_file = open('data-communications.csv', 'r')

result = my_file.readlines()

for line in result:
	sets = line.split(",")

pulse0 = np.ones(10)
#print(pulse0)
pulse0 = pulse0/np.linalg.norm(pulse0)
#print(pulse0)
pulse1 = np.append(np.ones(5), -1*np.ones(5))
#print(pulse1)
pulse1 = pulse1/np.linalg.norm(pulse1)
#print(pulse1)

binary_list = []
neg = 0
for i in range(0,len(sets)):
	if ((i+1) % 10) != 0:
		if float(sets[i]) < 0:
			neg = neg + 1
	else:
		if neg >= 3:
			binary_list.append('1')
			neg = 0
		else:
			binary_list.append('0')
			neg = 0

#del binary_list[0]
#print(binary_list)

bin_asci = []
temp = ""

for i in range(0, len(binary_list)):
	if ((i) % 8) != 0:
		temp = temp + binary_list[i]
	else:
		bin_asci.append(temp)
		temp = ""

#print(bin_asci)

letters = []
for item in bin_asci:
	if item is '':
		continue
	else:
		letters.append(chr(int(item, 2)))

#print(letters)

final_string = ""

for item in letters:
	final_string = final_string + item

print(final_string)
