import pygame
import random
import math

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
        self.rect.center = (random.randint(0,800), random.randint(0,600))
        self.xsmer = random.randrange(-5,5)
        self.ysmer = math.sqrt(25-self.xsmer**2)
        self.r = random.randint(0,255)
        self.g = random.randint(0,255)
        self.b = random.randint(0,255)
        self.radij=10

        self.draw_circle()


    def update(self):
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

    def draw_circle(self):
        pygame.draw.circle(self.image, (self.r,self.g,self.b), (30,30), self.radij, 3)





all_sprites = pygame.sprite.Group()
krogi = pygame.sprite.Group()


for i in range(1,StKrogov):
    krog=Krog()
    all_sprites.add(krog)
    krogi.add(krog)




#Game loop
running = True
i=0

while running:
    #Teci mora pri pravi hitrosti
    clock.tick(fps)

    #Events
    sec=seconds=(pygame.time.get_ticks()-start_ticks)/1000
    if sec > 20:
        running=False
    for event in pygame.event.get():
        i+=1
        #Preverim ce igralec zeli koncati
        if event.type == pygame.QUIT :
            running = False

    #Update
    all_sprites.update()
    #Draw / render
    screen.fill(black)
    all_sprites.draw(screen)
    #VEDNO NAKONCU!!!!
    pygame.display.flip()

pygame.quit()