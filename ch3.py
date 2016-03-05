# Step 1. View page source
# Step 2. Copy text after <!-- find rar characters in the mess -->, save to ch3.input
# Step 3. Coding

def isChar(c):
	return ord(c) >= ord('a') and ord(c) <= ord('z')

input_file = open('ch3.input', 'r')
text = input_file.read()

for x in range(0, len(text) - 1):
	if (isChar(text[x])):
		print (text[x], end ='')
print ()

