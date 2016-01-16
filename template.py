import pygame
import random
# pomgal sem si s tutoriali od "KidsCanCode" vir: https://www.youtube.com/watch?v=VO8rTszcW4s&list=PLsk-HSGFjnaH5yghzu7PcOzm9NhsW0Urw

width = 800
height = 600
fps = 40

#barve

black = (0,0,0)
white = (255,255,255)




#inicializacija pygame in naredi novo okno
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Chaaaaaaaain reaction')
clock = pygame.time.Clock()



# game loop
running = True
while running:
    #teci mora pri pravi hitrosti
    clock.tick(fps)
#Events
    for event in pygame.event.get():
        #preverim ce igralec zeli koncati
        if event.type == pygame.QUIT:
            running = False

#Update
#Draw / render
    screen.fill(black)
    #VEDNO NAKONCU!!!!
    pygame.display.flip()

pygame.quit()