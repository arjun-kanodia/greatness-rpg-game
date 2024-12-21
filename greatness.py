import pygame
from pygame.locals import *
import sys
import random
from tkinter import filedialog
from tkinter import *
 # Position and dire
pygame.init()
vec = pygame.math.Vector2
HEIGHT = 350
WIDTH = 435
ACC = 0.5
FRIC = -0.12
FPS = 60
FPS_CLOCK = pygame.time.Clock()
COUNT = 0
displaysurface=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Greatness")
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rawimage = pygame.image.load("left.png")
        self.size = self.rawimage.get_size()
        self.image = pygame.transform.scale(self.rawimage, (int(self.size[0]*0.5), int(self.size[1]*0.5)))
        self.image2 = pygame.image.load("right.png")
        self.rect = self.image.get_rect()
        self.vx = 0
        self.pos = pygame.math.Vector2((340, 240))
        self.vel = pygame.math.Vector2(0,0)
        self.acc = pygame.math.Vector2(0,0)
        self.direction = "RIGHT"
        self.playerflipped=False
    def move(self):
        pressed_keys=pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.acc.y = -ACC
        if pressed_keys[K_DOWN]:
            self.acc.y = ACC
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
            self.image=pygame.image.load("left.png")
            self.image = pygame.transform.scale(self.image, (int(self.size[0]*0.5), int(self.size[1]*0.5)))
            self.playerflipped=False
        if pressed_keys[K_RIGHT]:    
            self.acc.x = ACC
            self.image=pygame.image.load("right.png")
            self.image = pygame.transform.scale(self.image, (int(self.size[0]*0.5), int(self.size[1]*0.5)))
            self.playerflipped=True
        self.acc.x += self.vel.x * FRIC
        self.acc.y += self.vel.y * FRIC
        self.vel += self.acc
        if abs(self.vel.x) < 0.5:
             self.vel.x=0
             self.acc.x=0
        self.pos += self.vel + 0.2 * self.acc
        if abs(self.vel.y) < 0.5:
             self.vel.y=0
             self.acc.y=0
        # looping
        if self.pos.x > WIDTH-1:
            self.vel.x = 0
        if self.pos.x < 0:
            self.vel.x = 0
        
        if self.pos.y > HEIGHT-1:
             self.vel.y=0
        if self.pos.y < 0:
             self.vel.y = 0
    
        
        self.rect.midbottom = self.pos 
    def attack(self):
        pass
