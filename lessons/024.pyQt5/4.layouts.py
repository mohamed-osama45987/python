import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First GUI")
        self.setGeometry(0, 0, 500, 500)
        self.initUI()

    # for organization it is a common practice to make a function just for ui initiazation
    def initUI(self):
        central_widget = (
            QWidget()
        )  # first we make a widget then add it to the main window
        self.setCentralWidget(central_widget)

        # creating some labels
        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)

        label1.setStyleSheet("background-color:red;")
        label2.setStyleSheet("background-color:yellow;")
        label3.setStyleSheet("background-color:green;")
        label4.setStyleSheet("background-color:blue;")
        label5.setStyleSheet("background-color:purple;")

        # creating the label managers
        #  will make all lables each aranged each on in one row
        # vbox = QVBoxLayout()
        # vbox.addWidget(label1)
        # vbox.addWidget(label2)
        # vbox.addWidget(label3)
        # vbox.addWidget(label4)
        # vbox.addWidget(label5)
        # central_widget.setLayout(vbox)

        # will make all lables each aranged each on in one column
        # hbox = QHBoxLayout()
        # hbox.addWidget(label1)
        # hbox.addWidget(label2)
        # hbox.addWidget(label3)
        # hbox.addWidget(label4)
        # hbox.addWidget(label5)
        # central_widget.setLayout(hbox)

        # to make a grid layout of rows and columns we use QGridLayout
        gridbox = QGridLayout()
        gridbox.addWidget(
            label1, 0, 0
        )  # the additonal arguments is for row number, column number
        gridbox.addWidget(label2, 0, 1)
        gridbox.addWidget(label3, 1, 0)
        gridbox.addWidget(label4, 1, 1)
        gridbox.addWidget(label5, 1, 2)
        central_widget.setLayout(gridbox)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
