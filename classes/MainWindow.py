from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout
from utils.matrix_reading import *
from classes.Caja import Caja


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
        cuadricula = QGridLayout()

        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                if self.matriz[i][j] == 1:
                    cuadricula.addWidget(Caja("", "assets/imgs/pinocho.jpg"), i, j)
                elif self.matriz[i][j] == 2:
                    cuadricula.addWidget(Caja("", "assets/imgs/geppeto.jpg"), i, j)
                elif self.matriz[i][j] == 3:
                    cuadricula.addWidget(Caja("", "assets/imgs/zorro.jpg"), i, j)
                elif self.matriz[i][j] == 4:
                    cuadricula.addWidget(Caja("", "assets/imgs/porro.jpg"), i, j)
                elif self.matriz[i][j] == 5:
                    cuadricula.addWidget(Caja("black", ""), i, j)
                else:
                    cuadricula.addWidget(Caja("white", ""), i, j)

        # Creamos el widget dummy y le asignamos el layout horizontal
        widget = QWidget()
        widget.setLayout(cuadricula)

        self.setCentralWidget(widget)
