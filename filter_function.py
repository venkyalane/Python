import random
import string
raw_data = []
while True:
	n = int(input("How many int element you want to add: "))
	int_start = int(input("Enter Random int start numuber:"))
	int_stop = int(input("Enter Random int stop numuber:"))
	for i in range(n):
		raw_data.append(random.randint(int_start,int_stop))

	m = int(input("How many str element you want to add: "))
	for i in range(m):
		raw_data.append(random.choice(string.ascii_letters))
	
	exit = input("Want to exit?(y/n): ")
	if exit == 'y':
		break
	else:
		continue

print("raw data: \n", raw_data)
filtered_data_str = list(filter(lambda s: (type(s) is str), raw_data))
print("str filtered data: \n",filtered_data_str)
filtered_data_int = list(filter(lambda s: (type(s) is int), raw_data))
print("int filtered data: \n",filtered_data_int)
