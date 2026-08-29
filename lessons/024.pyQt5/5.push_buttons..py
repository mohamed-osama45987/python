import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Push Button")
        self.setGeometry(0, 0, 500, 500)
        self.button = QPushButton("Click Me!", self)
        self.lable = QLabel("Hello", self)
        self.initUI()

    def initUI(self):
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size:30px;")

        # to make event listners
        # here we call it signal and slot , signal is what i am listining for and the slot is what
        # is going to happen when the event i am listning for fire
        # in this example the signal is clicked and the self.on_click is the slot and the .connect is just to bind both
        self.button.clicked.connect(self.on_click)

        # adding text label
        self.lable.setGeometry(150, 300, 200, 100)
        self.lable.setStyleSheet("font-size:50px;")

    def on_click(self):
        print("Button clicked")
        self.button.setText("Clicked!")
        self.button.setDisabled(True)  # to disable a button after clicking on it
        # change a text on a sperate label
        self.lable.setText("GoodBye")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
