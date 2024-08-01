import pygame
import random
pygame.font.init()
height =720
screen = pygame.display.set_mode((1280,height))

player = [360,360]
barrier1 = [1280,0]
barrier2 = [1280,660]
playerSize = [60,60]
barrier1Size = [60,260]
barrier2Size = [60, 1000]
holeSize = 400


barrierSpeed = 0.2
playerSpeed = [0,0]
recallSpeed = 0.2
gravity = 0.4

backColor = 0, 255, 0
playerColor = 255, 0, 0
barrierColor = 60, 60, 60
scoreColor = 0, 0, 0

score = 0
jumpCount = 2
gravityCount = 0.00000001

x = 0
y = 1

play = True
scoreCheck = True
jump = False


sc = pygame.font.Font(None, 50)


pygame.init()
while play:
	
	scorePrint = sc.render(str(score), True, scoreColor)
	
	screen.fill((backColor))
	pygame.draw.rect(screen,playerColor,[player, playerSize])
	pygame.draw.rect(screen, barrierColor, [barrier1, barrier1Size])
	pygame.draw.rect(screen, barrierColor, [barrier2, barrier2Size])
	screen.blit(scorePrint, (600,670))
	pygame.display.flip()
	
	
	
	barrier1[x] -= barrierSpeed
	barrier2[x] -= barrierSpeed
	player[x] += playerSpeed[x]
	player[y] += playerSpeed[y]
	player[y] += gravity
	
	
	if barrier1[x] <= player[x] and scoreCheck:
		score += 1
		scoreCheck = False

		
	if jump:
		gravity = 0
		gravityCount = 0.01
		player[y] -= jumpCount**2	
		jumpCount -= 0.01
		if jumpCount <= 0:
			jumpCount = 2
			jump = False
	else:
		gravity += 0.002
		
	
	if barrier1[x]-barrier1Size[x] <= player[x] <= barrier1[x]+barrier1Size[x] and not(barrier1[y]+barrier1Size[y] <= player[y] <= barrier2[y]-playerSize[y]):
		break

	
	if not 0 <= player[y] <= height-playerSize[y]:
		break


	if player[x] >= 1280-playerSize[x]:
		player[x] = 1280-playerSize[x]
		playerSpeed[x] = 0
		barrierSpeed = barrierSpeed*2
	elif player[x] <= 0:
		player[x] = 0
		playerSpeed[x] = 0
		barrierSpeed = barrierSpeed/2


	if barrier1[x] <= -(barrier1Size[x]):
		barrier1[x] = 1280
		barrier2[x] = 1280
		barrier1Size[y] = random.randint(10, height-holeSize)
		barrier2[y] = barrier1Size[y]+holeSize
		scoreCheck = True
		
		
	if player[x] > 360:
		player[x] -= recallSpeed
	elif player[x] < 360:
		player[x] += recallSpeed	

	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_d:
				playerSpeed[x] = 0.4
			if event.key == pygame.K_a:
				playerSpeed[x] -= 0.4
			if event.key == pygame.K_SPACE:
				jump = True
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_d:
				playerSpeed[x] = 0	
			if event.key == pygame.K_a:
				playerSpeed[x] = 0		
					
			
