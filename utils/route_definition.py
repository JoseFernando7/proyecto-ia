arbol2 = {
    'A': ['B', 'F'],
    'B': ['A', 'C'],
    'C': ['B', 'D', 'H'],
    'D': ['C', 'E', 'I'],
    'E': ['D', 'J'],
    'F': ['A', 'K'],
    'H': ['C', 'I'],
    'I': ['D', 'H', 'J'],
    'J': ['E', 'I', 'O'],
    'K': ['F', 'P'],
    'O': ['J', 'T'],
    'P': ['K', 'Q', 'U'],
    'Q': ['P', 'R', 'V'],
    'R': ['Q', 'W'],
    'T': ['O', 'Y'],
    'U': ['P', 'V'],
    'V': ['Q', 'U', 'W'],
    'W': ['R', 'V', 'X'],
    'X': ['W', 'Y'],
    'Y': ['T', 'X']
}

arbol3 = {
    'F': ['A', 'K'],
    'A': ['B', 'C'],
    'K': ['P'],
    'B': [],
    'C': [],
    'P': [],
}

arbol4 = {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'C': ['F', 'G', 'H'],
    'D': ['I', 'J'],
    'E': [],
    'F': [],
    'G': ['K', 'L'],
    'H': [],
    'I': [],
    'J': [],
    'K': [],
    'L': [],
}

def busqueda_preferente_por_amplitud(arbol, inicio, objetivo):
    cola = []
    cola.append(inicio)
    visitados = []
    # nivel = -1
    while len(cola) > 0:
        # nivel += 1
        # print(f'Nivel {nivel}, cola: {cola}')
        ruta_actual = cola.pop(0)
        nodo_actual = ruta_actual[-1]
        if nodo_actual not in visitados:
            visitados.append(nodo_actual)
            if nodo_actual == objetivo:
                return ruta_actual
            for siguiente in arbol[nodo_actual]:
                nueva_ruta = list(ruta_actual)
                nueva_ruta.append(siguiente)
                cola.append(nueva_ruta)
    return None


# Ejemplo de uso:
camino = busqueda_preferente_por_amplitud(arbol2, 'F', 'T')
print(camino)
