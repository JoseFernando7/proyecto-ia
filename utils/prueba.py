from collections import deque    # Módulo de mesa lineal
 
# Primero defina una clase para crear un gráfico, usando la matriz de adyacencia
class Graph(object):
    def __init__(self, *args, **kwargs):
        self.order = []  # visited order
        self.neighbor = {}
 
    def add_node(self, node):
        key, val = node
        if not isinstance(val, list):
            print('La entrada del nodo debe ser una tabla lineal')    # Evite la entrada incorrecta
        self.neighbor[key] = val
 
    # Implementación del algoritmo de ancho primero
    def BFS(self, root):
        # Primero, determine si el nodo raíz es un nodo vacío
        if root != None:
            search_queue = deque()
            search_queue.append(root)
            visited = []
        else:
            print('root is None')
            return -1
 
        while search_queue:
            person = search_queue.popleft()
            self.order.append(person)            
 
            if (not person in visited) and (person in self.neighbor.keys()):
                search_queue += self.neighbor[person]
                visited.append(person)
            
                
             
 
    # Implementación del algoritmo de profundidad primero
    def DFS(self, root):
        # Primero determine si el nodo raíz es un nodo vacío
        if root != None:
            search_queue = deque()
            search_queue.append(root)
 
            visited = []
        else:
            print('root is None')
            return -1
 
        while search_queue:
            person = search_queue.popleft()
            self.order.append(person)
 
            if (not person in visited) and (person in self.neighbor.keys()):
                tmp = self.neighbor[person]
                tmp.reverse()
 
                for index in tmp:
                    search_queue.appendleft(index)
 
                visited.append(person)
 
    def clear(self):
        self.order = []
 
    def node_print(self):
        for index in self.order:
            print(index, end='  ')
 
 
if __name__ == '__main__':
    # Crea un gráfico de árbol binario
    g = Graph()
    g.add_node(('A', ['B', 'F']))
    g.add_node(('B', ['A', 'C']))
    g.add_node(('C', ['B', 'D', 'H']))
    g.add_node(('D', ['C', 'E', 'I']))
    g.add_node(('E', ['D', 'J']))
    g.add_node(('F', ['A', 'K']))
    g.add_node(('H', ['C', 'I']))
    g.add_node(('I', ['D', 'H', 'J']))
    g.add_node(('J', ['E', 'I', 'O']))
    g.add_node(('K', ['F', 'P']))
    g.add_node(('O', ['J', 'T']))
    g.add_node(('P', ['K', 'Q', 'U']))
    g.add_node(('Q', ['P', 'R', 'V']))
    g.add_node(('R', ['Q', 'W']))
    g.add_node(('T', ['O', 'Y']))
    g.add_node(('U', ['P', 'V']))
    g.add_node(('V', ['Q', 'U', 'W']))
    g.add_node(('W', ['R', 'V', 'X']))
    g.add_node(('X', ['W', 'Y']))
    g.add_node(('Y', ['T', 'X']))
 
    # Realice una búsqueda en amplitud
    g.BFS('F')
    print('Amplitud primera búsqueda:')
    print('  ', end='  ')
    g.node_print()
    g.clear()
 
    # Realice la primera búsqueda en profundidad
    print('\ n \ nprimera búsqueda en profundidad:')
    print('  ', end='  ')
    g.DFS('F')
    g.node_print()
    print()
        