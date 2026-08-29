import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First GUI")
        self.setGeometry(700, 300, 500, 500)
        # defining radio buttons
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("Master card", self)
        self.radio3 = QRadioButton("Gift card", self)
        # will be added to be used as second radio button group
        self.radio4 = QRadioButton("Online", self)
        self.radio5 = QRadioButton("In-store", self)

        # declare button group
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)
        self.initUI()

    def initUI(self):
        # changing postions and width and hieght
        self.radio1.setGeometry(0, 0, 300, 50)
        self.radio2.setGeometry(0, 50, 300, 50)
        self.radio3.setGeometry(0, 100, 300, 50)
        self.radio4.setGeometry(0, 150, 300, 50)
        self.radio5.setGeometry(0, 200, 300, 50)

        # a trick to apply css props to entire group of widgets
        self.setStyleSheet(
            "QRadioButton{" "font-size:40px;" "font-family:Arial;" "padding:10px;" "}"
        )

        # using radio button groups
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)

        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        # adding slots
        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)

    def radio_button_changed(self):
        # to dermine which button is clicked you must find the sender of the event
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is Selected")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
