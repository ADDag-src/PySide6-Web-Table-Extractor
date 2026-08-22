from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Web Table Extractor")
        self.setFixedWidth(800)
        self.setFixedHeight(1000)
