import pygame
import random

width = 1280
height = 720

screen = pygame.display.set_mode((width, height))
scale = pygame.image.load('SCALE.png')

scaleY = -2480

baseSize = [300, 50]
base = [width//2 - baseSize[0]//2, height-baseSize[1]-200]

gr = [0, base[1]+baseSize[1]]
grSize = [width, height]

block1 = [width, height-2*baseSize[1]-200]
blockSize1 = baseSize[0]

block2 = [-baseSize[0], height-2*baseSize[1]-200]
blockSize2 = baseSize[0]

blocks = []
sizes = []


screencol = (100, 100, 100)
blockcol1 = (255, 0, 0)
blockcol2 = (0, 255, 0)
blockcol3 = (0, 0, 255)
grcol = (0, 105, 0)

blockSpeed = 0.5

switch = True
alive = True
b = True
c = False


def move1():
	block1[0] -= blockSpeed

def move2():
	block2[0] += blockSpeed

def back1():
	global block1
	block1 = [width, height-3*baseSize[1]-200]

def back2():
	global block2
	block2 = [-blockSize2, height-3*baseSize[1]-200]

def step():
	global scaleY
	base[1] += baseSize[1]
	gr[1] += baseSize[1]
	block1[1] += baseSize[1]
	block2[1] += baseSize[1]
	for i in range(len(blocks)):
		blocks[i][1] += baseSize[1]
	scaleY += baseSize[1]
	

def cut1():
	global blockSize1, blockSize2, block1, block2, b
	if b:
		b = False
		if block1[0] < base[0]:
			blockSize1 -= base[0] - block1[0]
			block1[0] = base[0]
		if block1[0]+blockSize1 > base[0]+baseSize[0]:
			blockSize1 += (base[0]+baseSize[0]) - (block1[0]+blockSize1)
	else:
		if block1[0] < block2[0]:
			blockSize1 -= block2[0] - block1[0]
			block1[0] = block2[0]
		if block1[0]+blockSize1 > block2[0]+blockSize2:									
			blockSize1 += (block2[0]+blockSize2) - (block1[0]+blockSize1)
	
def cut2():
	global blockSize1, blockSize2, block1, block2

	if block2[0] < block1[0]:
		blockSize2 -= block1[0] - block2[0]
		block2[0] = block1[0]
	if block2[0]+blockSize2 > block1[0]+blockSize1:
		blockSize2 += (block1[0]+blockSize1) - (block2[0]+blockSize2)
	
def dead():
	global blockSpeed, alive, scaleY
	blockSpeed = 0
	alive = False
	while base[1] > height-baseSize[1]-200:
		screen.fill(screencol)
		screen.blit(scale, (base[0]+baseSize[0], scaleY))
		pygame.draw.rect(screen, grcol, (gr, grSize))
		pygame.draw.rect(screen, blockcol2, (base, baseSize))
		pygame.draw.rect(screen, blockcol1, (block1, [blockSize1, baseSize[1]]))
		pygame.draw.rect(screen, blockcol2, (block2, [blockSize2, baseSize[1]]))
		for i in range(len(blocks)):
			blocks[i][1] -= 0.3
			pygame.draw.rect(screen, blockcol3, (blocks[i], [sizes[i], baseSize[1]]))
		pygame.display.flip()
		base[1] -= 0.3
		gr[1] -= 0.3
		scaleY -= 0.3
		if switch: block2[1] -= 0.3
		else: block1[1] -= 0.3
	pygame.quit()



pygame.init()
while True:
	screen.fill(screencol)
	screen.blit(scale, (base[0]+baseSize[0], scaleY))
	pygame.draw.rect(screen, grcol, (gr, grSize))
	pygame.draw.rect(screen, blockcol2, (base, baseSize))
	pygame.draw.rect(screen, blockcol1, (block1, [blockSize1, baseSize[1]]))
	pygame.draw.rect(screen, blockcol2, (block2, [blockSize2, baseSize[1]]))
	for i in range(len(blocks)):
		pygame.draw.rect(screen, blockcol3, (blocks[i], [sizes[i], baseSize[1]]))
	pygame.display.flip()
	
	if switch: move1()
	else: move2()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				if alive:
					if c:
						if block2[0]+blockSize2 < block1[0] or block2[0] > block1[0]+blockSize1: dead()
					else: c = True	
					switch = not switch
					if switch:
						blocks.append(block1)
						sizes.append(blockSize1)
						cut2()
						back1()
					else:
						blocks.append(block2)
						sizes.append(blockSize2)
						cut1()
						back2()
					step()
					

				



	
	
	
	
