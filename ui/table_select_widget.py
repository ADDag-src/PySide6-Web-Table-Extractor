from PySide6.QtWidgets import (QWidget, QSizePolicy, QHBoxLayout, QVBoxLayout, QListWidget, QScrollArea, QTableView,
                               QLabel)
from PySide6.QtCore import Qt


class TableSelectPreviewWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

        # ---|outer layout|--- #
        outer_layout = QVBoxLayout(self)
        outer_layout.setContentsMargins(0, 0, 0, 0)
        outer_layout.setSpacing(6)

        # ---|labels|--- #
        title_label = QLabel("Detected Tables")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-weight: bold; font-size: 22px;")

        subtitle_label = QLabel("Select a table from the list to preview its contents")
        subtitle_label.setAlignment(Qt.AlignCenter)
        subtitle_label.setStyleSheet("color: #888; font-size: 19px;")

        outer_layout.addWidget(title_label)
        outer_layout.addWidget(subtitle_label)

        # ---|horizontal table view row|--- #
        row_layout = QHBoxLayout()
        row_layout.setContentsMargins(0, 0, 0, 0)
        row_layout.setSpacing(15)

        # --|left table list|-- #
        self.list_widget = QListWidget()
        self.list_widget.setMinimumHeight(500)
        self.list_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        list_scroll = QScrollArea()
        list_scroll.setWidgetResizable(True)
        list_scroll.setWidget(self.list_widget)

        # --|right selected table preview|-- #
        self.preview_widget = QTableView()
        self.preview_widget.setMinimumHeight(500)
        self.preview_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # --|add to layout|-- #
        row_layout.addWidget(list_scroll, 1)
        row_layout.addWidget(self.preview_widget, 2)

        outer_layout.addLayout(row_layout)

    def reset(self):
        self.list_widget.clear()
        self.preview_widget.setModel(None)

