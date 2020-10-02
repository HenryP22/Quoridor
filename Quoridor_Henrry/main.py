import pygame, random

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (14, 45, 99)

LARGO = 50
ALTO = 50

MARGEN = 5

grid = []
for fila in range(10):
    grid.append([])
    for columna in range(10):
        grid[fila].append(0)


grid[4][7] = 2
grid[3][7] = 2
grid[2][7]=2
pygame.init()

DIMENSION_VENTANA = [555, 555]
pantalla = pygame.display.set_mode(DIMENSION_VENTANA)

pygame.display.set_caption("Quoridor")
turno = random.randint(1, 2)
hecho = False
reloj = pygame.time.Clock()

while not hecho:
    def blanco():
        for fila in range(10):
            for columna in range(10):
                grid[fila][columna] = 0

    def encontrar_camino(y,x):
        while x < 10:
            if grid[y][x] == 2:
                y = y-1
                x = x -1
                grid[y][x] = 1
            else:
                grid[y][x] = 1
                x = x+1


    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a:
                blanco()
            if evento.key == pygame.K_b:
                turno = 3
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1 and turno == 1:
                turno = 2
                pos = pygame.mouse.get_pos()
                columna = pos[0] // (LARGO + MARGEN)
                fila = pos[1] // (ALTO + MARGEN)
                grid[fila][columna] = 1
                if grid[fila][columna+1] == 2:
                    fila = fila - 1
                    grid[fila][columna] = 3
                elif fila > 9 or grid[fila+1][columna] == 2:
                    fila = fila+1
                    grid[fila][columna] = 3
                else:
                    columna = columna+1
                    grid[fila][columna] = 3

                print("Click ", pos, "Coordenadas de la retícula: ", fila, columna)
            if evento.button == 3 and turno == 2:
                turno = 1
                pos = pygame.mouse.get_pos()
                columna = pos[0] // (LARGO + MARGEN)
                fila = pos[1] // (ALTO + MARGEN)
                grid[fila][columna] = 2
                print("Click ", pos, "Coordenadas de la retícula: ", fila, columna)
            if evento.button == 1 and turno == 3:
                turno = 2
                pos = pygame.mouse.get_pos()
                columna = pos[0] // (LARGO + MARGEN)
                fila = pos[1] // (ALTO + MARGEN)
                grid[fila][columna] = 3
                encontrar_camino(fila, columna)

    pantalla.fill(NEGRO)
    for fila in range(10):
        for columna in range(10):
            color = BLANCO
            if grid[fila][columna] == 1:
                color = VERDE
            if grid[fila][columna] == 2:
                color = AZUL
            if grid[fila][columna] == 0:
                color = BLANCO
            if grid[fila][columna] == 3:
                color = ROJO
            pygame.draw.rect(pantalla, color,
                             [(MARGEN + LARGO) * columna + MARGEN, (MARGEN + ALTO) * fila + MARGEN, LARGO, ALTO])
    reloj.tick(60)
    pygame.display.flip()
pygame.quit()
