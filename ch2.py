def origin(char, shift):
	num = ord(char)
	if (num >= ord('a') and num <= ord('z')):
		return chr(ord('a') + (num - ord('a') + shift) % (ord('z') - ord('a') + 1))
	else:
		return chr(num)

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

i = 0
while i < len(text):
	print (origin(text[i], 2), end='')
	i += 1
print ()

# After running, we know we should apply the function to 'url'
url = "map"
i = 0
while i < len(url):
	print (origin(url[i], 2), end='')
	i += 1
print()
