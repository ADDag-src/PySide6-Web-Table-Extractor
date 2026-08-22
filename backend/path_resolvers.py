from pathlib import Path
import sys


def app_dir():
    # --|pyinstaller|-- #
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS)
    # --|nuitka|-- #
    if getattr(sys, "frozen", False):
        return Path(sys.argv[0]).parent

    return Path(sys.argv[0]).parent


def root_dir():
    # --|pyinstaller|-- #
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS).parent
    # --|nuitka|-- #
    if getattr(sys, "frozen", False):
        return Path(sys.argv[0]).parent

    return Path(sys.argv[0]).parent


def app_icon_path():
    icon_dir = app_dir() / "resources" / "icons"
    icon_file = "app-icon.ico" if sys.platform.startswith("win") else "app-icon.png"
    return icon_dir / icon_file


def default_save_dir():
    path = root_dir() / "saved-tables"
    path.mkdir(exist_ok=True)
    return path

