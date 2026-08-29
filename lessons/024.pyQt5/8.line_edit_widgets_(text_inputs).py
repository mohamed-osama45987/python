import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First GUI")
        self.setGeometry(0, 0, 500, 500)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)
        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(10, 10, 200, 40)
        self.line_edit.setStyleSheet("font-size:25px; font-family:Arial;")
        self.line_edit.setPlaceholderText("Enter you name")

        self.button.setGeometry(210, 10, 100, 40)
        self.button.setStyleSheet("font-size:25px; font-family:Arial;")

        self.button.clicked.connect(self.submit_button_clicked)

    def submit_button_clicked(self):
        # to get the text from the line_edit widget
        value = self.line_edit.text()
        print(f"Hello {value}")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
