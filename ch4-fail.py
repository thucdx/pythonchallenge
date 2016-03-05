def isSmall(c):
	return ord(c) >= ord('a') and ord(c) <= ord('z')

def isBig(c):
	return ord(c) >= ord('A') and ord(c) <= ord('Z')

input = open("ch4.input", "r")

lines = []

for line in input:
	lines.append(line)	

row, col = len(lines), len(lines[0])
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for r in range(row):
	for c in range(col):
		if (isSmall(lines[r][c])):
			total, guard = 0, 0
			for i in range(4):
				nc, nr = c + dc[i], r + dr[i]
				if (nc >= 0 and nc < col and nr >= 0 and nr < row):
					guard += 1
					if (isBig(lines[nr][nc])):
						total += 1
				
			if (total == 3 and guard == 3):
#				print (r, ' ', c)
				print (lines[r][c], end = '')	

print ()
