from PIL import Image

image = Image.open("cave.jpg")
odd_img = Image.new('RGB', image.size, 'Black')
even_img = Image.new('RGB', image.size, 'Black')
img = image.load()
odd_pxl = odd_img.load()
even_pxl = even_img.load()

print (image.size)

for i in range(image.size[0]):
	for j in range(image.size[1]):
		if ((i + j) % 2 == 1):
			odd_pxl[i, j] = img[i, j]
		else:
			even_pxl[i, j] = img[i, j]

odd_img.save('odd.jpg')
even_img.save('even.jpg')
