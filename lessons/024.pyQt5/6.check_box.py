import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt  # to get the state of the checkbox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First GUI")
        self.setGeometry(0, 0, 500, 500)
        self.checkbox = QCheckBox("Do you like food?", self)
        self.initUI()

    def initUI(self):
        self.checkbox.setStyleSheet("font-size:30px;" "font-family:Arial;")
        self.checkbox.setGeometry(10, 0, 500, 100)

        # if you want by default the check box is already checked
        self.checkbox.setChecked(True)

        self.checkbox.stateChanged.connect(self.on_check_box_changed)

    def on_check_box_changed(self, state):
        if state == Qt.Checked:
            print("You like food")
        else:
            print("You do not like food")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
