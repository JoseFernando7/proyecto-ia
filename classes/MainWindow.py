from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout
from utils.matrix_reading import *
from classes.Box import Box


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IA Project")
        self.setGeometry(0, 0, 600, 600)
        self.show()
        mr = MatrixReading()
        mr.read(matrix_path="matrices/matriz.txt")
        self.matriz = mr.matrix

        # Creamos un layout en cuadrícula
        grid = QGridLayout()

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

        # Creamos el widget dummy y le asignamos el layout horizontal
        widget = QWidget()
        widget.setLayout(grid)

        self.setCentralWidget(widget)
