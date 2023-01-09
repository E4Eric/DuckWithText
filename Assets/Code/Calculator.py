import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
                             QPushButton, QVBoxLayout, QWidget)


class Calculator(QMainWindow):

    def __init__(self):
        super().__init__()

        # Set up the user interface
        self.initUI()

    def initUI(self):
        # Create the display and the buttons
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        button_names = [
            '7', '8', '9', '/', '(', ')', 'C',
            '4', '5', '6', '*', '1', '2', '3', '-',
            '0', '.', '=', '+',
        ]
        button_names = [
            '1', '2', '3', '+',
            '4', '5', '6', '-',
            '7', '8', '9', 'x',
            'C', '0', '.', '/',
            '(', '=', ')',
        ]

        self.buttons = {}
        for i, name in enumerate(button_names):
            button = QPushButton(name)
            self.buttons[name] = button
            button.released.connect(self.button_released)

        # Set up the layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.display)

        grid_layout = QGridLayout()
        main_layout.addLayout(grid_layout)

        for i, name in enumerate(button_names):
            button = self.buttons[name]
            grid_layout.addWidget(button, i // 4, i % 4)

        # Set the central widget and the window properties
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
        self.setWindowTitle('Calculator')

    def button_released(self):
        sender = self.sender()
        self.display.setText(self.display.text() + sender.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
