class MatrixReading:
    def __init__(self):
        super().__init__()
        self.matrix = []

    def read(self, matrix_path):
        with open(matrix_path, 'r') as file:
            for line in file:
                row = [int(element) for element in line.split()]
                self.matrix.append(row)
