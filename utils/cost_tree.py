def arbol_costo(matriz):
    arbol = {}
    nodos_validos = set(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y'])
    for i in range(5):
        for j in range(5):
            nodo = chr(ord('A') + i*5 + j)
            hijos = []
            if matriz[i][j] != 5:
                cost_definition(matriz, i, j)
                
                if i > 0 and matriz[i-1][j] != 5:
                    hijos.append((chr(ord('A') + (i-1)*5 + j), cost_definition(matriz, i-1, j)))
                if j > 0 and matriz[i][j-1] != 5:
                    hijos.append((chr(ord('A') + i*5 + (j-1)), cost_definition(matriz, i, j-1)))
                if i < 4 and matriz[i+1][j] != 5:
                    hijos.append((chr(ord('A') + (i+1)*5 + j), cost_definition(matriz, i+1, j)))
                if j < 4 and matriz[i][j+1] != 5:
                    hijos.append((chr(ord('A') + i*5 + (j+1)), cost_definition(matriz, i, j+1)))
                arbol[nodo] = hijos
                nodos_validos.remove(nodo)
    for nodo in nodos_validos:
        if nodo not in arbol:
            arbol[nodo] = []
    return arbol

def cost_definition(matriz, i, j):
    costo = 0
    if matriz[i][j] == 0 or matriz[i][j] == 2 or matriz[i][j] == 1:
        costo = 1
    elif matriz[i][j] == 3:
        costo = 3
    elif matriz[i][j] == 4:
        costo = 2

    return costo
