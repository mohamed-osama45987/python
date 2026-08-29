import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First GUI")
        self.setGeometry(
            0, 0, 500, 500
        )  # to control inatial window size when the program first run the args are (x,y,width in px, height in px)

        self.setWindowIcon(QIcon("./Me.jpg"))


def main():
    # argv here represnt comand line arguments if you need to use them
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # this will make the window persist so when the app finish executing it will close
    # without it the window will appear for a breaf second and auto close
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
