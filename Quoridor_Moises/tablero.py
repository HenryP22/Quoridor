import pygame,random
import a_star
NEGRO = (0, 0, 0)
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
grid[5][0] = 2
grid[5][9] = 3
xb = 0
yb = -1
inicio = (5,0)
final = (5,8)
inicio2 = (5,9)
final2 = (5,1)
x = 0
y = -1
pygame.init()
DIMENSION_VENTANA = [555, 555]
pantalla = pygame.display.set_mode(DIMENSION_VENTANA)
pygame.display.set_caption("Quoridor")
cont = 0
hecho = False
reloj = pygame.time.Clock()
while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                data1 = []
                data2 = []
                path = a_star.a_star(grid, inicio, final)
                for elemento in path:
                    data1.append(elemento[0])
                    data2.append(elemento[1])
                data1b = []
                data2b = []
                path2 = a_star.a_star(grid, inicio2, final2)
                for elemento2 in path2:
                    data1b.append(elemento2[0])
                    data2b.append(elemento2[1])
            if evento.button == 3:
                pos = pygame.mouse.get_pos()
                columna = pos[0] // (LARGO + MARGEN)
                fila = pos[1] // (ALTO + MARGEN)
                grid[fila][columna] = 1
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
               grid[data1[x+1]][data2[x+1]] = 2
               x = x + 1
               grid[data1b[xb + 1]][data2b[xb + 1]] = 3
               xb = xb + 1
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_r:
               grid[data1[y+1]][data2[y+1]] = 0
               y = y + 1
               grid[data1b[yb + 1]][data2b[yb + 1]] = 0
               yb = yb + 1
    for fila in range(10):
        for columna in range(10):
            color = BLANCO
            if grid[fila][columna] == 1:
                color = AZUL
            if grid[fila][columna] == 2:
                color = VERDE
            if grid[fila][columna] == 3:
                color = ROJO
            pygame.draw.rect(pantalla,color,[(MARGEN + LARGO) * columna + MARGEN,(MARGEN + ALTO) * fila + MARGEN,LARGO,ALTO])
    reloj.tick(60)
    pygame.display.flip()
pygame.quit()