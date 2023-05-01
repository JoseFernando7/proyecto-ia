from PyQt5.QtWidgets import QLabel

class Box(QLabel):
    def __init__(self, color, img):
        super().__init__()
        self.setStyleSheet(f"background-image: url({img}); background-color:{color};")
