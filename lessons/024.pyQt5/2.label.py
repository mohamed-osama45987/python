import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt  # used to alignments


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First GUI")
        self.setGeometry(
            0, 0, 500, 500
        )  # to control inatial window size when the program first run the args are (x,y,width in px, height in px)
        # labels can display text or images
        lable = QLabel("Hello world", self)
        lable.setFont(QFont("Arial", 40))
        lable.setGeometry(0, 0, 500, 100)
        # css like properties
        lable.setStyleSheet(
            "color:black;"
            "background-color:blue;"
            "font-weight:bold;"
            "font-style:italic;"
            "text-decoration:underline"
        )
        # y-axis
        lable.setAlignment(Qt.AlignTop)  # align vertacaly to the top
        lable.setAlignment(Qt.AlignBottom)  # align verticaly to bottom
        lable.setAlignment(Qt.AlignVCenter)  # align vertical to the center

        # x-axis
        lable.setAlignment(Qt.AlignRight)  # align right horizontaly
        lable.setAlignment(Qt.AlignLeft)  # align left horiziontaly
        lable.setAlignment(Qt.AlignHCenter)  # align center horiziontaly

        # you can combine horziltal and vertical alignment in 1 statment (x, y)
        lable.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        # if you want x and y to align center
        lable.setAlignment(Qt.AlignCenter)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # this will make the window persist so when the app finish executing it will close
    # without it the window will appear for a breaf second and auto close
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
