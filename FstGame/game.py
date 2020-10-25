import pygame
import os

pygame.init()

WIDTH = 500
HEIGHT = 480

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")

walkRight = [pygame.image.load(os.path.join("imgs",'R1.png')), pygame.image.load(os.path.join("imgs",'R2.png')), pygame.image.load(os.path.join("imgs",'R3.png')), pygame.image.load(os.path.join("imgs",'R4.png')), pygame.image.load(os.path.join("imgs",'R5.png')), pygame.image.load(os.path.join("imgs",'R6.png')), pygame.image.load(os.path.join("imgs",'R7.png')), pygame.image.load(os.path.join("imgs",'R8.png')), pygame.image.load(os.path.join("imgs",'R9.png'))]
walkLeft = [pygame.image.load(os.path.join("imgs",'L1.png')), pygame.image.load(os.path.join("imgs",'L2.png')), pygame.image.load(os.path.join("imgs",'L3.png')), pygame.image.load(os.path.join("imgs",'L4.png')), pygame.image.load(os.path.join("imgs",'L5.png')), pygame.image.load(os.path.join("imgs",'L6.png')), pygame.image.load(os.path.join("imgs",'L7.png')), pygame.image.load(os.path.join("imgs",'L8.png')), pygame.image.load(os.path.join("imgs",'L9.png'))]
bg = pygame.image.load(os.path.join("imgs",'bg.jpg'))
char = pygame.image.load(os.path.join("imgs",'standing.png'))

clock = pygame.time.Clock()

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y+11, 29, 52) #rectangle

    def draw(self,win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0],(self.x,self.y))
            else:
                win.blit(walkLeft[0],(self.x,self.y))
        self.hitbox = (self.x + 17, self.y+11, 29, 52)
        pygame.draw.rect(win, (255,0,0), self.hitbox,2)

class enemy(object):
    walkRight = [pygame.image.load(os.path.join("imgs",'R1E.png')), pygame.image.load(os.path.join("imgs",'R2E.png')), pygame.image.load(os.path.join("imgs",'R3E.png')), pygame.image.load(os.path.join("imgs",'R4E.png')), pygame.image.load(os.path.join("imgs",'R5E.png')), pygame.image.load(os.path.join("imgs",'R6E.png')), pygame.image.load(os.path.join("imgs",'R7E.png')), pygame.image.load(os.path.join("imgs",'R8E.png')), pygame.image.load(os.path.join("imgs",'R9E.png')), pygame.image.load(os.path.join("imgs",'R10E.png')), pygame.image.load(os.path.join("imgs",'R11E.png'))]
    walkLeft  = [pygame.image.load(os.path.join("imgs",'L1E.png')), pygame.image.load(os.path.join("imgs",'L2E.png')), pygame.image.load(os.path.join("imgs",'L3E.png')), pygame.image.load(os.path.join("imgs",'L4E.png')), pygame.image.load(os.path.join("imgs",'L5E.png')), pygame.image.load(os.path.join("imgs",'L6E.png')), pygame.image.load(os.path.join("imgs",'L7E.png')), pygame.image.load(os.path.join("imgs",'L8E.png')), pygame.image.load(os.path.join("imgs",'L9E.png')),pygame.image.load(os.path.join("imgs",'L10E.png')),pygame.image.load(os.path.join("imgs",'L11E.png'))]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkcount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)

    def draw(self, win):
        self.move()
        if self.walkcount + 1 >= 33:
            self.walkcount = 0
        if  self.vel > 0:
            win.blit(self.walkRight[self.walkcount //3], (self.x, self.y))
            self.walkcount += 1
        else:
            win.blit(self.walkLeft[self.walkcount //3], (self.x, self.y))
            self.walkcount += 1
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkcount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkcount = 0

    def hit(self):
        print("hit")
        pass



class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing # 1 or -1
        self.vel = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)


def redrawGameWindow():
    win.blit(bg, (0,0))
    man.draw(win)
    enemy.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


#mainloop
man = player(300,410,64,64)
enemy = enemy(100,410,64,64,450)
shootLoop = 0
bullets = []
run = True
while run:
    clock.tick(27)

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    for bullet in bullets:
        if bullet.y - bullet.radius < enemy.hitbox[1] + enemy.hitbox[3] and bullet.y + bullet.radius > enemy.hitbox[1]:
            if bullet.x + bullet.radius > enemy.hitbox[0] and bullet.x - bullet.radius < enemy.hitbox[0] + enemy.hitbox[2]:
                enemy.hit()
                bullets.pop(bullets.index(bullet))

        if bullet.x < WIDTH and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        if man.left:
            facing = -1
        else:
            facing = 1
            
        if len(bullets) < 5:
            bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))
        
        shootLoop = 1

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False

    elif keys[pygame.K_RIGHT] and man.x < WIDTH - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False

    else:
        man.standing = True
        man.walkCount = 0
    
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
        
    redrawGameWindow()


pygame.quit()