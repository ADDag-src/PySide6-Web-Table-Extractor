from PySide6.QtWidgets import QWidget, QSizePolicy, QHBoxLayout, QLineEdit, QPushButton, QLabel, QVBoxLayout
from PySide6.QtCore import Qt, Signal
from ui.stylesheet_builders import normal_button_stylesheet


class WebsiteSelectWidget(QWidget):
    # ---|custom signals|--- #
    websiteLookUpClicked = Signal()
    localSelectClicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

        # ---|outer layout|--- #
        outer_layout = QVBoxLayout(self)
        outer_layout.setContentsMargins(0, 0, 0, 0)
        outer_layout.setSpacing(6)

        # ---|labels|--- #
        title_label = QLabel("Website Lookup")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-weight: bold; font-size: 22px;")

        subtitle_label = QLabel("Type a public website address or load a local HTML file to detect extractable tables")
        subtitle_label.setAlignment(Qt.AlignCenter)
        subtitle_label.setStyleSheet("color: #888; font-size: 19px;")

        outer_layout.addWidget(title_label)
        outer_layout.addWidget(subtitle_label)

        # ---|horizontal input and button row|--- #
        row_layout = QHBoxLayout()
        row_layout.setContentsMargins(0, 0, 0, 0)
        row_layout.setSpacing(15)

        # --|url input|-- #
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Enter website URL...")
        self.url_input.setFixedWidth(390)

        # --|lookup button|-- #
        self.lookup_button = QPushButton("Lookup")
        self.lookup_button.setStyleSheet(normal_button_stylesheet())
        self.lookup_button.setFixedWidth(100)
        self.lookup_button.clicked.connect(self.websiteLookUpClicked)

        # --|load local|-- #
        self.local_button = QPushButton("Load local HTML")
        self.local_button.setStyleSheet(normal_button_stylesheet())
        self.local_button.setFixedWidth(160)
        self.local_button.clicked.connect(self.localSelectClicked)

        # ---|add widgets|--- #
        row_layout.addStretch()
        row_layout.addWidget(self.url_input)
        row_layout.addWidget(self.lookup_button)
        row_layout.addWidget(self.local_button)
        row_layout.addStretch()

        outer_layout.addLayout(row_layout)
