import pickle, urllib.request

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
text = urllib.request.urlopen(url).read()
data = pickle.loads(text)

print (data)
for line in data:
	print (''.join(e[0] * e[1] for e in line))

