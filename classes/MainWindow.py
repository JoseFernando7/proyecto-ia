from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QVBoxLayout, QPushButton, QHBoxLayout, QSizePolicy

from utils.matrix_reading import *
from utils.utils import MATRIZ_INTERFAZ, NODO_INICIO, NODO_META
from utils.route_definition import busqueda_preferente_por_amplitud, busqueda_por_profundidad_iterativa, busqueda_costo_uniforme
from utils.matrix_to_tree import matriz_a_arbol
from utils.cost_tree import arbol_costo
from classes.Box import Box


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IA Project")
        self.setGeometry(0, 0, 750, 600)
        self.show()

        self.depth_first = QPushButton("Profundidad")
        self.breadth_first = QPushButton("Amplitud")
        self.uniform_cost = QPushButton("Costo uniforme")

        self.ruta = []

        # Layout principal (horizontal)
        self.main_layout = QHBoxLayout()

        # Widget para el panel izquierdo (cuadrícula de imágenes)
        self.grid = QGridLayout()

        mr = MatrixReading()
        mr.read(matrix_path=MATRIZ_INTERFAZ)
        self.matriz = mr.matrix
        self.arbol = matriz_a_arbol(self.matriz)
        self.arbol_c = arbol_costo(self.matriz)
        self.nodo_inicio = NODO_INICIO
        self.nodo_meta = NODO_META

        self.create_interface()

        self.breadth_first.clicked.connect(self.amplitud)
        self.depth_first.clicked.connect(self.profundidad)
        self.uniform_cost.clicked.connect(self.costo)

    def create_interface(self):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                color_empty = "white"
                geppeto = "assets/imgs/geppeto.jpg"
                porro = "assets/imgs/porro.jpg"
                zorro = "assets/imgs/zorro.jpg"

                # Si la letra de la celda está en la ruta, la resaltamos en verde
                letra = chr(ord('A') + i*5 + j)
                if letra in self.ruta:
                    color_empty = "green"
                    geppeto = "assets/imgs/geppeto-verde.jpg"
                    porro = "assets/imgs/porro-verde.jpg"
                    zorro = "assets/imgs/zorro-verde.jpg"

                if self.matriz[i][j] == 1:
                    self.grid.addWidget(Box("", "assets/imgs/pinocho.jpg"), i, j)
                elif self.matriz[i][j] == 2:
                    self.grid.addWidget(Box("", geppeto), i, j)
                elif self.matriz[i][j] == 3:
                    self.grid.addWidget(Box("", zorro), i, j)
                elif self.matriz[i][j] == 4:
                    self.grid.addWidget(Box("", porro), i, j)
                elif self.matriz[i][j] == 5:
                    self.grid.addWidget(Box("black", ""), i, j)
                else:
                    self.grid.addWidget(Box(color_empty, ""), i, j)
                    
        # Creamos el widget para el panel izquierdo
        left_panel = QWidget()
        left_panel.setGeometry(0, 0, 600, 600)
        left_panel.setLayout(self.grid)

        # Widget para el panel derecho (opciones y botón)
        right_panel = QWidget()
        right_panel.setGeometry(600, 0, 500, 600)
        right_layout = QVBoxLayout()
        right_panel.setLayout(right_layout)

        # Añadimos los widgets al layout del panel derecho
        #right_layout.addWidget(options_label)
        right_layout.addWidget(self.depth_first)
        right_layout.addWidget(self.breadth_first)
        right_layout.addWidget(self.uniform_cost)

        # Añadimos los paneles al layout principal
        self.main_layout.addWidget(left_panel)
        self.main_layout.addWidget(right_panel)

        left_panel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        right_panel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)

        # Widget principal
        main_widget = QWidget()
        main_widget.setLayout(self.main_layout)

        # Asignamos el widget principal como central
        self.setCentralWidget(main_widget)

    def amplitud(self):
        amplitud = busqueda_preferente_por_amplitud(self.arbol, self.nodo_inicio, self.nodo_meta)
        self.ruta = amplitud
        self.create_interface()

    def profundidad(self):
        profundidad = busqueda_por_profundidad_iterativa(self.arbol, self.nodo_inicio, self.nodo_meta)
        self.ruta = profundidad
        self.create_interface()

    def costo(self):
        costo = busqueda_costo_uniforme(self.arbol_c, self.nodo_inicio, self.nodo_meta)
        self.ruta = costo
        self.create_interface()
