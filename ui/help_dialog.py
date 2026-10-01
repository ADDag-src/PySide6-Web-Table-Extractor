from PySide6.QtWidgets import QDialog, QVBoxLayout, QTextBrowser, QFrame
from PySide6.QtCore import Qt


class AppHelpDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Tips & Troubleshooting")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)

        html = (
            "<div style='font-size: 15px; text-align: center; font-weight: bold;'>"
            "Tips & Troubleshooting"
            "</div>"

            "<div style='font-size: 15px; text-align: left; margin-top: 12px;'>"

            "<b>Page Won't Load</b><br>"
            "If a URL fails to load, the site may be blocking automated requests, or the page may "
            "require a login. This tool only works with publicly accessible pages.<br><br>"

            "<b>Non Public Pages</b><br>"
            "If a table is on a page that requires signing in, save the page's HTML from your browser "
            "(Ctrl+S, or Save Page As from the browser menu) and use 'Load Local HTML' instead. "
            "Accepted file types are .html, .htm, and .xhtml.<br><br>"
            
            "<b>No Tables Found</b><br>"
            "This tool looks for standard HTML &lt;table&gt; tags. If a page builds its table "
            "another way (like JavaScript or CSS grids), it likely won't be detected. "
            "Saving the loaded page (Ctrl+S) and using 'Load Local HTML' is worth trying, "
            "since it sometimes still contains &lt;table&gt; tags the app can detect.<br><br>"

            "<b>Header Misalignment Warning</b><br>"
            "Some web tables use messy or unusual header layouts. If you see "
            "'POTENTIAL HEADER MISALIGNMENT' in your exported file, double check the column names "
            "manually before using the data.<br><br>"

            "<b>Export Formats</b><br>"
            "Tables can be saved as Excel (.xlsx) or CSV (.csv) files.<br><br>"

            "</div>"
        )

        text = QTextBrowser()
        text.setHtml(html)
        text.setReadOnly(True)
        text.setOpenExternalLinks(False)
        text.setFrameShape(QFrame.NoFrame)
        text.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        text.setStyleSheet("QTextBrowser { background: transparent; padding: 0; margin: 0; border: none; }")
        text.document().setDocumentMargin(0)

        layout.addWidget(text)

        self.adjustSize()
        min_width = 650
        min_height = 450

        if self.width() < min_width:
            self.resize(min_width, self.height())
        if self.height() < min_height:
            self.resize(self.width(), min_height)

        self.setFixedSize(self.size())

        if parent is not None:
            self.move(parent.geometry().center() - self.rect().center())