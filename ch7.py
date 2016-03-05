import zipfile

with zipfile.ZipFile('channel.zip', 'r') as myzip:
	
	lines = myzip.open('readme.txt').readlines()
	name = lines[2].decode('utf-8').rsplit(None, 1)[-1]
	print (name)
	info = []
	
	while True:
		content = myzip.open("%s.txt" % name).read().decode('utf-8')
		print (content)
		name = content.rsplit(None, 1)[-1]
		print (name)
		if (name[0] < '0' or name[0] > '9'):
			break
		info.append(myzip.getinfo("%s.txt" % name).comment.decode('utf-8'))

for c in info:
	print(c, end='')
