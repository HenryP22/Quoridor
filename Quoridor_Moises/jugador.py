
class movimientoJugador():
    def __init__(self,grid,posicionJugador):
        self.grid = grid
        self.posicionJugador = posicionJugador
    def movimientoArriba(self):
        if (self.grid[self.posicionJugador[0] - 1][self.posicionJugador[1]] != 1 and
                self.grid[self.posicionJugador[0] - 1][
                    self.posicionJugador[1]] != 4):
            if (self.posicionJugador[0] > 0):
                self.grid[self.posicionJugador[0] - 1][self.posicionJugador[1]] = 3
                self.grid[self.posicionJugador[0]][self.posicionJugador[1]] = 0
                self.posicionJugador = (self.posicionJugador[0] - 1, self.posicionJugador[1])
                return self.posicionJugador
    def movimientoAbajo(self):
        if (self.grid[self.posicionJugador[0] + 1][self.posicionJugador[1]] != 1 and self.grid[self.posicionJugador[0] + 1][
            self.posicionJugador[1]] != 4):
            if (self.posicionJugador[0] < 9):
                self.grid[self.posicionJugador[0] + 1][self.posicionJugador[1]] = 3
                self.grid[self.posicionJugador[0]][self.posicionJugador[1]] = 0
                self.posicionJugador = (self.posicionJugador[0] + 1, self.posicionJugador[1])
                return self.posicionJugador
    def movimientoDerecha(self):
        if (self.grid[self.posicionJugador[0]][self.posicionJugador[1] + 1] != 1 and self.grid[self.posicionJugador[0]][
            self.posicionJugador[1] + 1] != 4):
            if (self.posicionJugador[0] < 9):
                self.grid[self.posicionJugador[0]][self.posicionJugador[1] + 1] = 3
                self.grid[self.posicionJugador[0]][self.posicionJugador[1]] = 0
                self.posicionJugador = (self.posicionJugador[0], self.posicionJugador[1] + 1)
                return self.posicionJugador
    def movimientoIzquierda(self):
        if (self.grid[self.posicionJugador[0]][self.posicionJugador[1] - 1] != 1 and
                self.grid[self.posicionJugador[0]][
                    self.posicionJugador[1] - 1] != 4):
            if (self.posicionJugador[0] > 0):
                self.grid[self.posicionJugador[0]][self.posicionJugador[1] - 1] = 3
                self.grid[self.posicionJugador[0]][self.posicionJugador[1]] = 0
                self.posicionJugador = (self.posicionJugador[0], self.posicionJugador[1] - 1)
                return self.posicionJugador