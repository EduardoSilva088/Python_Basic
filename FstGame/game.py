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

    def draw(self,win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1
        else:
            win.blit(char, (self.x,self.y))

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
    pygame.display.update()


#mainloop
man = player(300,410,64, 64)
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False

    elif keys[pygame.K_RIGHT] and man.x < WIDTH - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
    else:
        man.right = False
        man.left = False
        man.walkCount = 0
    
    if not(man.isJump):
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right = False
            man.left = False
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
