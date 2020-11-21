import pygame,random
import bot
import jugador
import time
NARANJA = (255, 128, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (14, 45, 99)
LARGO = 50
ALTO =  50
MARGEN = 5
x = 0
grid = [
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0]
          ]
inicio = (5,0)
final = (5,11)
turno = 0
pygame.init()
DIMENSION_VENTANA = [665,665]
pantalla = pygame.display.set_mode(DIMENSION_VENTANA)
pygame.display.set_caption("Quoridor")
cont = 0
posicionJugador = final
hecho = False
reloj = pygame.time.Clock()
while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 3:
                pos = pygame.mouse.get_pos()
                columna = pos[0] // (LARGO + MARGEN)
                fila = pos[1] // (ALTO + MARGEN)
                if(grid[fila][columna] == 0) :
                    grid[fila][columna] = 1
                    turno = 1
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_w:
                posicionJugador = movimiento.movimientoArriba()
                turno = 1
            if evento.key == pygame.K_s:
                posicionJugador = movimiento.movimientoAbajo()
                turno = 1
            if evento.key == pygame.K_d:
                posicionJugador = movimiento.movimientoDerecha()
                turno = 1
            if evento.key == pygame.K_a:
                posicionJugador = movimiento.movimientoIzquierda()
                turno = 1
    for fila in range(12):
        for columna in range(12):
            color = BLANCO
            if grid[fila][columna] == 1:
                color = AZUL
            if grid[fila][columna] == 2:
                color = VERDE
            if grid[fila][columna] == 3:
                color = ROJO
            if grid[fila][columna] == 4:
                color = NARANJA
            pygame.draw.rect(pantalla,color,[(MARGEN + LARGO) * (columna) + MARGEN,(MARGEN + ALTO) * fila + MARGEN,LARGO,ALTO])

    grid[5][0] = 2
    grid[5][11] = 2
    Recorrido = bot.algoritmo(grid, inicio, final, 2)
    path = Recorrido.a_star()
    data1 = path[0]
    data2 = path[1]
    movimiento = jugador.movimientoJugador(grid, posicionJugador)
    if (turno == 1):
        Movimiento = bot.movimientoBot(grid,data1,data2,x)
        Movimiento.movimiento()
        inicio = Movimiento.movimiento()
        turno = 2
    reloj.tick(60)
    pygame.display.flip()
pygame.quit()