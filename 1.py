


import pygame
import constants
import random

pygame.init()

# datos de pantalla
dimensiones = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Brazo repartidor")

# Iteramos hasta que el usuario haga click sobre el botón de cerrar
hecho = False

# Usado para gestionar cuán rápido se actualiza la pantalla
reloj = pygame.time.Clock()

# Posición de partida del rectángulo
rect_x = 90
rect_y = -50

# Velocidad y dirección inicial del rectángulo
rect_cambio_x = 0
rect_cambio_y = 5

color = random.choice(constants.colores)
cantidad = 1

menu = constants.ImagenFondo1
fondo = constants.ImagenFondo2
resultados = constants.ImagenFondo3
background = fondo
# ----------------------- BUCLE PRINCIPAL-------------------------------------------------#

while not hecho:
    for evento in pygame.event.get():  # El usuario hizo algo
        if evento.type == pygame.QUIT:  # Si el usuario hace click sobre cerrar
            hecho = True  # Marca que ya lo hemos hecho, de forma que abandonamos el bucle

    pantalla.blit(background, (0, 0))
    # --- Lógica del juego
    # Mueve el punto de partida del rectángulo
    rect_x += rect_cambio_x
    rect_y += rect_cambio_y

    # Rebota el rectángulo, si hace falta.

    if rect_y > 340 and rect_x == 90 :  # Si el valor de y es mayor a 450 y menor a 0 píxeles,
        rect_cambio_y = 0  # modifico la tasa de cambio, de positiva, a negativa.
        rect_cambio_x = 5

    if rect_x > 500 and color == constants.BLANCO :  # Si el valor de y es mayor a 450 y menor a 0 píxeles,
        rect_cambio_y = -4  # modifico la tasa de cambio, de positiva, a negativa.
        rect_cambio_x = 5
    if rect_x > 500 and color == constants.VERDE:  # Si el valor de y es mayor a 450 y menor a 0 píxeles,
        rect_cambio_y = 4  # modifico la tasa de cambio, de positiva, a negativa.
        rect_cambio_x = 5
    if rect_x > 500 and color == constants.ROJO:  # Si el valor de y es mayor a 450 y menor a 0 píxeles,
        rect_cambio_y = 2  # modifico la tasa de cambio, de positiva, a negativa.
        rect_cambio_x = 5
    if rect_x > 800 :  # Si el valor de y es mayor a 450 y menor a 0 píxeles,
        rect_cambio_y = 0  # modifico la tasa de cambio, de positiva, a negativa.
        rect_cambio_x = 5
    if rect_x > 1000 and cantidad > 0:  # Si el valor de y es mayor a 450 y menor a 0 píxeles,
        if cantidad == 1:
           rect_cambio_y = 0  # modifico la tasa de cambio, de positiva, a negativa.
        else:
           rect_cambio_y = 5
        rect_cambio_x = 0
        rect_x = 90
        rect_y = -50
        color = random.choice(constants.colores)
        print (cantidad)
        cantidad = cantidad - 1
    if cantidad == 0:
        background = resultados


    # --- Dibujamos
    # Limpia la pantalla y establece su color de fondo
    #pantalla.fill(constants.NEGRO)
    pantalla.blit(background, (0, 0))

    # Dibujamos los Rectángulos
    pygame.draw.rect(pantalla, constants.NEGRO, [rect_x, rect_y, 50, 50])
    pygame.draw.rect(pantalla, color, [rect_x + 10, rect_y + 10, 30, 30])

    # --- Envolvemos todo
    # Limitamos a 60 fotogramas por segundo
    reloj.tick(60)

    # Avancemos y actualicemos la pantalla con lo que hemos dibujado.
    pygame.display.flip()


# Pórtate bien con el IDLE. Si nos olvidamos de esta línea, el programa se 'colgará'
# en la salida.
pygame.quit()