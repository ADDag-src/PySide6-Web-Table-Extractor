from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
import backend.path_resolvers as paths
from backend.palette_maker import create_dark_palette
from ui.main_window import MainWindow


if __name__ == "__main__":
    app = QApplication()
    app.setStyle("Fusion")
    app.setPalette(create_dark_palette())

    icon_path = paths.app_icon_path()

    if icon_path.exists():
        app.setWindowIcon(QIcon(str(icon_path)))

    main_window = MainWindow()
    main_window.show()
    app.exec()
