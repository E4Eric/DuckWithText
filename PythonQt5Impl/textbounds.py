import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QFontMetrics, QFont

app = QApplication(sys.argv)

# Create a label with the text that you want to get the bounding box for
label = QLabel('This is some text')

# Set the font for the label
label.setFont(QFont('Arial', 16))

# Get the font metrics for the label's font
font_metrics = QFontMetrics(label.font())

# Get the bounding box for the text in the label
bounding_box = font_metrics.boundingRect(label.text())

# Print the bounding box dimensions
print(f'Width: {bounding_box.width()}')
print(f'Height: {bounding_box.height()}')

sys.exit(app.exec_())
