from pickle import TRUE
import pygame
from ob import player
from ob import Road
from ob import Tree
from ob import pr
import random

pygame.init()
SCREEN = WIDTH , HEIGHT = 288 , 512
win = pygame.display.set_mode(SCREEN)

clock = pygame.time.Clock()
FPS = 10



home_img = pygame.image.load(r"bg/home.png")
bg = pygame.image.load(r"bg/bg.png")
road = pygame.image.load(r"bg/road.png")
road = pygame.transform.scale(road,(WIDTH-60 , HEIGHT))

p = player(100,HEIGHT-120,0)
move_left = False
move_right = False

road = Road()
speed = 2
tree_group = pygame.sprite.Group()
pr_group = pygame.sprite.Group()

home_page = False
game_page = True
cuonter = 0




BLUE = (30,144,255)
running = True
while running:
    win.fill(BLUE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y =event.pos
            if x< WIDTH//2:
                move_left = TRUE
            else:
                move_right = True
        if event.type == pygame.MOUSEBUTTONUP:
            move_left = False
            move_right = False

    if home_page:
       win.blit(home_img,(0,0))

    if game_page:
        win.blit(bg,(0,0))
        road.update(speed)
        road.draw(win)
        
        cuonter += 1
        if cuonter %60 == 0:
            tree = Tree(random.choice([-5, WIDTH-35]), -20)
            tree_group.add(tree)
        tree_group.update(speed)
        tree_group.draw(win)
        if cuonter % 90 == 0:
            obs = random.choices([1,2,3],weights=[6,2,2],k=1)[0]
            obee = pr(obs)
            pr_group.add(obee)
            
        pr_group.update(speed)
        pr_group.draw(win)

    p.draw(win)
    p.update(move_left,move_right)
        

    pygame.display.update()
pygame.quit()