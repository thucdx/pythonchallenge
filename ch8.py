from PIL import Image

img = Image.open('oxygen.png')
(width, heigh) = img.size
print (width, ' ', heigh)

for i in range(0, width - 1, 7):
	rdpxl = img.getpixel((i, heigh / 2))
	print (chr(rdpxl[0]), end ='')
print ()

encoded = [105, 110, 116, 101, 103, 114, 105, 116, 121]
for e in encoded:
	print (chr(e), end = '')
print()
