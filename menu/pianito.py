import pygame, sys
from pygame.locals import *

pygame.init()



class Opcion:

    def __init__(self, fuente, titulo, x, y, paridad, funcion_asignada):
        self.imagen_normal = fuente.render(titulo, 1, (0, 0, 0))
        self.imagen_destacada = fuente.render(titulo, 1, (200, 0, 0))
        self.image = self.imagen_normal
        self.rect = self.image.get_rect()
        self.rect.x = 500 * paridad
        self.rect.y = y
        self.funcion_asignada = funcion_asignada
        self.x = float(self.rect.x)

    def actualizar(self):
        destino_x = 105
        self.x += (destino_x - self.x) / 5.0
        self.rect.x = int(self.x)

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)

    def destacar(self, estado):
        if estado:
            self.image = self.imagen_destacada
        else:
            self.image = self.imagen_normal

    def activar(self):
        self.funcion_asignada()


class Cursor:

    def __init__(self, x, y, dy):
        self.image = pygame.image.load('cursor.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.y_inicial = y
        self.dy = dy
        self.y = 0
        self.seleccionar(0)

    def actualizar(self):
        self.y += (self.to_y - self.y) / 10.0
        self.rect.y = int(self.y)

    def seleccionar(self, indice):
        self.to_y = self.y_inicial + indice * self.dy

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)


class Menu:
    "Representa un menú con opciones para un juego"
    
    def __init__(self, opciones):
        self.opciones = []
        fuente = pygame.font.Font('LDFComicSans.ttf', 20)
        x = 105
        y = 105
        paridad = 1

        self.cursor = Cursor(x - 30, y, 30)

        for titulo, funcion in opciones:
            self.opciones.append(Opcion(fuente, titulo, x, y, paridad, funcion))
            y += 30
            if paridad == 1:
                paridad = -1
            else:
                paridad = 1

        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False

    def actualizar(self):
        """Altera el valor de 'self.seleccionado' con los direccionales."""

        k = pygame.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:
                # Invoca a la función asociada a la opción.
                self.opciones[self.seleccionado].activar()

        # procura que el cursor esté entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1
        
        self.cursor.seleccionar(self.seleccionado)

        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]

        self.cursor.actualizar()
     
        for o in self.opciones:
            o.actualizar()

    def imprimir(self, screen):
        """Imprime sobre 'screen' el texto de cada opción del menú."""

        self.cursor.imprimir(screen)

        for opcion in self.opciones:
            opcion.imprimir(screen)

def comenzar_nuevo_juego():

    pygame.font.init()
    screen = pygame.display.set_mode((800, 600))
    fondo = pygame.image.load("pianito.jpg").convert()

    screen.blit(fondo, (0, 0))
    pygame.display.flip()
    pygame.time.delay(10)

    while True:
        for event in pygame.event.get():
            if (event.type == KEYDOWN and event.key == K_q):
                fondo = pygame.image.load("Letras/Q.jpg").convert()
                screen.blit(fondo, (0, 0))
                pygame.display.flip()
                pygame.time.delay(10)

                pygame.mixer.music.load("wav/a1.wav")
                pygame.mixer.music.play()
                pygame.event.wait()

                fondo = pygame.image.load("pianito.jpg").convert()
                screen.blit(fondo, (0, 0))
                pygame.display.flip()
                pygame.time.delay(10)

            elif (event.type == KEYDOWN and event.key == K_w):
                fondo = pygame.image.load("Letras/W.jpg").convert()
                screen.blit(fondo, (0, 0))
                pygame.display.flip()
                pygame.time.delay(10)

                pygame.mixer.music.load("wav/a1s.wav")
                pygame.mixer.music.play()
                pygame.event.wait()

                fondo = pygame.image.load("pianito.jpg").convert()
                screen.blit(fondo, (0, 0))
                pygame.display.flip()
                pygame.time.delay(10)

            elif (event.type == KEYDOWN and event.key == K_e):
                fondo = pygame.image.load("Letras/E.jpg").convert()
                screen.blit(fondo, (0, 0))
                pygame.display.flip()
                pygame.time.delay(10)

                pygame.mixer.music.load("wav/b1.wav")
                pygame.mixer.music.play()
                pygame.event.wait()

                fondo = pygame.image.load("pianito.jpg").convert()
                screen.blit(fondo, (0, 0))
                pygame.display.flip()
                pygame.time.delay(10)
            elif (event.type == KEYDOWN and event.key == K_r):
                fondo = pygame.image.load("Letras/R.jpg").convert()
                screen.blit(fondo, (0, 0))
                pygame.display.flip()
                pygame.time.delay(10)

                pygame.mixer.music.load("wav/c1.wav")
                pygame.mixer.music.play()
                pygame.event.wait()

                fondo = pygame.image.load("pianito.jpg").convert()
                screen.blit(fondo, (0, 0))
                pygame.display.flip()
                pygame.time.delay(10)

            elif (event.type == KEYDOWN and event.key == K_t):
                fondo = pygame.image.load("Letras/T.jpg").convert()
                screen.blit(fondo, (0, 0))
                pygame.display.flip()
                pygame.time.delay(10)

                pygame.mixer.music.load("wav/c1s.wav")
                pygame.mixer.music.play()
                pygame.event.wait()

                fondo = pygame.image.load("pianito.jpg").convert()
                screen.blit(fondo, (0, 0))
                pygame.display.flip()
                pygame.time.delay(10)

            elif (event.type == KEYDOWN and event.key == K_y):
                pygame.mixer.music.load("wav/c2.wav")
                pygame.mixer.music.play()
                pygame.event.wait()

            elif (event.type == KEYDOWN and event.key == K_u):
                pygame.mixer.music.load("wav/d1.wav")
                pygame.mixer.music.play()
                pygame.event.wait()

            elif (event.type == KEYDOWN and event.key == K_i):
                pygame.mixer.music.load("wav/d1s.wav")
                pygame.mixer.music.play()
                pygame.event.wait()

            elif (event.type == KEYDOWN and event.key == K_o):
                pygame.mixer.music.load("wav/e1.wav")
                pygame.mixer.music.play()
                pygame.event.wait()
            elif (event.type == KEYDOWN and event.key == K_p):
                pygame.mixer.music.load("wav/f1.wav")
                pygame.mixer.music.play()
                pygame.event.wait()
            elif (event.type == KEYDOWN and event.key == K_k):
                pygame.mixer.music.load("wav/f1s.wav")
                pygame.mixer.music.play()
                pygame.event.wait()
            elif (event.type == KEYDOWN and event.key == K_l):
                pygame.mixer.music.load("wav/g1.wav")
                pygame.mixer.music.play()
                pygame.event.wait()
            elif (event.type == KEYDOWN and event.key == K_ESCAPE):
                import sys
                print(" Gracias por utilizar este programa.")
                sys.exit(0)


def mostrar_opciones():
    print (" Función que muestra otro menú de opciones.")

def creditos():
    print (" Función que muestra los creditos del programa.")

def salir_del_programa():
    import sys
    print (" Gracias por utilizar Tecladito Ramon-Nachon.")
    sys.exit(0)


if __name__ == '__main__':

    salir = False
    opciones = [
        ("Freeplay", comenzar_nuevo_juego),
        ("Opciones", mostrar_opciones),
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
