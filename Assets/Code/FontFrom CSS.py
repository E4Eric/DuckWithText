from PyQt5.QtGui import QFont

def setFontFromStyleSheet(font: QFont, styleSheet: str):
    """
    Set the font properties of a QFont object from a style sheet string.
    """
    font.setStyleHint(QFont.SansSerif)  # default style hint
    for property, value in parseStyleSheet(styleSheet):
        if property == "font-family":
            font.setFamily(value)
        elif property == "font-size":
            font.setPointSize(int(value[:-2]))  # value is in pixels, convert to points
        elif property == "font-weight":
            font.setWeight(int(value))
        elif property == "font-style":
            if value == "italic":
                font.setItalic(True)
        elif property == "text-decoration":
            if value == "underline":
                font.setUnderline(True)

def parseStyleSheet(styleSheet: str):
    """
    Parse a style sheet string into a list of (property, value) tuples.
    """
    properties = []
    for rule in styleSheet.split(";"):
        if not rule:
            continue
        property, value = rule.split(":")
        properties.append((property.strip(), value.strip()))
    return properties

-------------------------------------------------------------------------------------

font = QFont()
setFontFromStyleSheet(font, "font-family: Arial; font-size: 12px; font-weight: bold; font-style: italic; text-decoration: underline")

# Set the font of a QWidget
widget.setFont(font)

# Set the default font of a QTextDocument
document.setDefaultFont(font)
