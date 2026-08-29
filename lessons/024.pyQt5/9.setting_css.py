import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Setting style sheet")
        # we do not need to pass self as a second argument here to QpushButton as we are going to use layout manager
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        hbox = QHBoxLayout()  # layout manager
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)
        central_widget.setLayout(hbox)

        # add css selectors as ids
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        # for very large stings we use triple qoutes
        # this will set the style sheet for all buttons in the window and also we can set different styles for each button using their ids
        self.setStyleSheet("""
        QPushButton{
            font-size:40px;
            font-family:Arial;
            padding:15px 75px;
            margin:25px;
            border:3px solid;
            border-radius:15px;
        }

        QPushButton#button1{
            background-color:red;
        }

        QPushButton#button2{
            background-color:green;
        }

        QPushButton#button3{
            background-color:blue;
        }

        QPushButton#button1:hover{
            background-color: lightcoral;
        }

        QPushButton#button2:hover{
            background-color: lightgreen;
        }   

        QPushButton#button3:hover{
            background-color: lightblue;
        }      

""")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
