from random import randrange
import datetime
import os
import sys
import pygame
from pygame.locals import *
import pygameMenu
from pygameMenu.locals import *

pygame.init()

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

display_size = (800,600)
FPS = 60.0

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
purple = (255,0,255)
blue = (0,255,255)

crash = False
menu = True

gameDisplay = pygame.display.set_mode((display_size))
pygame.display.set_caption('Tecladitos Nachon')
clock = pygame.time.Clock()
dt = 1 / FPS

dificultad = ['Facil']

def fondo():
    Background('/home/alumno/PycharmProjects/R&N/dio.png', [0, 0])

def cambiar_dificultad(d):
    print('Dificultad seleccionada: {0}'.format(d))
    dificultad[0] = d

def free():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

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

def jugar(dificultadasa, fuente_letra):
    difficulty = dificultadasa[0]
    assert isinstance(difficulty, str)

    if difficulty == 'Facil':
        f = fuente_letra.render('Jugando en Facil', 1, white)
    elif difficulty == 'Medio':
        f = fuente_letra.render('Jugando en Medio', 1, white)
    elif difficulty == 'Dificil':
        f = fuente_letra.render('Jugando en Dificil', 1, white)

    f_width = f.get_size()[0]


    while not crash:


        clock.tick(60)

        playevents = pygame.event.get()
        for e in playevents:
            if e.type == QUIT:
                exit()
            elif e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    if menu_pricipal.is_disabled():
                        menu_pricipal.enable()
                        return

        menu_pricipal.mainloop(playevents)

        gameDisplay.fill(blue)
        gameDisplay.blit(f, ((display_size[0] - f_width) / 2, display_size[1] / 2))
        pygame.display.flip()




menu_jugar_dif = pygameMenu.Menu(gameDisplay,
                                 bgfun=fondo,
                                 color_selected=purple,
                                 font=pygameMenu.fonts.FONT_BEBAS,
                                 font_color=black,
                                 font_size=30,
                                 menu_alpha=100,
                                 menu_color=blue,
                                 menu_height=int(display_size[1] * 0.6),
                                 menu_width=int(display_size[0] * 0.6),
                                 onclose=PYGAME_MENU_DISABLE_CLOSE,
                                 option_shadow=False,
                                 title='Menu del Juego',
                                 window_height=display_size[1],
                                 window_width=display_size[0]
                                 )
menu_jugar_dif.add_option('Jugar', jugar, dificultad,
                          pygame.font.Font(pygameMenu.fonts.FONT_FRANCHISE, 30))
menu_jugar_dif.add_selector('Seleccione Dificultad', [('Facil', 'Facil'),
                                                      ('Medio', 'Medio'),
                                                      ('Dificil', 'Dificil')],
                            onreturn=None,
                            onchange=cambiar_dificultad)
menu_jugar_dif.add_option('Volver al Menu Principal', PYGAME_MENU_BACK)

menu_jugar_free = pygameMenu.Menu(gameDisplay,
                                 bgfun=fondo,
                                 color_selected=purple,
                                 font=pygameMenu.fonts.FONT_BEBAS,
                                 font_color=black,
                                 font_size=30,
                                 menu_alpha=100,
                                 menu_color=blue,
                                 menu_height=int(display_size[1] * 0.6),
                                 menu_width=int(display_size[0] * 0.6),
                                 onclose=PYGAME_MENU_DISABLE_CLOSE,
                                 option_shadow=False,
                                 title='Menu de Freeplay',
                                 window_height=display_size[1],
                                 window_width=display_size[0]

                                 )
menu_jugar_free.add_option('Jugar', free,
                          pygame.font.Font(pygameMenu.fonts.FONT_FRANCHISE, 30))
menu_jugar_free.add_option('Volver al Menu Principal', PYGAME_MENU_BACK)

menu_pricipal = pygameMenu.Menu(gameDisplay,
                                bgfun=fondo,
                                color_selected=purple,
                                font=pygameMenu.fonts.FONT_BEBAS,
                                font_color=black,
                                font_size=30,
                                menu_alpha=100,
                                menu_color=blue,
                                menu_height=int(display_size[1] * 0.6),
                                menu_width=int(display_size[0] * 0.6),
                                onclose=PYGAME_MENU_DISABLE_CLOSE,
                                option_shadow=False,
                                title='Menu Principal',
                                window_height=display_size[1],
                                window_width=display_size[0]
                                )
menu_pricipal.add_option('NIVELES', menu_jugar_dif)
menu_pricipal.add_option('FREEPLAY', menu_jugar_free)
menu_pricipal.add_option('EXIT', PYGAME_MENU_EXIT)

#MAIN

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameDisplay.fill(blue)
            Titulo = pygame.font.Font('freesansbold.ttf',115)
            clock.tick(60)
            menu_pricipal.mainloop(event)
            pygame.display.flip()
