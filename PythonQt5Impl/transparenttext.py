import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QFont

app = QApplication(sys.argv)

# Create a label with the text that you want to draw
label = QLabel('This is some text')

# Set the font for the label
label.setFont(QFont('Arial', 16))

# Set the background color of the label to transparent using CSS
label.setStyleSheet('background-color: transparent')

# Set the text color to white
label.setStyleSheet('color: white')

# Show the label
label.show()

sys.exit(app.exec_())
