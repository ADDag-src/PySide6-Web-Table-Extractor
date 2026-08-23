from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from ui.website_select_widget import WebsiteSelectWidget

DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 1000
MIN_WIDTH = 800


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Web Table Extractor")
        self.resize(DEFAULT_WIDTH, DEFAULT_HEIGHT)
        self.setMinimumSize(MIN_WIDTH, DEFAULT_HEIGHT)

        # -----|UI setup|----- #
        # ---|main widget|--- #
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        # ---|website select top row|--- #
        self.web_select_widget = WebsiteSelectWidget()
        main_layout.addWidget(self.web_select_widget)

        # -----|signal connections|----- #
        self.web_select_widget.websiteLookUpClicked.connect(self.website_lookup_clicked)
        self.web_select_widget.localSelectClicked.connect(self.website_local_clicked)

    def website_lookup_clicked(self):
        pass

    def website_local_clicked(self):
        pass
