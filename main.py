import os

import sys
from PyQt4 import QtGui

from threading import Timer


class PyAlarm():
    timer = None

    @staticmethod
    def stop_timer():
        if PyAlarm.timer is not None:
            PyAlarm.timer.cancel()

    @staticmethod
    def init_timer(time_in_seconds):
        PyAlarm.stop_timer()

        PyAlarm.timer = Timer(time_in_seconds, PyAlarm.timer_expired, ())
        PyAlarm.timer.start()

    @staticmethod
    def timer_expired():
        #TODO configuration for notification method, and error handling - OS without notify-send
        os.system("notify-send 'Timer expired.'")

        #TODO easier method to play sound
        import pygame

        pygame.init()
        # notify_sound_name = 'notify_sound.wav'
        song = pygame.mixer.Sound("/home/evilkhaoskat/projects/python/PyAlarm/Mallet.ogg")
        song.play()

    @staticmethod
    def exit():
        PyAlarm.stop_timer()
        sys.exit(0)


#TODO gui configuration of time for alarm clock
class SystemTrayIcon(QtGui.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        QtGui.QSystemTrayIcon.__init__(self, icon, parent)
        self.menu = QtGui.QMenu(parent)

        in_10_sec_action = self.menu.addAction("In 00:00:10")
        in_10_sec_action.triggered.connect(lambda: PyAlarm.init_timer(10))

        in_half_min_action = self.menu.addAction("In 00:00:30")
        in_half_min_action.triggered.connect(lambda: PyAlarm.init_timer(30))

        self.menu.addSeparator()

        # TODO timers presets to be configurable
        in_1_min_action = self.menu.addAction("In 00:01:00")
        in_1_min_action.triggered.connect(lambda: PyAlarm.init_timer(60))

        in_2_min_action = self.menu.addAction("In 00:02:00")
        in_2_min_action.triggered.connect(lambda: PyAlarm.init_timer(120))

        in_3_min_action = self.menu.addAction("In 00:03:00")
        in_3_min_action.triggered.connect(lambda: PyAlarm.init_timer(180))

        in_5_min_action = self.menu.addAction("In 00:05:00")
        in_5_min_action.triggered.connect(lambda: PyAlarm.init_timer(300))

        in_7_min_action = self.menu.addAction("In 00:07:00")
        in_7_min_action.triggered.connect(lambda: PyAlarm.init_timer(420))

        in_10_min_action = self.menu.addAction("In 00:10:00")
        in_10_min_action.triggered.connect(lambda: PyAlarm.init_timer(600))

        in_15_min_action = self.menu.addAction("In 00:15:00")
        in_15_min_action.triggered.connect(lambda: PyAlarm.init_timer(900))

        self.menu.addSeparator()

        exit_action = self.menu.addAction("Exit")
        exit_action.triggered.connect(lambda: PyAlarm.exit())

        self.setContextMenu(self.menu)


def main():
    app = QtGui.QApplication(sys.argv)
    # style = app.style()
    icon = QtGui.QIcon("Icon.png")
    # QtGui.QIcon(style.standardPixmap(QtGui.QStyle.SP_ComputerIcon))
    # QtGui.QIcon.fromTheme("timer")

    trayIcon = SystemTrayIcon(icon)

    trayIcon.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
