from matrix_to_tree import matriz_a_arbol
from matrix_reading import *
from utils.utils import MATRIZ_BUSQUEDA
from cost_tree import arbol_costo
from queue import PriorityQueue

mr = MatrixReading()
mr.read(matrix_path=MATRIZ_BUSQUEDA)
matriz = mr.matrix

arbol = matriz_a_arbol(matriz)
arbol_c = arbol_costo(matriz)


def busqueda_preferente_por_amplitud(arbol, inicio, objetivo):
    cola = []
    cola.append(inicio)
    visitados = []
    while len(cola) > 0:
        ruta_actual = cola.pop(0)
        nodo_actual = ruta_actual[-1]
        if nodo_actual not in visitados:
            visitados.append(nodo_actual)
            if nodo_actual == objetivo:
                return ruta_actual
            for hijo in arbol[nodo_actual]:
                nueva_ruta = list(ruta_actual)
                nueva_ruta.append(hijo)
                cola.append(nueva_ruta)
    return None


def busqueda_por_profundidad_iterativa(arbol, inicio, objetivo, visitados = None):
    if visitados is None:
        visitados = set()
    visitados.add(inicio)
    if inicio == objetivo:
        return [inicio]
    for hijo in arbol[inicio]:
        if hijo not in visitados:
            ruta = busqueda_por_profundidad_iterativa(arbol, hijo, objetivo, visitados)
            if ruta is not None:
                return [inicio] + ruta
    return None

def busqueda_costo_uniforme(arbol, inicio, meta):
    visitados = set()
    cola_prioridad = PriorityQueue()
    cola_prioridad.put((0, [inicio]))
    
    while not cola_prioridad.empty():
        (costo, ruta) = cola_prioridad.get()
        nodo_actual = ruta[-1]
        
        if nodo_actual == meta:
            return ruta
        
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            for hijo, costo_hijo in arbol[nodo_actual]:
                if hijo not in visitados:
                    nueva_ruta = list(ruta)
                    nueva_ruta.append(hijo)
                    nueva_prioridad = costo + costo_hijo
                    cola_prioridad.put((nueva_prioridad, nueva_ruta))
    
    return None



amplitud = busqueda_preferente_por_amplitud(arbol, 'F', 'T')
print(f'Ruta por amplitud: {amplitud}')

profundidad = busqueda_por_profundidad_iterativa(arbol, 'F', 'T')
print(f'Ruta por profundidad: {profundidad}')

costo = busqueda_costo_uniforme(arbol_c, 'F', 'T')
print(f'Ruta por costo: {costo}')
