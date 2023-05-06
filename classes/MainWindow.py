from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QVBoxLayout, QLabel, QRadioButton, QPushButton, QHBoxLayout

from utils.matrix_reading import *
from utils.matrix_route import MATRIZ_INTERFAZ
from classes.Box import Box


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IA Project")
        self.setGeometry(0, 0, 1200, 600)
        self.show()

        # Layout principal (horizontal)
        main_layout = QHBoxLayout()

        # Widget para el panel izquierdo (cuadrícula de imágenes)
        grid = QGridLayout()
        mr = MatrixReading()
        mr.read(matrix_path=MATRIZ_INTERFAZ)
        self.matriz = mr.matrix

        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                if self.matriz[i][j] == 1:
                    grid.addWidget(Box("", "assets/imgs/pinocho.jpg"), i, j)
                elif self.matriz[i][j] == 2:
                    grid.addWidget(Box("", "assets/imgs/geppeto.jpg"), i, j)
                elif self.matriz[i][j] == 3:
                    grid.addWidget(Box("", "assets/imgs/zorro.jpg"), i, j)
                elif self.matriz[i][j] == 4:
                    grid.addWidget(Box("", "assets/imgs/porro.jpg"), i, j)
                elif self.matriz[i][j] == 5:
                    grid.addWidget(Box("black", ""), i, j)
                else:
                    grid.addWidget(Box("white", ""), i, j)

        # Creamos el widget para el panel izquierdo
        left_panel = QWidget()
        left_panel.setLayout(grid)

        # Widget para el panel derecho (opciones y botón)
        right_panel = QWidget()
        right_layout = QVBoxLayout()
        right_panel.setLayout(right_layout)

        # Opciones para el algoritmo
        #options_label = QLabel("Seleccione un algoritmo:")
        depth_first = QRadioButton("Profundidad")
        breadth_first = QRadioButton("Amplitud")
        uniform_cost = QRadioButton("Costo uniforme")

        # Botón de aceptar
        accept_button = QPushButton("Aceptar")

        # Añadimos los widgets al layout del panel derecho
        #right_layout.addWidget(options_label)
        right_layout.addWidget(depth_first)
        right_layout.addWidget(breadth_first)
        right_layout.addWidget(uniform_cost)
        right_layout.addWidget(accept_button)

        # Añadimos los paneles al layout principal
        main_layout.addWidget(left_panel)
        main_layout.addWidget(right_panel)

        # Widget principal
        main_widget = QWidget()
        main_widget.setLayout(main_layout)

        # Asignamos el widget principal como central
        self.setCentralWidget(main_widget)
