from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMessageBox
from ui.website_select_widget import WebsiteSelectWidget
from ui.table_select_widget import TableSelectPreviewWidget
from ui.bottom_action_widget import BottomActionBarWidget
from backend.app_state_class import AppState
from backend.request_manager import RequestManager
from backend.html_parse_class import HTMLParser

DEFAULT_WIDTH = 960
DEFAULT_HEIGHT = 1000
MIN_WIDTH = 900


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Web Table Extractor")
        self.resize(DEFAULT_WIDTH, DEFAULT_HEIGHT)
        self.setMinimumSize(MIN_WIDTH, DEFAULT_HEIGHT)

        # -----|app state|----- #
        self.request_manager = RequestManager()
        self.app_state = AppState()

        # -----|UI setup|----- #
        # ---|main widget|--- #
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        main_layout.setSpacing(50)
        main_layout.setContentsMargins(30, 30, 30, 30)

        # ---|website select top row|--- #
        self.web_select_widget = WebsiteSelectWidget()
        main_layout.addWidget(self.web_select_widget)

        # ---|table select and preview row|--- #
        self.table_select_widget = TableSelectPreviewWidget()
        main_layout.addWidget(self.table_select_widget)

        main_layout.addStretch()

        # ---|bottom action row|--- #
        self.bottom_action_row_widget = BottomActionBarWidget()
        main_layout.addWidget(self.bottom_action_row_widget)

        # -----|signal connections|----- #
        self.web_select_widget.websiteLookUpClicked.connect(self._website_lookup_clicked)
        self.web_select_widget.localSelectClicked.connect(self._website_local_clicked)
        self.bottom_action_row_widget.resetClicked.connect(self.reset_clicked)
        self.bottom_action_row_widget.saveClicked.connect(self.save_clicked)
        self.table_select_widget.tableSelected.connect(self.table_selected)

    def _website_lookup_clicked(self):
        user_url = self.web_select_widget.url_input.text()
        result = self.request_manager.fetch_html(user_url)

        # ---|error handling|--- #
        if not result["ok"]:
            error_text = result["error"]

            # --|exception|-- #
            if error_text.strip().startswith("INTERNAL_EXCEPTION:"):
                full_details = error_text.replace("INTERNAL_EXCEPTION:", "")
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Request Error")
                msg.setText("Something went wrong while loading the page.")
                msg.setDetailedText(full_details)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
                return

            # --|normal errors|-- #
            QMessageBox.warning(self, "Request Error", error_text)
            return

        html = result["html"]
        self._parse_html_into_state(user_url, html)

    def _website_local_clicked(self):
        pass

    def _parse_html_into_state(self, user_url: str, html: str):
        # ---|html parsing|--- #
        parser = HTMLParser(html)
        parsed_tables = parser.extract_tables()

        if not parsed_tables:
            QMessageBox.information(self, "No Tables Found", "The page contains no HTML tables.")
            return

        # ---|update state|--- #
        self.app_state.reset()
        self.app_state.current_website_address = user_url
        self.app_state.website_html = html
        self.app_state.tables_list = parsed_tables
        self.app_state.selected_table_index = None

        QMessageBox.information(self, f"Success!", f"{len(parsed_tables)} HTML tables Found!")

        # ---|populate UI|--- #
        self.table_select_widget.set_tables(parsed_tables)

    def save_clicked(self):
        pass

    def table_selected(self, index):
        self.app_state.selected_table_index = index

    def reset_clicked(self):
        self.web_select_widget.reset()
        self.table_select_widget.reset()
        self.app_state.reset()
