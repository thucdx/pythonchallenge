import urllib.request

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
num = '12345'
last_num = 0
divided_by_two = False

while True:
	with urllib.request.urlopen(url % num) as response:
		last_num = int(num)
		html = response.read().decode('utf-8')
		num = html.rsplit(None, 1)[-1]
		print (html, ' -> ', num)
		if (num[0] < '0' or num[0] > '9'):
			if divided_by_two == False:
				num = last_num / 2
				divided_by_two = True
			else:
				print ("Result: ", num)
				break


