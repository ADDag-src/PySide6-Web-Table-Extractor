from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenuBar
from PySide6.QtCore import Signal


class MainMenu(QMenuBar):
    # ---|custom signals|--- #
    exitClicked = Signal()
    openSaveFolderClicked = Signal()
    appHelpClicked = Signal()
    aboutClicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        # --|file menu|-- #
        file_menu = self.addMenu("File")

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.exitClicked)
        file_menu.addAction(exit_action)

        # --|tools menu|-- #
        tools_menu = self.addMenu("Tools")

        open_export_folder_action = QAction("Open Default Save Folder", self)
        open_export_folder_action.triggered.connect(self.openSaveFolderClicked)
        tools_menu.addAction(open_export_folder_action)

        # --|help menu|-- #
        help_menu = self.addMenu("Help")

        app_help_action = QAction("Tips && Troubleshooting", self)
        app_help_action.triggered.connect(self.appHelpClicked)
        help_menu.addAction(app_help_action)

        about_action = QAction("About", self)
        about_action.triggered.connect(self.aboutClicked)
        help_menu.addAction(about_action)
