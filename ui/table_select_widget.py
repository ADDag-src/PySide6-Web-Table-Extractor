from PySide6.QtWidgets import (QWidget, QSizePolicy, QHBoxLayout, QVBoxLayout, QListWidget, QScrollArea, QTableView,
                               QLabel, QHeaderView)
from PySide6.QtCore import Qt, Signal
from backend.parsed_table import ParsedTable
from PySide6.QtGui import QStandardItemModel, QStandardItem


class TableSelectPreviewWidget(QWidget):
    # ---|custom signals|--- #
    tableSelected = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

        self.tables = []

        # ---|outer layout|--- #
        outer_layout = QVBoxLayout(self)
        outer_layout.setContentsMargins(0, 0, 0, 0)
        outer_layout.setSpacing(6)

        # ---|labels|--- #
        title_label = QLabel("Detected Tables")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-weight: bold; font-size: 22px;")

        subtitle_label = QLabel("Select a table from the list to preview its contents")
        subtitle_label.setAlignment(Qt.AlignCenter)
        subtitle_label.setStyleSheet("color: #888; font-size: 19px;")

        outer_layout.addWidget(title_label)
        outer_layout.addWidget(subtitle_label)

        # ---|horizontal table view row|--- #
        row_layout = QHBoxLayout()
        row_layout.setContentsMargins(0, 0, 0, 0)
        row_layout.setSpacing(15)

        # --|left table list|-- #
        self.list_widget = QListWidget()
        self.list_widget.setMinimumHeight(500)
        self.list_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.list_widget.setStyleSheet("font-size: 16px;")
        self.list_widget.currentRowChanged.connect(self._table_selected_changed)

        list_scroll = QScrollArea()
        list_scroll.setWidgetResizable(True)
        list_scroll.setWidget(self.list_widget)

        # --|right selected table preview|-- #
        self.preview_widget = QTableView()
        self.preview_widget.setMinimumHeight(500)
        self.preview_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.preview_widget.setEditTriggers(QTableView.NoEditTriggers)
        self.preview_widget.setAlternatingRowColors(True)

        header = self.preview_widget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Interactive)
        header.setStretchLastSection(True)

        # --|add to layout|-- #
        row_layout.addWidget(list_scroll, 1)
        row_layout.addWidget(self.preview_widget, 2)

        outer_layout.addLayout(row_layout)

    def set_tables(self, tables: list[ParsedTable]):
        self.reset()
        self.tables = tables

        for table in self.tables:
            self.list_widget.addItem(table.name)

    def _table_selected_changed(self, index):
        if index < 0 or index >= len(self.tables):
            self.preview_widget.setModel(None)
            return

        # ---|update state|--- #
        self.tableSelected.emit(index)

        # ---|build preview model and display|--- #
        table = self.tables[index]
        model = self._build_model(table)
        self.preview_widget.setModel(model)
        self.preview_widget.horizontalHeader().resizeSections(QHeaderView.ResizeToContents)

    @staticmethod
    def _build_model(table: ParsedTable):
        model = QStandardItemModel()

        # ---|headers|--- #
        if table.headers:
            model.setColumnCount(len(table.headers))
            model.setHorizontalHeaderLabels(table.headers)

        # ---|rows|--- #
        for row in table.rows:
            items = [QStandardItem(str(cell)) for cell in row]
            model.appendRow(items)

        return model

    def reset(self):
        self.tables = []
        self.list_widget.clear()
        self.preview_widget.setModel(None)

