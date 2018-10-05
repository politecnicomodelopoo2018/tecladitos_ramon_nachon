import pygame
from pygame.locals import *
import pymysql
from menu.pianito import *

#cuando inicia el programa que pueda seleccionar la cancion
#cuando termine la partida se le pide el nombre y se guarda el highscore
#modo grabación de niv

class Funciones(object):

    def __init__(self,cant_tec,partitura):
        self.nivel = cant_tec
        self.cancion_chota = partitura

    def get_nivel_part(self):

        print("Seleccione Cancion: 1 - Cancion Ramon")
        print("                    2 - Cancion Chota")
        ID_Cancion = input("Eleccion: ")

        query = ("select 'nivel' from CANCION where 'id' = %s" % (ID_Cancion))
        query_2 = ("select 'nivel' from CANCION where 'id' = %s" % (ID_Cancion))

        db = pymysql.connect (host='127.0.0.1',
                               user='root',
                               passwd='alumno',
                               db='mydb',
                               charset='utf8',
                               autocommit=True)

        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query)
        cant_tec = cursor.fetchone()
        cursor.execute(query_2)
        partitura = cursor.fetchone()
        db.close()

    def comenzar_nuevo_juego(self):

        pygame.font.init()
        screen = pygame.display.set_mode((800, 600))
        fondo = pygame.image.load("pianito.jpg").convert()

        screen.blit(fondo, (0, 0))
        pygame.display.flip()
        pygame.time.delay(10)

        sound = pygame.mixer.Sound("/home/alumno/Escritorio/piano/c1.wav")
        sound1 = pygame.mixer.Sound("/home/alumno/Escritorio/piano/c1s.wav")
        sound2 = pygame.mixer.Sound("/home/alumno/Escritorio/piano/d1.wav")
        sound3 = pygame.mixer.Sound("/home/alumno/Escritorio/piano/d1s.wav")
        sound4 = pygame.mixer.Sound("/home/alumno/Escritorio/piano/e1.wav")
        sound5 = pygame.mixer.Sound("/home/alumno/Escritorio/piano/f1.wav")
        sound6 = pygame.mixer.Sound("/home/alumno/Escritorio/piano/f1s.wav")
        sound7 = pygame.mixer.Sound("/home/alumno/Escritorio/piano/g1.wav")
        sound8 = pygame.mixer.Sound("/home/alumno/Escritorio/piano/g1s.wav")
        sound9 = pygame.mixer.Sound("/home/alumno/Escritorio/piano/a1.wav")
        sound10 = pygame.mixer.Sound("/home/alumno/Escritorio/piano/a1s.wav")
        sound11 = pygame.mixer.Sound("/home/alumno/Escritorio/piano/b1.wav")



        while True:
            for event in pygame.event.get():
                if (event.type == KEYDOWN and event.key == K_z):
                    fondo = pygame.image.load("Letras/Q.jpg").convert()
                    screen.blit(fondo, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(10)

                    sound.play()

                    fondo = pygame.image.load("pianito.jpg").convert()
                    screen.blit(fondo, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(10)

                elif (event.type == KEYDOWN and event.key == K_s):
                    fondo = pygame.image.load("Letras/W.jpg").convert()
                    screen.blit(fondo, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(10)

                    sound1.play()

                    fondo = pygame.image.load("pianito.jpg").convert()
                    screen.blit(fondo, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(10)

                elif (event.type == KEYDOWN and event.key == K_x):
                    fondo = pygame.image.load("Letras/E.jpg").convert()
                    screen.blit(fondo, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(10)

                    sound2.play()

                    fondo = pygame.image.load("pianito.jpg").convert()
                    screen.blit(fondo, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(10)

                elif (event.type == KEYDOWN and event.key == K_d):
                    fondo = pygame.image.load("Letras/R.jpg").convert()
                    screen.blit(fondo, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(10)

                    sound3.play()

                    fondo = pygame.image.load("pianito.jpg").convert()
                    screen.blit(fondo, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(10)

                elif (event.type == KEYDOWN and event.key == K_c):
                    fondo = pygame.image.load("Letras/T.jpg").convert()
                    screen.blit(fondo, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(10)

                    sound4.play()

                    fondo = pygame.image.load("pianito.jpg").convert()
                    screen.blit(fondo, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(10)

                elif (event.type == KEYDOWN and event.key == K_v):

                    sound5.play()

                    fondo = pygame.image.load("pianito.jpg").convert()
                    screen.blit(fondo, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(10)

                elif (event.type == KEYDOWN and event.key == K_g):

                    sound6.play()

                    fondo = pygame.image.load("pianito.jpg").convert()
                    screen.blit(fondo, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(10)

                elif (event.type == KEYDOWN and event.key == K_b):

                    sound7.play()

                    fondo = pygame.image.load("pianito.jpg").convert()
                    screen.blit(fondo, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(10)

                elif (event.type == KEYDOWN and event.key == K_h):

                    sound8.play()

                    fondo = pygame.image.load("pianito.jpg").convert()
                    screen.blit(fondo, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(10)

                elif (event.type == KEYDOWN and event.key == K_n):

                    sound9.play()

                    fondo = pygame.image.load("pianito.jpg").convert()
                    screen.blit(fondo, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(10)

                elif (event.type == KEYDOWN and event.key == K_j):

                    sound10.play()

                    fondo = pygame.image.load("pianito.jpg").convert()
                    screen.blit(fondo, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(10)

                elif (event.type == KEYDOWN and event.key == K_m):

                    sound11.play()

                    fondo = pygame.image.load("pianito.jpg").convert()
                    screen.blit(fondo, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(10)


                elif (event.type == KEYDOWN and event.key == K_ESCAPE):
                    import sys
                    print(" Gracias por utilizar Tecladitos Ramon-Nachon.")
                    sys.exit(0)

    def niveles(self,nivel,cancion_chota):
        pygame.font.init()
        screen = pygame.display.set_mode((800, 600))
        fondo = pygame.image.load("pianito.jpg").convert()

        #get_nivel_part()

        cancion_tocada = ""

        i = 0

        screen.blit(fondo, (0, 0))
        pygame.display.flip()
        pygame.time.delay(10)

        sound = pygame.mixer.Sound("/home/alumno/Escritorio/piano/c1.wav")
        sound1 = pygame.mixer.Sound("/home/alumno/Escritorio/piano/c1s.wav")
        sound2 = pygame.mixer.Sound("/home/alumno/Escritorio/piano/d1.wav")
        sound3 = pygame.mixer.Sound("/home/alumno/Escritorio/piano/d1s.wav")
        sound4 = pygame.mixer.Sound("/home/alumno/Escritorio/piano/e1.wav")
        sound5 = pygame.mixer.Sound("/home/alumno/Escritorio/piano/f1.wav")
        sound6 = pygame.mixer.Sound("/home/alumno/Escritorio/piano/f1s.wav")
        sound7 = pygame.mixer.Sound("/home/alumno/Escritorio/piano/g1.wav")
        sound8 = pygame.mixer.Sound("/home/alumno/Escritorio/piano/g1s.wav")
        sound9 = pygame.mixer.Sound("/home/alumno/Escritorio/piano/a1.wav")
        sound10 = pygame.mixer.Sound("/home/alumno/Escritorio/piano/a1s.wav")
        sound11 = pygame.mixer.Sound("/home/alumno/Escritorio/piano/b1.wav")



        while i < nivel:
            for event in pygame.event.get():
                if (event.type == KEYDOWN and event.key == K_z):
                    fondo = pygame.image.load("Letras/Q.jpg").convert()
                    screen.blit(fondo, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(10)

                    sound.play()

                    fondo = pygame.image.load("pianito.jpg").convert()
                    screen.blit(fondo, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(10)

                    cancion_tocada = str(cancion_tocada) + 'z'

                    i = i + 1

                elif (event.type == KEYDOWN and event.key == K_s):
                    fondo = pygame.image.load("Letras/W.jpg").convert()
                    screen.blit(fondo, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(10)

                    sound1.play()

                    fondo = pygame.image.load("pianito.jpg").convert()
                    screen.blit(fondo, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(10)

                    cancion_tocada = str(cancion_tocada) + 's'

                    i = i + 1

                elif (event.type == KEYDOWN and event.key == K_x):
                    fondo = pygame.image.load("Letras/E.jpg").convert()
                    screen.blit(fondo, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(10)

                    sound2.play()

                    fondo = pygame.image.load("pianito.jpg").convert()
                    screen.blit(fondo, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(10)

                    cancion_tocada = str(cancion_tocada) + 'x'

                    i = i + 1

                elif (event.type == KEYDOWN and event.key == K_d):
                    fondo = pygame.image.load("Letras/R.jpg").convert()
                    screen.blit(fondo, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(10)

                    sound3.play()

                    fondo = pygame.image.load("pianito.jpg").convert()
                    screen.blit(fondo, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(10)

                    cancion_tocada = str(cancion_tocada) + 'd'

                    i = i + 1

                elif (event.type == KEYDOWN and event.key == K_c):
                    fondo = pygame.image.load("Letras/T.jpg").convert()
                    screen.blit(fondo, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(10)

                    sound4.play()

                    fondo = pygame.image.load("pianito.jpg").convert()
                    screen.blit(fondo, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(10)

                    cancion_tocada = str(cancion_tocada) + 'c'

                    i = i + 1

                elif (event.type == KEYDOWN and event.key == K_v):

                    sound5.play()

                    fondo = pygame.image.load("pianito.jpg").convert()
                    screen.blit(fondo, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(10)

                    cancion_tocada = str(cancion_tocada) + 'y'

                    i = i + 1

                elif (event.type == KEYDOWN and event.key == K_g):

                    sound6.play()

                    fondo = pygame.image.load("pianito.jpg").convert()
                    screen.blit(fondo, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(10)

                    cancion_tocada = str(cancion_tocada) + 'g'

                    i = i + 1

                elif (event.type == KEYDOWN and event.key == K_b):

                    sound7.play()

                    fondo = pygame.image.load("pianito.jpg").convert()
                    screen.blit(fondo, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(10)

                    cancion_tocada = str(cancion_tocada) + 'b'

                    i = i + 1

                elif (event.type == KEYDOWN and event.key == K_h):

                    sound8.play()

                    fondo = pygame.image.load("pianito.jpg").convert()
                    screen.blit(fondo, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(10)

                    cancion_tocada = str(cancion_tocada) + 'h'

                    i = i + 1

                elif (event.type == KEYDOWN and event.key == K_n):

                    sound9.play()

                    fondo = pygame.image.load("pianito.jpg").convert()
                    screen.blit(fondo, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(10)

                    cancion_tocada = str(cancion_tocada) + 'n'

                    i = i + 1

                elif (event.type == KEYDOWN and event.key == K_j):

                    sound10.play()

                    fondo = pygame.image.load("pianito.jpg").convert()
                    screen.blit(fondo, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(10)

                    cancion_tocada = str(cancion_tocada) + 'j'

                    i = i + 1

                elif (event.type == KEYDOWN and event.key == K_m):

                    sound11.play()

                    fondo = pygame.image.load("pianito.jpg").convert()
                    screen.blit(fondo, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(10)

                    cancion_tocada = str(cancion_tocada) + 'm'

                    i = i + 1


                elif (event.type == KEYDOWN and event.key == K_ESCAPE):
                    import sys
                    print(" GGracias por utilizar Tecladitos Ramon-Nachon.")
                    sys.exit(0)


        if cancion_tocada == cancion_chota:
            print("Ganaste Maestro")
            print(cancion_tocada)
        else:
            print("u mom gay")
            print(cancion_tocada)




    def creditos(self):
        print ("Este maravilloso juego fue creado por los mismisimos RAMON & NACHON.")
        print ("Ya sé lo que estás pensando, eso es imposible, pero ne.")
        print ("Con mucho esfuerzo y sufrimiento, lo logramos.QUE FORT")
        print ("(En realidad lo hizo todo NAMON, pero el otro pibe nos da un poco de pena.)")

    def salir_del_programa(self):
        import sys
        print (" Gracias por utilizar Tecladitos Ramon-Nachon.")
        sys.exit(0)


    if __name__ == '__main__':

        salir = False
        opciones = [
            ("Freeplay", comenzar_nuevo_juego),
            ("Levels", niveles),
            ("Creditos", creditos),
            ("Salir", salir_del_programa)
            ]

        pygame.font.init()
        screen = pygame.display.set_mode((320, 240))

        fondo = pygame.image.load("fondo.png").convert()
        menu = Menu(opciones)

        while not salir:

            for e in pygame.event.get():
                if e.type == QUIT:
                    salir = True

            screen.blit(fondo, (0, 0))
            menu.actualizar()
            menu.imprimir(screen)
            pygame.display.flip()
            pygame.time.delay(10)
