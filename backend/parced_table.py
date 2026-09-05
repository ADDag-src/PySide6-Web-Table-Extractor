class ParsedTable:
    def __init__(self, name: str, rows: list[list[str]], headers: list[str] | None = None):
        self.name = name
        self.headers = headers or []
        self.rows = rows

    def __repr__(self):
        return f"ParsedTable(name={self.name!r}, rows={len(self.rows)} rows)"