class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  
        self.bgimage = pygame.image.load("pixil-frame-0 (1).png")
        self.bgX = 0
        self.bgY = 0
    def render(self):
        displaysurface.blit(self.bgimage, (self.bgX, self.bgY))
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
         super().__init__()
         self.bouncing=False
         self.image = pygame.image.load("enemy-removebg-preview.png")
         self.rect = self.image.get_rect()
         self.pos=vec(random.randint(0,350),random.randint(0,435))
         self.vel=vec(0,0)  
         self.acc=vec(0,0)    
         self.direction = random.randint(0,1)
         self.vel.x = random.randint(2,6) / 2
         self.delete=False
        #  if self.direction == 0:
        #     self.pos.x = 0
        #     self.pos.y = 0
        #  if self.direction ==1:
        #     self.pos.x = 700
        #     self.pos.y = 235
     
    def enemymove(self):
        self.movementx=player.pos.x-self.pos.x
        self.movementy=player.pos.y-self.pos.y
        if(self.movementx>0 and self.movementy>0):
            self.acc.x=ACC*0.5
            self.acc.y=ACC*0.5
        if(self.movementx<0 and self.movementy>0):
             self.acc.x=ACC*-0.5
             self.acc.y=ACC*0.5
        if(self.movementx>0 and self.movementy<0):
             self.acc.x=ACC*0.5
             self.acc.y=ACC*-0.5
        if(self.movementx<0 and self.movementy<0):
             self.acc.x=ACC*-0.5
             self.acc.y=ACC*-0.5
        if self.bouncing==True:
            self.vel=-self.vel*random.randint(2,5)*1
        self.acc.x += self.vel.x * FRIC
        self.acc.y += self.vel.y * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos
        #          print("enemy1 bouncing = " , enemy.bouncing)
        #     # self.acc.x = self.vel.x * FRIC
        #     # self.acc.y = self.vel.y * FRIC
        #          if self.vel.x<0:
        #             self.pos.x+=60
        # if self.vel.x>0:
        #     self.pos.x-=60
        # if self.vel.y<0:
        #     self.pos.y+=60
        # if self.vel.y>0:
        #     self.pos.y-=60
        # if self.pos.x<0:
        #     self.pos.x=0
        # if self.pos.x>WIDTH-50:
        #     self.pos.x=WIDTH-50
        # if self.pos.y<0:
        #     self.pos.y=0
        # if self.pos.y>HEIGHT-70:
        #     self.pos.y=HEIGHT-70   
            
        #     self.rect.midbottom = self.pos
        #     self.vel=-self.vel
        # if self.bouncing==False:
            # self.acc.x += self.vel.x * FRIC
            # self.acc.y += self.vel.y * FRIC
            # self.vel += self.acc
            # self.pos += self.vel + 0.5 * self.acc
            # self.rect.midbottom = self.pos
            # print(self.bouncing)
            # print("enemy1 vel = " ,enemy.vel)
            # print("enemy1 pos = " ,enemy.pos)
            # print("enemy2 vel = " ,enemy2.vel)
            # print("enemy2 pos = " ,enemy2.pos)

    def enemyrender1(self):
        displaysurface.blit(self.image, (self.pos.x, self.pos.y))

    def enemyrender2(self):
        displaysurface.blit(self.image, (self.pos.x, self.pos.y))
     
enemy=Enemy()

def update(self):
            pass 

def attack(self):
    # pressed_keys=pygame.key.get_pressed() 
    # if pressed_keys[K_SPACE]:
    #     enemy = background.render()
    pass
def jump(self):
             pass
def enemydelete(self):
 pressed_keys=pygame.key.get_pressed() 
 if pressed_keys[K_SPACE]:
    del enemy

    
            
background = Background()  
player=Player() #adds instance of the player class
enemy=Enemy()
enemy2=Enemy()
displaysurface.blit(player.image, player.rect) #displays the player
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.key==pygame.K_SPACE:
            display.rect = True
    Color=(255,0,0)
    enemyhitbox=pygame.draw.rect(displaysurface,Color, pygame.Rect(enemy.pos.x-20,enemy.pos.y-30, 110, 130))
    enemy2hitbox=pygame.draw.rect(displaysurface,Color, pygame.Rect(enemy2.pos.x-20,enemy2.pos.y-30, 110, 130))
    collide=pygame.Rect.colliderect(enemyhitbox,enemy2hitbox)
    background.render()
    if player.playerflipped==False:
        playerhitbox=pygame.draw.rect(displaysurface,Color, pygame.Rect(player.pos.x-40,player.pos.y-60, 40, 60))
    else:  
        playerhitbox=pygame.draw.rect(displaysurface,Color, pygame.Rect(player.pos.x+5,player.pos.y-60, 40, 60))
    playercollide1=pygame.Rect.colliderect(enemyhitbox,playerhitbox)
    playercollide2=pygame.Rect.colliderect(enemy2hitbox,playerhitbox)
    if collide:
         enemy.bouncing=True
         enemy2.bouncing=True
    if collide==False:
         enemy.bouncing=False
         enemy2.bouncing=False
    
    if (playercollide1==True):
        enemy.delete=True
    if (playercollide2==True):
        enemy2.delete=True
    displaysurface.blit(player.image, player.rect)
    player.move()
    enemy.enemymove()
    if(enemy.delete==False):
        displaysurface.blit(enemy.image, enemy.rect)
    enemy2.enemymove()
    if(enemy2.delete==False):
        displaysurface.blit(enemy2.image, enemy2.rect)
    pygame.display.update()
    FPS_CLOCK.tick(FPS)