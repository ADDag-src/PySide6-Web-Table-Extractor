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
            headers, rows = HTMLParser._parse_table(table_tag)
            name = HTMLParser._generate_name(table_tag, index)
            tables.append(ParsedTable(name, rows, headers))

        return tables

    @staticmethod
    def _parse_table(table_tag) -> tuple[list[str], list[list[str]]]:
        grid = []
        header_row_flags = []
        pending = {}

        table_rows = [tr for tr in table_tag.find_all("tr") if tr.find_parent("table") is table_tag]

        for tr in table_rows:
            cells = tr.find_all(["td", "th"], recursive=False)
            row = []
            col_index = 0
            cell_index = 0
            row_is_header = len(cells) > 0 and all(c.name == "th" for c in cells)

            while cell_index < len(cells) or col_index in pending:
                if col_index in pending:
                    entry = pending[col_index]
                    row.append(entry["value"])
                    entry["remaining"] -= 1
                    if entry["remaining"] <= 0:
                        del pending[col_index]
                    col_index += 1
                    continue

                cell = cells[cell_index]
                text = cell.get_text(" ", strip=True)
                colspan = HTMLParser._get_span_value(cell, "colspan")
                rowspan = HTMLParser._get_span_value(cell, "rowspan")

                for i in range(colspan):
                    row.append(text)
                    if rowspan > 1:
                        pending[col_index + i] = {"value": text, "remaining": rowspan - 1}
                col_index += colspan
                cell_index += 1

            if row:
                grid.append(row)
                header_row_flags.append(row_is_header)

        # ---|decide header row|--- #
        header_row_count = 0
        for flag in header_row_flags:
            if flag:
                header_row_count += 1
            else:
                break

        if header_row_count == 0:
            return [], grid

        headers = grid[header_row_count - 1]
        rows = grid[header_row_count:]
        return headers, rows

    @staticmethod
    def _get_span_value(cell, attr) -> int:
        try:
            value = int(cell.get(attr, 1) or 1)
            return value if value > 0 else 1
        except (TypeError, ValueError):
            return 1

    @staticmethod
    def _generate_name(table_tag, index: int) -> str:
        caption = table_tag.find("caption")
        if caption:
            text = " ".join(caption.stripped_strings)
            if text:
                return f"Table {index + 1}: {text}"
        return f"Table {index + 1}: No title"
