import sys

from PyQt6.QtCore import QTimer, QTime, QUrl
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtWidgets import QApplication, QMainWindow

import ui


class Main(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.audio = QSoundEffect()
        self.audio.setSource(QUrl.fromLocalFile("media/sound.wav"))

        self.timeEdit.timeChanged.connect(self.set_time)

        self.timer = QTimer()
        self.time = QTime()

        self.timer.timeout.connect(self.show_timer)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)

    def lcd_display(self):
        self.lcdNumber.display(self.time.toString("hh:mm:ss"))

    def set_time(self, value):
        self.time.setHMS(value.hour(), value.minute(), value.second())
        self.lcd_display()

    def show_timer(self):
        if self.time.second() == self.time.minute() == self.time.hour() == 0:
            self.timer.stop()
            self.audio.play()
        else:
            self.time = self.time.addSecs(-1)
            self.lcd_display()

    def start(self):
        self.set_time(self.timeEdit.time())
        self.timer.start(1000)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.timeEdit.setTime(QTime(0, 0, 0))
        self.time.setHMS(0, 0, 0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Main()
    win.show()
    sys.exit(app.exec())
