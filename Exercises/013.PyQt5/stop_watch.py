import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)
from PyQt5.QtCore import QTime, QTimer, Qt


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)  # time to be displayed
        self.time_label = QLabel(
            "00:00:00.00", self
        )  # text label will be swapped out when you display time
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)  # Timer that will imit change event each second
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stop Watch")

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        self.setLayout(vbox)

        # time lable styles
        self.time_label.setAlignment(Qt.AlignCenter)

        # for button alignment to make each button aranged verticaly with the time label
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox.addLayout(hbox)  # you can add layout manager within layout managers

        # passing the style sheet
        self.setStyleSheet("""
            QPushButton,Qlabel{
                padding:20px;
                font-weight:bold;
                font-family:calibri;
            }
            QPushButton{
                font-size:50px;
            }

            QLabel{
                font-size:120px;
                background-color:hsl(200,100%,85%);
                border-radius:20px
            }
        """)

        # connecting the buttons with signal and slot
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)

        # coonecting timer to time out signal
        self.timer.timeout.connect(self.update_display)

    def start(self):
        self.timer.start(10)  # for 10 millisecond make a time out event

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.fomat_time(self.time))

    def fomat_time(self, time):
        hours = time.hour()
        mins = time.minute()
        seconds = time.second()
        milli_seconds = time.msec() // 10  # make 2 digit milliseconds
        return f"{hours:02}:{mins:02}:{seconds:02}.{milli_seconds:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.fomat_time(self.time))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())
