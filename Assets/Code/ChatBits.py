from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication([])

label = QLabel("Hello, World!")
label.setObjectName("label1")
label.setStyleSheet("font: bold 18pt Arial;")
label.font().setPointSize(16)

label.show()
app.exec_()
