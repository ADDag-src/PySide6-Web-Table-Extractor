def normal_button_stylesheet(font_size=15):
    return f"""
        QPushButton {{
            color: white;
            background-color: #4C63B8;
            font-size: {font_size}px;
            padding: 6px 12px;
            border-radius: 4px;
        }}

        QPushButton:hover {{
            background-color: #174a91;
        }}

        QPushButton:disabled {{
            background-color: #444;
            color: #888;
            border: 1px solid #555;
            font-size: {font_size}px;
        }}
    """


def red_button_stylesheet(font_size=15):
    return f"""
        QPushButton {{
            color: white;
            background-color: #B02020;
            font-size: {font_size}px;
            padding: 6px 12px;
            border-radius: 4px;
        }}

        QPushButton:hover {{
            background-color: #8A1A1A;
        }}

        QPushButton:disabled {{
            background-color: #444;
            color: #888;
            border: 1px solid #555;
            font-size: {font_size}px;
        }}
    """


