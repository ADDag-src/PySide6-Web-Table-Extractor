from backend.parsed_table import ParsedTable


class AppState:
    def __init__(self):
        self.current_website_address: str = ""
        self.website_html: str = ""
        self.tables_list: list[ParsedTable] = []
        self.selected_table_index: int | None = None

    def reset(self):
        self.current_website_address = ""
        self.website_html = ""
        self.tables_list = []
        self.selected_table_index = None
