import pygame,random
import a_star
import time
NARANJA = (255, 128, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (14, 45, 99)
LARGO = 50
ALTO =  50
MARGEN = 5

grid = [
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]
          ]
inicio = (5,0)
final = (5,9)
turno = 0
data1 = []
data2 = []
x = 0
pygame.init()
DIMENSION_VENTANA = [555, 555]
pantalla = pygame.display.set_mode(DIMENSION_VENTANA)
pygame.display.set_caption("Quoridor")
cont = 0
hecho = False
reloj = pygame.time.Clock()
posicionJugador = final
class algoritmo() :
    def __init__(self,grid,inicio,final,jugador):
        self.grid = grid
        self.inicio = inicio
        self.final = final
        self.jugador = jugador
    def a_star(self):
        data1[:] = []
        data2[:] = []
        path = a_star.a_star(self.grid,self.inicio,self.final,self.jugador)
        for elemento in path:
            data1.append(elemento[0])
            data2.append(elemento[1])
        return data1,data2
class movimientoBot():
    def __init__(self,grid,data1,data2):
        self.grid = grid
        self.data1 = data1
        self.data2 = data2
    def movimiento(self):
        self.grid[self.data1[x+1]][self.data2[x+1]] = 4
        self.grid[self.data1[x]][self.data2[x]] = 0
        return 2
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
                if (grid[posicionJugador[0]-1][posicionJugador[1]] != 1 and grid[posicionJugador[0] - 1][posicionJugador[1]] != 4):
                    if (posicionJugador[0] > 0):
                        grid[posicionJugador[0]-1][posicionJugador[1]] = 3
                        grid[posicionJugador[0]][posicionJugador[1]] = 0
                        posicionJugador = (posicionJugador[0]-1,posicionJugador[1])
                turno = 1
            if evento.key == pygame.K_s:
                if (grid[posicionJugador[0] + 1][posicionJugador[1]] != 1 and grid[posicionJugador[0] + 1][posicionJugador[1]] != 4):
                    if (posicionJugador[0] < 9):
                        grid[posicionJugador[0]+1][posicionJugador[1]] = 3
                        grid[posicionJugador[0]][posicionJugador[1]] = 0
                        posicionJugador = (posicionJugador[0]+1, posicionJugador[1])
                turno = 1
            if evento.key == pygame.K_d:
                if (grid[posicionJugador[0]][posicionJugador[1] + 1] != 1 and grid[posicionJugador[0]][posicionJugador[1] + 1] != 4):
                    if (posicionJugador[1] < 9):
                        grid[posicionJugador[0]][posicionJugador[1]+1] = 3
                        grid[posicionJugador[0]][posicionJugador[1]] = 0
                        posicionJugador = (posicionJugador[0], posicionJugador[1]+1)
                turno = 1
            if evento.key == pygame.K_a:
                if (grid[posicionJugador[0]][posicionJugador[1] - 1] != 1 and grid[posicionJugador[0]][posicionJugador[1] - 1] != 4):
                    if (posicionJugador[1] > 0):
                        grid[posicionJugador[0]][posicionJugador[1]-1] = 3
                        grid[posicionJugador[0]][posicionJugador[1]] = 0
                        posicionJugador = (posicionJugador[0], posicionJugador[1] - 1)
                turno = 1
    for fila in range(10):
        for columna in range(10):
            color = BLANCO
            if grid[fila][columna] == 1:
                color = AZUL
            if grid[fila][columna] == 2:
                color = VERDE
            if grid[fila][columna] == 3:
                color = ROJO
            if grid[fila][columna] == 4:
                color = NARANJA
            pygame.draw.rect(pantalla,color,[(MARGEN + LARGO) * columna + MARGEN,(MARGEN + ALTO) * fila + MARGEN,LARGO,ALTO])
    Recorrido = algoritmo(grid, inicio, final,2)
    path = Recorrido.a_star()
    data1 = path[0]
    data2 = path[1]
    grid[5][0] = 2
    grid[5][9] = 2
    if (turno == 1):
        Movimiento = movimientoBot(grid,data1,data2)
        turno = Movimiento.movimiento()
        x = x + 1
    reloj.tick(60)
    pygame.display.flip()
pygame.quit()