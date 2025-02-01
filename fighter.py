import pygame
b = True
d = False
g = True
f = True
s = False
c = 300
class GG():
    
    def __init__(self, hp, damage, x, y, speedX, speedx, speedY, backspeed, sizeX, sizeY, jump, isdrop, isatk, atk, atkrange, isalive, isdown, isup):
        self.hp = hp
        self.damage = damage
        self.x = x
        self.y = y
        self.speedX = speedX
        self.speedx = speedx
        self.speedY = speedY
        self.backspeed = backspeed
        self.width = sizeX
        self.height = sizeY
        self.isjump = jump
        self.isdrop = isdrop
        self.isatk = isatk
        self.atk = atk
        self.atkrange = atkrange
        self.isalive = isalive
        self.isdown = isdown
        self.isup = isup

    def jump(self):
        if self.isjump:
            self.speedY += 0.01
    
    def stop(self, e):
        global b, d, g, f, s
        try:
            e.hp
            if e.x - self.width <= self.x <= e.x + e.width and e.y -self.height < self.y < e.y + e.height:
                self.isdrop = True
                b = True
                hit(e, self)
        except AttributeError:
            
            if e.x - self.width <= self.x <= e.x + e.width and e.y -self.height < self.y < e.y + e.height:
                self.backspeed = 0
                g = True
                f = True
                s = True
            if -1 < self.y + self.height - e.y < 7 and e.x - self.width <= self.x <= e.x + e.width and e.y -self.height < self.y < e.y + e.height and self.speedY >= 0:
                if g:
                    self.y = e.y-self.height -1
                    self.speedY = 0
                    g = False
                    self.isjump = False
                #else:
                    #self.isjump = True
            elif self.y+ self.height < e.y and not e.x - self.width <= self.x <= e.x + e.width:
                self.isjump = True
            
            elif -1 < e.y + e.height - self.y < 7 and e.x - self.width+1 <= self.x <= e.x + e.width-1 and e.y -self.height < self.y < e.y + e.height:
                if f:
                    self.y = e.y+e.height +1
                    self.speedY = 0
                    f = False
                else:
                    self.isjump = True
            
            if e.x - self.width <= self.x <= e.x + e.width and e.y -self.height < self.y < e.y + e.height and s:
                self.speedX = 0
                self.speedx = 0

    def attack(self, e):
        global c
        if c < 150:
            if self.isdown:
                sword = Block(self.x+self.width/2-self.height/4, self.y+self.height,  self.height/2, self.atkrange)
                pygame.draw.rect(screen, (0, 255, 255), [self.x+self.width/2-self.height/4, self.y+self.height,  self.height/2, self.atkrange])
            elif self.isup:
                sword = Block(self.x+self.width/2-self.height/4, self.y-self.atkrange,  self.height/2, self.atkrange)
                pygame.draw.rect(screen, (0, 255, 255), [self.x+self.width/2-self.height/4, self.y-self.atkrange,  self.height/2, self.atkrange])
            elif self.atk:
                sword = Block(self.x+self.width, self.y+self.height/2, self.atkrange, self.height/2)
                pygame.draw.rect(screen, (0, 255, 255), [self.x+self.width, self.y+self.height/2, self.atkrange, self.height/2])
            else:
                sword = Block(self.x-self.atkrange, self.y+self.height/2, self.atkrange, self.height/2)
                pygame.draw.rect(screen, (0, 255, 255), [self.x-self.atkrange, self.y+self.height/2, self.atkrange, self.height/2])
            if e.stop(sword) and self.isatk:
                if self.isdown:
                    self.speedY = -2
                    self.isjump = True
                hit(self, e)
                print(e.hp)
            self.isatk = False
        if c <= 300:
            c += 1


            

    def drop(self, e):
        global b
        if self.isdrop:
            if not self.x + self.width/2 < e.x + e.width/2:
                self.backspeed = -self.backspeed
            if self.speedY > 0:
                self.speedY = -self.speedY
                if self.speedY < -2:
                    self.speedY = -2
            if b:
                self.backspeed = -2.5
                b = False
            else:
                self.backspeed += 0.01
            if self.backspeed >= 0:
                    self.isdrop = False
                    self.backspeed = 0
            if not self.x + self.width/2 < e.x + e.width/2:
                self.backspeed = -self.backspeed
                
                
    def moving(self):
        global c
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.speedX = 0.8
                if event.key == pygame.K_a:
                    self.speedx = -0.8
                if event.key == pygame.K_s:
                    self.isdown = True
                elif event.key == pygame.K_w:
                    self.isup = True
                if event.key == pygame.K_SPACE and not self.isjump:
                    self.isjump = True
                    self.speedY = -3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.speedX = 0
                if event.key == pygame.K_a:
                    self.speedx = 0
                if event.key == pygame.K_s:
                    self.isdown = False
                elif event.key == pygame.K_w:
                    self.isup = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if c > 300:
                    c = 0
                    self.isatk = True
                    if pygame.mouse.get_pos()[0] >= self.x + self.width/2:
                        self.atk = True
                    else:
                        self.atk = False
    def dead(self):
        if self.hp <= 0:
            self.isalive = False

                


class Enemy():

    def __init__(self, hp, damage, x, y, speedX, speedY, sizeX, sizeY):
        self.hp = hp
        self.damage = damage
        self.x = x
        self.y = y
        self.speedX = speedX
        self.speedY = speedY
        self.width = sizeX
        self.height = sizeY
    
    def stop(self, e):
        if e.x - self.width <= self.x <= e.x + e.width and e.y -self.height < self.y < e.y + e.height:
            return True
        return False

    

class Block():

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.height = height
        self.width = width

def hit(one, two):
    two.hp -= one.damage

screenH = 1080
screenW = 1920

screen = pygame.display.set_mode((screenW, screenH))

ground = Block(0, 800, screenW, 280)
block = Block(1000, 199, 300, 500)
hero = GG(hp = 5, damage = 1, x = 500, y = 700, speedX = 0, speedx = 0, speedY = 0, backspeed = 0, sizeX = 70, sizeY = 100, jump = False, isdrop = False, isatk = False, atk = False, atkrange = 200, isalive = True, isdown = False, isup = False)
enemy = Enemy(20, 1, 1400, 600, 0, 0, 140, 200)


pygame.init()
while True:
    screen.fill((60, 60, 60))
    pygame.draw.rect(screen, (100, 100, 100), [ground.x, ground.y, ground.width, ground.height])
    if hero.isalive:
        pygame.draw.rect(screen, (255, 0, 0), [hero.x, hero.y, hero.width, hero.height])
    pygame.draw.rect(screen, (0, 255, 0), [enemy.x, enemy.y, enemy.width, enemy.height])
    #pygame.draw.rect(screen, (100, 100, 255), [block.x, block.y, block.width, block.height])
    pygame.draw.rect(screen, (0, 0, 0), [45, 45, 510, 60])
    pygame.draw.rect(screen, (200, 0, 0), [50, 50, hero.hp*100, 50])
    hero.attack(enemy)
    pygame.display.flip()

    hero.x += hero.speedX
    hero.x += hero.speedx
    hero.y += hero.speedY
    hero.x += hero.backspeed
    enemy.x += enemy.speedX
    enemy.y += enemy.speedY

    if hero.isalive:
        hero.jump()
        hero.stop(enemy)
        #hero.stop(block)
        hero.stop(ground)
        hero.drop(enemy)
        hero.dead()
    
        hero.moving()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    

