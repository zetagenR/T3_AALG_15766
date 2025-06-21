import time


laberinto = [
    ["F", 1, 1, 3, 0, 1, 1, 1, 4],
    [3,   0, 0, 1, 0, 1, 0, 0, 1],
    [1,   1, 0, 1, 1, 1, 1, 0, 1],
    [0,   1, 0, 1, 0, 0, 1, 0, 1],
    [1,   1, 1, 1, 1, 1, 3, 1, 1],
    [3,   0, 1, 0, 0, 0, 1, 0, 1],
    [1,   1, 1, 1, 3, 1, 1, 1, 1],
    [1,   0, 0, 1, 0, 1, 0, 0, 4],
    ["I", 1, 3, 1, 0, 1, 1, 1, 1]
]

inicio = (8, 0)
final = (0, 0)
direcciones = [(-1, 0), (0, 1), (1, 0), (0, -1)]

camino_final = []
puntos_finales = 0
encontrado = False

def es_valido(x, y, visitado):
    return (0 <= x < 9 and 0 <= y < 9 and laberinto[x][y] != 0 and (x, y) not in visitado)

def puntos_extra(x, y):
    return laberinto[x][y] if laberinto[x][y] in [3, 4] else 0

def backtrack(x, y, visitado, camino, puntos):
    global camino_final, puntos_finales, encontrado

    if encontrado:
        return

    camino.append((x, y))
    visitado.add((x, y))

    if laberinto[x][y] not in ["I", "F"]:
        puntos += puntos_extra(x, y)

    if (x, y) == final:
        puntos += 1
        if puntos >= 23:
            camino_final = camino[:]
            puntos_finales = puntos
            encontrado = True
        return

    for dx, dy in direcciones:
        nx, ny = x + dx, y + dy
        if es_valido(nx, ny, visitado):
            backtrack(nx, ny, visitado.copy(), camino[:], puntos)

def imprimir_matriz(camino, delay=True):
    for i in range(9):
        fila = []
        for j in range(9):
            if (i, j) in camino:
                if laberinto[i][j] in ["I", "F"]:
                    fila.append(laberinto[i][j])
                else:
                    fila.append("•")
            else:
                fila.append(str(laberinto[i][j]))
        print("[", ", ".join(fila), "]")
    print()
    if delay:
        time.sleep(0.3)


print("Laberinto original:")
imprimir_matriz([], delay=False)


backtrack(inicio[0], inicio[1], set(), [], 0)


if encontrado:
    print(f"Camino encontrado con {puntos_finales} puntos\n")
    print("Avance paso a paso:\n")
    pasos = []
    for pos in camino_final:
        pasos.append(pos)
        imprimir_matriz(pasos)
    print("Camino completo final:")
    imprimir_matriz(camino_final, delay=False)
else:
    print("No se encontró un camino válido con al menos 23 puntos.")
