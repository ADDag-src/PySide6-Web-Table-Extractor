from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QSizePolicy
from PySide6.QtCore import Qt, Signal
from ui.stylesheet_builders import normal_button_stylesheet, red_button_stylesheet


class BottomActionBarWidget(QWidget):
    # ---|custom signals|--- #
    resetClicked = Signal()
    saveClicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

        # ---|layout|--- #
        row_layout = QHBoxLayout(self)
        row_layout.setContentsMargins(0, 0, 0, 0)
        row_layout.setSpacing(15)

        # ---|reset button)|--- #
        self.reset_button = QPushButton("Reset")
        self.reset_button.setStyleSheet(red_button_stylesheet())
        self.reset_button.setFixedWidth(120)
        self.reset_button.clicked.connect(self.resetClicked)

        # ---|extract button|--- #
        self.save_button = QPushButton("Save Selected As...")
        self.save_button.setStyleSheet(normal_button_stylesheet())
        self.save_button.setFixedWidth(160)
        self.save_button.clicked.connect(self.saveClicked)

        # ---|add widgets|--- #
        row_layout.addWidget(self.reset_button, alignment=Qt.AlignLeft)
        row_layout.addStretch()
        row_layout.addWidget(self.save_button, alignment=Qt.AlignRight)