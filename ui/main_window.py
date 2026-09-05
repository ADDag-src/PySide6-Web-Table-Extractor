from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
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
        self.web_select_widget.websiteLookUpClicked.connect(self.website_lookup_clicked)
        self.web_select_widget.localSelectClicked.connect(self.website_local_clicked)
        self.bottom_action_row_widget.resetClicked.connect(self.reset_clicked)
        self.bottom_action_row_widget.saveClicked.connect(self.save_clicked)

    def website_lookup_clicked(self):
        user_url = self.web_select_widget.url_input.text()
        print(f"User input: {user_url}")
        raw_html_or_error = self.request_manager.fetch_html(user_url)

        if raw_html_or_error["ok"]:
            html = raw_html_or_error["html"]

            parser = HTMLParser(html)
            parsed_tables = parser.extract_tables()

            print(parsed_tables)

            for table in parsed_tables:
                print(f"#--|{table.name}|--#")
                for row in table.rows:
                    print(row)

    def website_local_clicked(self):
        pass

    def save_clicked(self):
        pass

    def reset_clicked(self):
        self.web_select_widget.reset()
        self.table_select_widget.reset()
        self.app_state.reset()
