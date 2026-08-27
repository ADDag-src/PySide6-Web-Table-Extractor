class AppState:
    def __init__(self):
        self.current_website_address: str = ""
        self.website_html: str = ""
        self.tables_list: list[list[list[str]]] = []
        self.selected_table_index: int | None = None
        self.selected_table_data: list[list[str]] | None = None

    def reset(self):
        self.current_website_address = ""
        self.website_html = ""
        self.tables_list = []
        self.selected_table_index = None
        self.selected_table_data = None
