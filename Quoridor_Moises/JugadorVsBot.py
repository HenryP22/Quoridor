import pygame,random
import bot
import jugador
import time
NARANJA = (255, 128, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
NEGRO = (0,0,0)
AZUL = (14, 45, 99)
LARGO = 50
ALTO =  50
MARGEN = 5
x = 0
grid = [
            [0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0]
          ]
inicio = (6,0)
finalJugador = (6,0)
final = (6,12)
turno = 0
pygame.init()
DIMENSION_VENTANA = [600,600]
pantalla = pygame.display.set_mode(DIMENSION_VENTANA)
pygame.display.set_caption("Quoridor")
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
                if pos[0] < 300:
                    columna = pos[0] // (50)
                else:
                    columna = pos[0] // (45)

                if pos[1] < 300:
                    fila = pos[1] // (50)
                else:
                    fila = pos[1] // (45)
                print(pos[0],pos[1])

                if(grid[fila][columna] == 0 and columna %2 != 0 or fila%2!=0):
                    if  columna %2 != 0 and fila%2!=0: continue
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
    for fila in range(13):
        for columna in range(13):
            color = BLANCO
            if grid[fila][columna] == 1:
                color = AZUL
            if grid[fila][columna] == 2:
                color = VERDE
            if grid[fila][columna] == 3:
                color = ROJO
            if grid[fila][columna] == 4:
                color = NARANJA
            if columna %2 != 0 and fila%2!=0:
                grid[fila][columna] = 5
                color = NEGRO
            if columna % 2 == 0:
                if columna == 0:
                    if fila % 2 != 0:
                        if fila == 1:
                            pygame.draw.rect(pantalla,color,[(MARGEN + LARGO) * (columna) + MARGEN ,(MARGEN + ALTO) * fila + MARGEN+5,LARGO,20])
                        else:
                            pygame.draw.rect(pantalla, color,
                                             [(MARGEN + LARGO) * (columna) + MARGEN , (MARGEN + 40) * fila + MARGEN+15,
                                              LARGO, 20])
                        ##primera fila de bloques
                    else:
                        if fila == 0:
                            pygame.draw.rect(pantalla, color,
                                         [(MARGEN + LARGO) * (columna) + MARGEN, (MARGEN + 40) * fila + MARGEN, LARGO,
                                          ALTO])
                        else:
                            pygame.draw.rect(pantalla, color,
                                             [(MARGEN + LARGO) * (columna) + MARGEN, (MARGEN + 40) * fila + MARGEN,
                                              LARGO,
                                              ALTO])
                        ##primera columna
                elif columna <13: ##columnas pares que no sea 0
                    if fila % 2 != 0:
                        pygame.draw.rect(pantalla,color,[(MARGEN + 40) * (columna) + MARGEN,(MARGEN + 40) * fila + MARGEN+15,LARGO,20])

                    else:
                        pygame.draw.rect(pantalla, color,
                                         [(MARGEN + 40) * (columna) + MARGEN, (MARGEN + 40) * fila + MARGEN,
                                          LARGO,
                                          ALTO])
            else: ##columnas impares
                if columna == 1:
                    if fila % 2 != 0:
                        pygame.draw.rect(pantalla,color,[(MARGEN + LARGO) * (columna) + MARGEN+5,(MARGEN + 40) * fila + MARGEN + 15,20,20])
                    else:
                        pygame.draw.rect(pantalla, color,
                                     [(MARGEN + LARGO) * (columna) + MARGEN+5, (MARGEN + 40) * fila + MARGEN, 20, ALTO])
                elif columna <13:
                    if fila % 2 != 0:
                        pygame.draw.rect(pantalla,color,[(MARGEN + 40) * (columna) + MARGEN+15,(MARGEN + 40) * fila + MARGEN+ 15,20,20])
                    else:
                        pygame.draw.rect(pantalla, color,
                                         [(MARGEN + 40) * (columna) + MARGEN+ 15, (MARGEN + 40) * fila + MARGEN,
                                          20,
                                          ALTO])




    grid[6][0] = 2
    grid[6][12] = 2
    Recorrido = bot.algoritmo(grid, inicio, final, 2)
    path = Recorrido.a_star()
    data1 = path[0]
    data2 = path[1]
    movimiento = jugador.movimientoJugador(grid, posicionJugador)
    if turno == 1 :
        Movimiento = bot.movimientoBot(grid,data1,data2,x,4)
        Movimiento.movimiento()
        inicio = Movimiento.movimiento()
        turno = 2
    if(posicionJugador == finalJugador or inicio == final):
        pygame.quit()
    reloj.tick(60)
    pygame.display.flip()
pygame.quit()