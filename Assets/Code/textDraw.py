from PyQt5.QtGui import QColor, QFont, QPainter, QPen
from PyQt5.QtWidgets import QWidget

class MyWidget(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)

        # Set the font
        font = QFont("Tacoma", 16, QFont.Italic)
        painter.setFont(font)

        # Set the pen color to red
        pen = QPen(QColor(255, 0, 0))
        painter.setPen(pen)

        # Draw the text
        painter.drawText(10, 50, "Hello World")

widget = MyWidget()
widget.show()
