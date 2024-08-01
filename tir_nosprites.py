import pygame
import random

screen = pygame.display.set_mode((1280, 720))

col1 = 0, 0, 0
col2 = 255, 255, 255
col3 = 60, 60, 60
col4 = 255, 0, 0

charSize = 60
enemySize = 60
shootSize = 20
charX = 1280/2 - charSize//2
charY = 720/2 - charSize//2
charSpeedX = 0
charSpeedY = 0
shootX = charX+charSize//2-shootSize//2
shootY = charY+charSize//2-shootSize//2
shootSpeedX = 0
shootSpeedY = 0
enemyX = 1
enemyY = 1
markX = 510
markY = 265
enemySpeed = 0

check = True
playing = False
menu = True
difscreen = False

opt = 1
dif = 1




pygame.init()
while menu:
	screen.fill((col2))
	pygame.draw.rect(screen, col3, [540, 240, 200, 50])
	pygame.draw.rect(screen, col3, [540, 360, 200, 50])
	pygame.draw.rect(screen, col3, [540, 480, 200, 50])
	pygame.draw.circle(screen, col4, [markX, markY], 25)
	pygame.display.flip()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			 
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN and opt < 3:
				opt += 1
				markY += 120
			if event.key == pygame.K_UP and opt > 1:
				opt -= 1
				markY -= 120
			if event.key == pygame.K_RETURN:
				if opt == 1: 

					playing = True
					while playing:
						screen.fill((col2))
						pygame.draw.rect(screen, col1, [shootX, shootY, shootSize, shootSize])
						pygame.draw.rect(screen, col3, [charX, charY, charSize, charSize])
						pygame.draw.rect(screen, col4, [enemyX, enemyY, enemySize, enemySize  ])
	
	
						pygame.display.flip()
	
						#ограничение поля
						if charX >= 1280-charSize:  
							charX = 1280-charSize-1
							charSpeedX = 0
						elif charX <= 0:
							charX = 1
							charSpeedX = 0 
						if charY >= 720-charSize: 
							charY = 720-charSize-1
							charSpeedY = 0
						elif charY <= 0:
							charY = 1
							charSpeedY = 0

						if dif != 1:
							if enemyX < charX:
								enemyX += enemySpeed
							elif enemyX > charX:
								enemyX -= enemySpeed
							if enemyY < charY:
								enemyY += enemySpeed
							elif enemyY > charY:
								enemyY -= enemySpeed


						if enemyX >= 1280-enemySize: enemyX -= 1
						elif enemyX <= 0: enemyX += 1
						elif enemyY >= 720-enemySize: enemyY -= 1
						elif enemyY <= 0: enemyY += 1
	
						#выстрелы
						if shootX>1280 or shootX<-shootSize or shootY>720 or shootY<-shootSize:
							shootX = charX+charSize//2-shootSize//2
							shootY = charY+charSize//2-shootSize//2
							shootSpeedX = 0
							shootSpeedY = 0
							check = True

						if enemyX-shootSize <= shootX < shootX+shootSize <= enemyX+enemySize+shootSize and enemyY-shootSize <= shootY < shootY+shootSize <= enemyY+enemySize+shootSize:
							enemyX = random.randint(0, 1280-enemySize)
							enemyY = random.randint(0, 720-enemySize)
							if enemyX-charSize <= charX < charX+charSize <= enemyX+enemySize+charSize and enemyY-charSize <= charY < charY+charSize <= enemyY+enemySize+charSize:
								enemyX = random.randint(0, 1280-enemySize)
								enemyY = random.randint(0, 720-enemySize)
	
						if check:
							shootX = charX + charSize//2-shootSize//2
							shootY = charY + charSize//2-shootSize//2

						#столкновения	
						if enemyX-charSize <= charX < charX+charSize <= enemyX+enemySize+charSize and enemyY-charSize <= charY < charY+charSize <= enemyY+enemySize+charSize:
							charSpeedX = 0
							charSpeedY = 0	
							charX = 1280/2 - charSize//2
							charY = 720/2 - charSize//2
							shootSpeedX = 0
							shootSpeedY = 0
							shootX = charX+charSize//2-shootSize//2
							shootY = charY+charSize//2-shootSize//2
							enemyX = 1
							enemyY = 1
							check = True
							playing = False

	

						#движения	
						charX += charSpeedX
						charY += charSpeedY
						shootX += shootSpeedX
						shootY += shootSpeedY
	
	
						for event in pygame.event.get():
							if event.type == pygame.QUIT:
								pygame.quit()
		
							if event.type == pygame.KEYDOWN:
								if event.key == pygame.K_s:
									charSpeedY = 0.7
								if event.key == pygame.K_w:
									charSpeedY = -0.7
								if event.key == pygame.K_d:
									charSpeedX = 0.7
								if event.key == pygame.K_a:
									charSpeedX = -0.7
				
								if shootSpeedX == 0 and shootSpeedY == 0:		
									if event.key == pygame.K_UP:
										check = False
										shootSpeedY = -1.2
									if event.key == pygame.K_DOWN:
										check = False
										shootSpeedY = 1.2
									if event.key == pygame.K_LEFT:
										check = False
										shootSpeedX = -1.2
									if event.key == pygame.K_RIGHT:
										check = False
										shootSpeedX = 1.2
				
				
							if event.type == pygame.KEYUP:
								if event.key == pygame.K_s:
									charSpeedY = 0
								if event.key == pygame.K_w:
									charSpeedY = 0
								if event.key == pygame.K_d:
									charSpeedX = 0
								if event.key == pygame.K_a:
									charSpeedX = 0 
				elif opt == 2:
					markY = 265
					opt = 1
					difscreen = True
					while difscreen:
						screen.fill((col2))
						pygame.draw.rect(screen, col3, [540, 240, 200, 50])
						pygame.draw.rect(screen, col3, [540, 360, 200, 50])
						pygame.draw.rect(screen, col3, [540, 480, 200, 50])
						pygame.draw.circle(screen, col4, [markX, markY], 25)
						pygame.display.flip()

						for event in pygame.event.get():
							if event.type == pygame.QUIT:
								pygame.quit()
			 
							if event.type == pygame.KEYDOWN:
								if event.key == pygame.K_DOWN and opt < 3:
									opt += 1
									markY += 120
								if event.key == pygame.K_UP and opt > 1:
									opt -= 1
									markY -= 120
								if event.key == pygame.K_RETURN:
									difscreen = False					
									if opt == 1:
										enemySize = 80
										enemySpeed = 0
										dif = 1
									elif opt == 2:
										enemySize = 60
										enemySpeed = 0.2
										dif = 2
									elif opt == 3:
										enemySize = 40
										enemySpeed = 0.5
										dif = 3
									opt = 1
									markY = 265	
				elif opt == 3:
					pygame.quit()
