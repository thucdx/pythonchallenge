# Conway sequence

num = '1'
step = 0

while step < 30:
	new_num = ""
	count = 0
	last = '-'

	for i in range(len(num)):
		if (num[i] == last):
			count += 1
		else:
			if (last != '-'):
				new_num += str(count) + str(last)
			count = 1
			last = num[i]
	new_num += str(count) + str(last)
	num = new_num
	step += 1

print (len(num))
