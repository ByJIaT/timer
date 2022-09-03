import sys

from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtCore import QTimer, QTime, QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow


import timer


class Main(QMainWindow, timer.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.audio = QSoundEffect()
        self.audio.setSource(QUrl.fromLocalFile('Ring02.wav'))

        self.lcdNumber.setNumDigits(8)

        self.timeEdit.timeChanged.connect(self.set_time)

        self.timer = QTimer()
        self.time = QTime()

        self.timer.timeout.connect(self.show_timer)

        self.pushButton.clicked.connect(self.start)
        self.pushButton_2.clicked.connect(self.stop)
        self.pushButton_3.clicked.connect(self.reset)

    def set_time(self, value):
        secs = value.second()
        mins = value.minute()
        hours = value.hour()
        self.time.setHMS(hours, mins, secs)
        self.lcdNumber.display(self.time.toString('hh:mm:ss'))

    def show_timer(self):
        if self.time.second() == self.time.minute() == self.time.hour() == 0:
            self.timer.stop()
            self.audio.play()
        else:
            self.time = self.time.addSecs(-1)
            self.lcdNumber.display(self.time.toString('hh:mm:ss'))

    def start(self):
        self.timer.start(1000)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.timeEdit.setTime(QTime(0, 0, 0))
        self.time.setHMS(0, 0, 0)
        self.lcdNumber.display(self.time.toString('hh:mm:ss'))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = Main()
    win.show()
    sys.exit(app.exec())
