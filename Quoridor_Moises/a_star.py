class Node():
    def __init__(self, padre=None, posicion=None):
        self.padre = padre
        self.posicion = posicion
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.posicion == other.posicion


def a_star(matriz, inicio, final):
    inicio_node = Node(None, inicio)
    inicio_node.g = inicio_node.h = inicio_node.f = 0
    final_node = Node(None, final)
    final_node.g = final_node.h = final_node.f = 0
    open_list = []
    closed_list = []
    open_list.append(inicio_node)
    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == final_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.posicion)
                current = current.padre
            return path[::-1]
        hijos = []
        for nueva_posicion in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            node_posicion = (current_node.posicion[0] + nueva_posicion[0], current_node.posicion[1] + nueva_posicion[1])

            if node_posicion[0] > (len(matriz) - 1) or node_posicion[0] < 0 or node_posicion[1] > (
                    len(matriz[len(matriz) - 1]) - 1) or node_posicion[1] < 0:
                continue

            if matriz[node_posicion[0]][node_posicion[1]] != 0 and matriz[node_posicion[0]][node_posicion[1]] != 2:
                continue


            new_node = Node(current_node, node_posicion)
            hijos.append(new_node)

        for hijo in hijos:
            for closed_hijo in closed_list:
                if hijo == closed_hijo:
                    continue

            hijo.g = current_node.g + 1
            hijo.h = ((hijo.posicion[0] - final_node.posicion[0]) ** 2) + (
                        (hijo.posicion[1] - final_node.posicion[1]) ** 2)
            hijo.f = hijo.g + hijo.h

            for open_node in open_list:
                if hijo == open_node and hijo.g > open_node.g:
                    continue

            open_list.append(hijo)

