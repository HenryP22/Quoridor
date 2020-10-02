grid = []
for fila in range(10):
    grid.append([])
    for columna in range(10):
        grid[fila].append(0)
x=0
y=4

while x < 9:
    if grid[y][x] == 2:
        y = -1
    else:
        x = +1
    grid[x][y] = 1

print(grid)