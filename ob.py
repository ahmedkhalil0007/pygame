from hmac import trans_36
import pygame
import random
from pygame.sprite import  Group

SCREEN = WIDTH , HEIGHT = 288 , 512

len_pos = (50,95,124,190)

class player:
    def __init__(self,x,y,type):
        self.image = pygame.image.load(f"cars\{type+1}.png")

        self.image = pygame.transform.scale(self.image,(30 , 82))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y













    def update(self,left,right):
        if left:
            self.rect.x -=1
            if self.rect.x <=45:
                self.rect.x = 45
        if right:
            self.rect.x +=1
            if self.rect.right >=250:
                self.rect.right = 250

    def draw(self,win):
        win.blit(self.image,self.rect)


class Road:
    def __init__(self):
        self.image = pygame.image.load(r"bg/road.png")
        self.image = pygame.transform.scale(self.image,(WIDTH-60,HEIGHT))
        self.move = True
        self.reset()









    def reset(self):
        self.x=30
        self.y1=0
        self.y2= -HEIGHT


    def update(self,speed):
        if self.move:
            self.y1 += speed
            self.y2 += speed
        if self.y1 >= HEIGHT:
            self.y1 = -HEIGHT
        if self.y2 >= HEIGHT:
            self.y2 = -HEIGHT


    def draw(self,win):
        win.blit(self.image,(self.x,self.y1))
        win.blit(self.image,(self.x,self.y2))

class Tree(pygame.sprite.Sprite):
    
    def __init__(self,x,y):
        super(Tree,self).__init__()
        type = random.randint(1,4)
        self.image = pygame.image.load(f"Trees\{type}.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def update(self,speed):
        self.rect.y += speed
        if self.rect.y >= HEIGHT:
            self.kill()
    def draw(self,win):
        win.blit(self.image,self.rect)

class pr(pygame.sprite.Sprite):
    def __init__(self,type):
        super(pr,self).__init__()
        dx = 0
        if type == 1:
            type=random.randint(2,8)
            self.image = pygame.image.load(f"cars\{type+1}.png")
            self.image = pygame.transform.flip(self.image,False , True)
            self.image = pygame.transform.scale(self.image,(24 , 36))

        if type == 2:
            self.image = pygame.image.load(f"cars\{type+2}.png")
            self.image = pygame.transform.scale(self.image,(50 , 25))
            dx = 10
        if type == 3:
            self.image = pygame.image.load(f"cars\{type+3}.png")
            self.image = pygame.transform.scale(self.image,(50 , 25))
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(len_pos)+ dx
        self.y = -100

    def update(self,speed):
        self.rect.y += speed
        self.mask = pygame.mask.from_surface(self.image)
        
    def draw(self,win):
        win.blit(self.image, self.rect)            
