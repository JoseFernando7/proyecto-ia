def matriz_a_arbol(matriz):
    arbol = {}
    nodos_validos = set(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y'])
    for i in range(5):
        for j in range(5):
            nodo = chr(ord('A') + i*5 + j)
            hijos = []
            if matriz[i][j] != 5:
                if i > 0 and matriz[i-1][j] != 5:
                    hijos.append(chr(ord('A') + (i-1)*5 + j))
                if j > 0 and matriz[i][j-1] != 5:
                    hijos.append(chr(ord('A') + i*5 + (j-1)))
                if i < 4 and matriz[i+1][j] != 5:
                    hijos.append(chr(ord('A') + (i+1)*5 + j))
                if j < 4 and matriz[i][j+1] != 5:
                    hijos.append(chr(ord('A') + i*5 + (j+1)))
                arbol[nodo] = hijos
                nodos_validos.remove(nodo)
    for nodo in nodos_validos:
        if nodo not in arbol:
            arbol[nodo] = []
    return arbol
