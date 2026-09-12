from bs4 import BeautifulSoup
from backend.parsed_table import ParsedTable


class HTMLParser:
    def __init__(self, html: str):
        self.html = html
        self.soup = BeautifulSoup(html, "html.parser")

    def extract_tables(self) -> list[ParsedTable]:
        tables = []
        table_tags = self.soup.find_all("table")

        for index, table_tag in enumerate(table_tags):
            headers, rows = self._parse_table(table_tag)
            name = self._generate_name(table_tag, index)
            tables.append(ParsedTable(name, rows, headers))

        return tables

    @staticmethod
    def _parse_table(table_tag) -> tuple[list[str], list[list[str]]]:
        headers = []
        rows = []

        # ---|parse all rows|--- #
        for tr in table_tag.find_all("tr"):
            cells = tr.find_all(["td", "th"])
            row = [" ".join(cell.stripped_strings) for cell in cells]
            if row:
                rows.append(row)

        # ---|detect headers|--- #
        if table_tag.find_all("th") and rows:
            headers = rows[0]
            rows = rows[1:]
        return headers, rows

    @staticmethod
    def _generate_name(table_tag, index: int) -> str:
        caption = table_tag.find("caption")
        if caption:
            text = " ".join(caption.stripped_strings)
            if text:
                return f"Table {index + 1}: {text}"
        return f"Table {index + 1}: No title"
