import pygame
import random
import math

screen = pygame.display.set_mode((800, 800))

block2img = pygame.image.load('2.png')
block4img = pygame.image.load('4.png')
block8img = pygame.image.load('8.png')
block16img = pygame.image.load('16.png')
block32img = pygame.image.load('32.png')
block64img = pygame.image.load('64.png')

cells = ((0,0), (200, 0), (400,0), (600, 0), (0,200), (200, 200), (400,200), (600, 200), (0,400), (200, 400), (400,400), (600, 400), (0,600), (200, 600), (400,600), (600, 600))
freeBl = []
nums = (block2img, block4img, block8img, block16img, block32img, block64img)

mat = [[0, 0, 2, 0],
       [0, 0, 0, 0],
       [0, 0, 2, 0],
       [0, 0, 0, 0]]

play = True
count = 0



def down():
    global free, freeBl
    free = 3
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[3-j][i] != 0:
                b = mat[3-j][i]
                mat[3-j][i] = 0
                mat[free][i] = b
                free -= 1   
        free = 3
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[2-j][i] == mat[3-j][i]:
                mat[3-j][i] *= 2
                mat[2-j][i] = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[3-j][i] != 0:
                b = mat[3-j][i]
                mat[3-j][i] = 0
                mat[free][i] = b
                free -= 1
            if mat[i][j] == 0:
                freeBl.append([i, j])
        free = 3
   
def up():
    global free, freeBl
    free = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[j][i] != 0:
                b = mat[j][i]
                mat[j][i] = 0
                mat[free][i] = b
                free += 1
        free = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[j-1][i] == mat[j][i]:
                mat[j][i] *= 2
                mat[j-1][i] = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[j][i] != 0:
                b = mat[j][i]
                mat[j][i] = 0
                mat[free][i] = b
                free += 1
            if mat[i][j] == 0:
                freeBl.append([i, j])
        free = 0

def left():
    global free, freeBl
    free = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] != 0:
                b = mat[i][j]
                mat[i][j] = 0
                mat[i][free] = b
                free += 1
        free = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j-1] == mat[i][j]:
                mat[i][j] *= 2
                mat[i][j-1] = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] != 0:
                b = mat[i][j]
                mat[i][j] = 0
                mat[i][free] = b
                free += 1
            if mat[i][j] == 0:
                freeBl.append([i, j])
        free = 0

def right():
    global free, freeBl
    free = 3
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][3-j] != 0:
                b = mat[i][3-j]
                mat[i][3-j] = 0
                mat[i][free] = b
                free -= 1
        free = 3
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][2-j] == mat[i][3-j]:
                mat[i][3-j] *= 2
                mat[i][2-j] = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][3-j] != 0:
                b = mat[i][3-j]
                mat[i][3-j] = 0
                mat[i][free] = b
                free -= 1
            if mat[i][j] == 0:
                freeBl.append([i, j])
        free = 3

def fill():
    global freeBl
    if len(freeBl) > 0:
        ch = random.randint(0, len(freeBl)-1)
        mat[freeBl[ch][0]][freeBl[ch][1]] = 2
        freeBl = []

def check():
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if len(freeBl) == 0:
                if mat[i][j] == mat[i][j-1] or mat[j][i] == mat[j][i-1]:
                    return True
                return False
            return True


pygame.init()
while play:
    screen.fill((100, 100, 100))
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] != 0:
                screen.blit(nums[int(math.log(mat[i][j], 2))-1], cells[i*4+j])
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
		
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                down()
            if event.key == pygame.K_w:
                up()
            if event.key == pygame.K_d:
                right()
            if event.key == pygame.K_a:
                left()
            play = check()
            fill()



