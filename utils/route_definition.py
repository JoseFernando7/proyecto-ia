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
    'V': ['Q', 'X'],
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

hijo_izq = arbol2['F'][0]
# print(hijo_izq)

cola = []
cola.append(arbol2['F'][0])
cola.append(arbol2['I'][0])
cola.append(arbol2['K'][0])
cola.append(arbol2['Y'][0])

for element in cola:
    if element != 'T':
        print(element,  end=' -> ')
    else:
        print(element)

def busqueda_preferente_por_amplitud(arbol,  inicio, objetivo):
    cola = []
    cola.append(inicio)
    visitados = []
    while len(cola) > 0:
        nodo_actual = cola.pop(0)
        if nodo_actual not in visitados:
            visitados.append(nodo_actual)
            if nodo_actual == objetivo:
                break
            for siguiente in arbol[nodo_actual]:
                cola.append(siguiente)
    return visitados

# Ejemplo de uso:
camino = busqueda_preferente_por_amplitud(arbol3, 'F', 'B')
print(camino)


def inorder_traversal(arbol, inicio, objetivo):
    # Primero, se busca el nodo de inicio para obtener su hijo izquierdo
    nodo_actual = inicio
    while nodo_actual != objetivo:
        if len(arbol[nodo_actual]) > 0:
            nodo_actual = arbol[nodo_actual][0]
        else:
            break

    # Se comienza a recorrer el árbol en orden
    visitados = []
    while len(visitados) < len(arbol):
        if nodo_actual == objetivo:
            visitados.append(nodo_actual)
            break
        visitados.append(nodo_actual)
        # Se visita el hijo derecho del nodo actual
        if len(arbol[nodo_actual]) > 1:
            nodo_actual = arbol[nodo_actual][1]
        # Si no tiene hijo derecho, se visita el siguiente nodo padre
        elif nodo_actual == inicio:
            break
        else:
            # Busca el siguiente nodo padre
            padre_actual = inicio
            while padre_actual != nodo_actual:
                if len(arbol[padre_actual]) > 1 and arbol[padre_actual][1] == nodo_actual:
                    break
                padre_actual = arbol[padre_actual][0]
            nodo_actual = padre_actual
            # # Se busca el hijo izquierdo del siguiente nodo padre
            # while len(arbol[nodo_actual]) > 0:
            #     nodo_actual = arbol[nodo_actual][0]

    return visitados

# # Ejemplo de uso:
# camino = inorder_traversal(arbol2, 'F', 'Q')
# print(camino)

