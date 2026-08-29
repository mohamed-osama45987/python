import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import (
    QPixmap,
)  # used to handle images loading manipulate and displaying images


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)

        lable = QLabel(self)
        lable.setGeometry(0, 0, 250, 250)

        # image pix map
        pix_map = QPixmap("./Me.jpg")

        lable.setPixmap(pix_map)
        lable.setScaledContents(
            True
        )  # to make the image scale to the size of the label

        lable.setGeometry(
            self.width() - lable.width(),  # to right justify the image on x-axis
            self.height()
            - lable.height(),  # to make the image at the buttom of the window
            lable.width(),
            lable.height(),
        )

        # to make the image at the center
        lable.setGeometry(
            (self.width() - lable.width())
            // 2,  # here we need the pixiles to be hole nums this is why we used // called intnger devision
            (self.height() - lable.height()) // 2,
            lable.width(),
            lable.height(),
        )


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
