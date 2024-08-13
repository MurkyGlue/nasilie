import pygame
import random

#screen = pygame.display.set_mode((800, 800))

block2img = pygame.image.load('2.png')
block4img = pygame.image.load('4.png')
block8img = pygame.image.load('8.png')
block16img = pygame.image.load('16.png')
block32img = pygame.image.load('32.png')
block64img = pygame.image.load('64.png')

cells = ((0,0), (200, 0), (400,0), (600, 0), (0,200), (200, 200), (400,200), (600, 200), (0,400), (200, 400), (400,400), (600, 400), (0,600), (200, 600), (400,600), (600, 600))
blocks = []

mat = [[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 2, 2, 0],
       [0, 2, 0, 2]]

free = 3
num = 0
prenum = 0

def down():
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
        free = 3
   
def up():
    global free
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
        free = 0


            




#pygame.init()
while True:
    #screen.fill((100, 100, 100))
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(mat[i][j], end = ' ')
        print()
    print()

    a = input()
    if a == 'w':
        up()
    elif a == 's':
        down()
    elif a == 'd':
        continue
    elif a == 'a':
        continue
    else:
        break

    


