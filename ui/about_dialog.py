from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel
from PySide6.QtCore import Qt


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("About")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 20, 40, 20)
        label = QLabel(
            "<div style='font-size: 15px; text-align: center;'>"
            "<b style='font-size: 18px;'>Web Table Extractor</b><br><br>"
            "Version 1.0<br><br>"
            "Licensed under the MIT License<br><br>"
            "© 2026 ADDag-src<br><br>"
            "Source available on GitHub<br>"
            "https://github.com/ADDag-src/PySide6-Web-Table-Extractor<br>"
            "</div>"
        )

        label.setTextFormat(Qt.RichText)
        label.setTextInteractionFlags(Qt.TextSelectableByMouse)

        layout.addWidget(label)

        self.adjustSize()
        self.setFixedSize(self.size())

        if parent is not None:
            self.move(parent.geometry().center() - self.rect().center())
