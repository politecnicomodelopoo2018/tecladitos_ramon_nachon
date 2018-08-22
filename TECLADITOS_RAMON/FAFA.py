import pygame, sys
import pyglet
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((100, 100))



while True:

    for event in pygame.event.get():
            if (event.type == KEYDOWN and event.key == K_q):
                pygame.mixer.music.load("/home/alumno/PycharmProjects/R&N/68437__pinkyfinger__piano-a.wav")
                pygame.mixer.music.play()
                pygame.event.wait()

            if (event.type == KEYDOWN and event.key == K_w):
                pygame.mixer.music.load("/home/alumno/PycharmProjects/R&N/68438__pinkyfinger__piano-b.wav")
                pygame.mixer.music.play()
                pygame.event.wait()

            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                sys.exit()