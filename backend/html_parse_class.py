from bs4 import BeautifulSoup
from backend.parced_table import ParsedTable


class HTMLParser:
    def __init__(self, html: str):
        self.html = html
        self.soup = BeautifulSoup(html, "html.parser")

    def extract_tables(self) -> list[ParsedTable]:
        tables = []
        table_tags = self.soup.find_all("table")

        for index, table_tag in enumerate(table_tags):
            rows = self.parse_table(table_tag)
            name = self.generate_name(table_tag, index)
            tables.append(ParsedTable(name, rows))

        return tables

    @staticmethod
    def parse_table(table_tag) -> list[list[str]]:
        rows = []
        for tr in table_tag.find_all("tr"):
            cells = tr.find_all(["td", "th"])
            row = [" ".join(cell.stripped_strings) for cell in cells]
            if row:
                rows.append(row)
        return rows

    @staticmethod
    def generate_name(table_tag, index: int) -> str:
        caption = table_tag.find("caption")
        if caption:
            text = " ".join(caption.stripped_strings)
            if text:
                return f"Table {index + 1}: {text}"
        return f"Table {index + 1}: No title"

