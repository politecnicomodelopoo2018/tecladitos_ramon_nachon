import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((100, 100))

display_width = 800
display_height = 600

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

crash = False
menu = True


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Tecladitos Nachon')
clock = pygame.time.Clock()

tecladito_img = pygame.image.load('/home/alumno/Escritorio/piano_keys_final_real.png')

def tecladito(x,y):
    gameDisplay.blit(tecladito_img,(x,y))

x = (display_width * 0.5)
y = (display_height * 0.5)


while not crash:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crash = True
        if (event.type == KEYDOWN and event.key == K_q):
            pygame.mixer.music.load("/home/alumno/PycharmProjects/R&N/68437__pinkyfinger__piano-a.wav")
            pygame.mixer.music.play()
            pygame.event.wait()

        if (event.type == KEYDOWN and event.key == K_w):
            pygame.mixer.music.load("/home/alumno/PycharmProjects/R&N/68439__pinkyfinger__piano-bb.wav")
            pygame.mixer.music.play()
            pygame.event.wait()

        if (event.type == KEYDOWN and event.key == K_e):
            pygame.mixer.music.load("/home/alumno/PycharmProjects/R&N/68438__pinkyfinger__piano-b.wav")
            pygame.mixer.music.play()
            pygame.event.wait()

        if (event.type == KEYDOWN and event.key == K_r):
            pygame.mixer.music.load("/home/alumno/PycharmProjects/R&N/68441__pinkyfinger__piano-c.wav")
            pygame.mixer.music.play()
            pygame.event.wait()


        if (event.type == KEYDOWN and event.key == K_t):
            pygame.mixer.music.load("/home/alumno/PycharmProjects/R&N/68440__pinkyfinger__piano-c.wav")
            pygame.mixer.music.play()
            pygame.event.wait()

        if (event.type == KEYDOWN and event.key == K_y):
            pygame.mixer.music.load("/home/alumno/PycharmProjects/R&N/68442__pinkyfinger__piano-d.wav")
            pygame.mixer.music.play()
            pygame.event.wait()

        if (event.type == KEYDOWN and event.key == K_u):
            pygame.mixer.music.load("/home/alumno/PycharmProjects/R&N/68444__pinkyfinger__piano-eb.wav")
            pygame.mixer.music.play()
            pygame.event.wait()

        if (event.type == KEYDOWN and event.key == K_i):
            pygame.mixer.music.load("/home/alumno/PycharmProjects/R&N/68443__pinkyfinger__piano-e.wav")
            pygame.mixer.music.play()
            pygame.event.wait()

        if (event.type == KEYDOWN and event.key == K_o):
            pygame.mixer.music.load("/home/alumno/PycharmProjects/R&N/68445__pinkyfinger__piano-f.wav")
            pygame.mixer.music.play()
            pygame.event.wait()

        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            sys.exit()

    gameDisplay.fill(white)
    tecladito(x, y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()


while menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    gameDisplay.fill(white)
    Titulo = pygame.font.Font('freesansbold.ttf',115)