import pygame
import random
import math

import time


# Pomgal sem si s tutoriali od "KidsCanCode" vir: https://www.youtube.com/watch?v=VO8rTszcW4s&list=PLsk-HSGFjnaH5yghzu7PcOzm9NhsW0Urw

width = 800
height = 600
fps = 60


#Inicializacija pygame in naredi novo okno
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Chaaaaaaaain reaction')
clock = pygame.time.Clock()


#krogi

StKrogov=30
PoceniKrogi=list()


#Barve

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

#Time
start_ticks = pygame.time.get_ticks()



class Krog(pygame.sprite.Sprite):
    #Sprite za Krog
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60,60))
        self.image.fill(black)
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0,width-50), random.randint(0,height-50))
        self.xsmer = random.randrange(-5,5)
        self.ysmer = math.sqrt(25-self.xsmer**2)
        self.r = random.randint(0,255)
        self.g = random.randint(0,255)
        self.b = random.randint(0,255)
        self.radius=10
        self.press=False

        pygame.draw.circle(self.image, (self.r,self.g,self.b), (30,30), self.radius, 3)


   #premikanje
    def update(self):

        if self.press:
            self.radius=30
            pygame.draw.circle(self.image, (self.r,self.g,self.b), (30,30), self.radius)
        else:
            self.rect.x += self.xsmer
            self.rect.y += self.ysmer
            if self.rect.bottom -20 > height:
                self.ysmer *= -1
            if self.rect.right -20 > width:
                self.xsmer *= -1
            if self.rect.top +20 < 0:
                self.ysmer *= -1
            if self.rect.left +20 < 0:
                self.xsmer *= -1

    def presed(self):
        self.press=True





#velik bel krog
class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60,60))
        self.image.fill(black)
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = (20, 20)
        self.press=False
        self.radius=30

        pygame.draw.circle(self.image, (255,255,255), (30,30), self.radius, 3)

        #premikanje + onclick effect
    def update(self):
        if self.press:
            pygame.draw.circle(self.image, white, (30,30), 30)
        else:
            self.rect.center = pygame.mouse.get_pos()
    #ko je pritisnjeno gre press na True
    def presed(self):
        self.press=True




#sprites:

all_sprites = pygame.sprite.Group()
krogi = pygame.sprite.Group()
PoceniKrogi = pygame.sprite.Group()
velikKrog=Cursor()
all_sprites.add(velikKrog)


#da je narisanih več krogov
for i in range(1,StKrogov):
    krog=Krog()
    all_sprites.add(krog)
    krogi.add(krog)



#Game loop
running = True
st_pocenih=0

while running:
    #Teci mora pri pravi hitrosti
    clock.tick(fps)

    #Events
    sec=seconds=(pygame.time.get_ticks()-start_ticks)/1000
    if sec > 20:
        running=False
        print("Uspelo vam je pociti:", len(PoceniKrogi)+1," krogov")
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            #izrise bel krog
            velikKrog.presed()
        #Preverim ce igralec zeli koncati
        if event.type == pygame.QUIT :
            running = False

    #Update
    all_sprites.update()
    #collision
    if velikKrog.press:
        for krog in krogi:

            if pygame.sprite.collide_circle(velikKrog,krog):
                krog.presed()
                PoceniKrogi.add(krog)
            for krog2 in PoceniKrogi:
                if pygame.sprite.collide_circle(krog2,krog):
                    krog.presed()
                    PoceniKrogi.add(krog)

                   





    #Draw / render
    screen.fill(black)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()