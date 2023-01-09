import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create a button and set its text to "Hello"
        helloButton = QPushButton("Hello", self)
        helloButton.resize(helloButton.sizeHint())

        # Set the button's style sheet to set the text color to red
        helloButton.setStyleSheet("color: red;")

        # Set the button as the central widget of the main window
        self.setCentralWidget(helloButton)

        # Connect the button's clicked signal to the sayHello slot
        helloButton.clicked.connect(self.sayHello)

        # Set the window properties
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Hello Button")
        self.show()

    def sayHello(self):
        # Display a message box with the "Hello" message
        QMessageBox.information(self, "Hello", "Hello World!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
