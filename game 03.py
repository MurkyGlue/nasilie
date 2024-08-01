import os
import random
mat = [['@','.','.','.','.','.','.','.','.','.'],
['.','#','.','.','.','.','.','.','.','.'],
['.','.','.','.','.','.','.','.','.','.'],
['.','.','.','.','.','.','.','.','.','.'],
['.','.','.','.','.','.','.','.','.','.'],
['.','.','.','.','.','.','.','.','.','.'],
['.','.','.','.','.','.','.','.','.','.'],
['.','.','.','.','.','.','.','.','.','.'],
['.','.','.','.','.','.','.','.','.','.'],
['.','.','.','.','.','.','.','.','.','.']]

play = True
check = True
check2 = True
while play:
	
	for i in range(len(mat)):
		print(mat[i][0], mat[i][1], mat[i][2], mat[i][3], mat[i][4], mat[i][5], mat[i][6], mat[i][7], mat[i][8], mat[i][9])
		for j in range(len(mat[i])):
			xx = mat[i][j].find('@')
			if xx != -1 and check:
				x = xx
				y = i
				check = False
		for j in range(len(mat[i])):
			xx2 = mat[i][j].find('#')
			if xx2 != -1 and check2:
				x2 = xx
				y2 = i
				check2 = False
				
				
	print(x, y)	
	a = input()
	mat[y][x] = '.'
	if a == 'w':
		mat[y-1][x] = '@'
		y -= 1
	elif a == 's':
		mat[y+1][x] = '@'
		y += 1
	elif a == 'a':
		mat[y][x-1] = '@'
		x -= 1
	elif a == 'd':
		mat[y][x+1] = '@'
		x += 1
	else:
		mat[y][x] = '@'
		
	if x == x2 and y == y2:
		mat[random.randint(9)][random.randint(9)] = '#'
			

		
		

