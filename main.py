import os
import sys
from PyQt4 import QtGui

from threading import Timer


class PyAlarm:
    def __init__(self):
        pass

    timer = None
    qt_system_tray_icon = None

    @staticmethod
    def init_timer(time_in_seconds, qt_system_tray_icon=None):
        PyAlarm.qt_system_tray_icon = qt_system_tray_icon

        PyAlarm._set_active_tray_icon()

        PyAlarm._stop_timer()  # resets previous active timer if exists

        PyAlarm.timer = Timer(time_in_seconds, PyAlarm._timer_expired, ())
        PyAlarm.timer.start()

    @staticmethod
    def _stop_timer():
        if PyAlarm.timer is not None:
            PyAlarm.timer.cancel()

    @staticmethod
    def _set_active_tray_icon():
        PyAlarm.qt_system_tray_icon.setIcon(QtGui.QIcon("Icon_active.png"))

    @staticmethod
    def _timer_expired():
        PyAlarm._reset_tray_icon()
        PyAlarm._gui_notify()
        PyAlarm._play_notify_sound()

    @staticmethod
    def _gui_notify():
        # TODO configuration for notification method, and error handling - OS without notify-send
        os.system("notify-send 'Timer expired.'")

    @staticmethod
    def _play_notify_sound():
        # TODO easier method to play sound
        import pygame
        pygame.init()
        # notify_sound_name = 'notify_sound.wav'
        song = pygame.mixer.Sound("Mallet.ogg")
        song.play()

    @staticmethod
    def _reset_tray_icon():
        if PyAlarm.qt_system_tray_icon:
            PyAlarm.qt_system_tray_icon.setIcon(QtGui.QIcon("Icon.png"))

    @staticmethod
    def exit():
        PyAlarm._stop_timer()
        sys.exit(0)


# TODO gui configuration of time for alarm clock
class SystemTrayIcon(QtGui.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        QtGui.QSystemTrayIcon.__init__(self, icon, parent)
        self.menu = QtGui.QMenu(parent)

        in_10_sec_action = self.menu.addAction("In 00:00:10")
        in_10_sec_action.triggered.connect(lambda: PyAlarm.init_timer(10, self))

        in_half_min_action = self.menu.addAction("In 00:00:30")
        in_half_min_action.triggered.connect(lambda: PyAlarm.init_timer(30, self))

        self.menu.addSeparator()

        # TODO timers presets to be configurable
        in_1_min_action = self.menu.addAction("In 00:01:00")
        in_1_min_action.triggered.connect(lambda: PyAlarm.init_timer(60, self))

        in_2_min_action = self.menu.addAction("In 00:02:00")
        in_2_min_action.triggered.connect(lambda: PyAlarm.init_timer(120, self))

        in_3_min_action = self.menu.addAction("In 00:03:00")
        in_3_min_action.triggered.connect(lambda: PyAlarm.init_timer(180, self))

        in_5_min_action = self.menu.addAction("In 00:05:00")
        in_5_min_action.triggered.connect(lambda: PyAlarm.init_timer(300, self))

        in_7_min_action = self.menu.addAction("In 00:07:00")
        in_7_min_action.triggered.connect(lambda: PyAlarm.init_timer(420, self))

        in_10_min_action = self.menu.addAction("In 00:10:00")
        in_10_min_action.triggered.connect(lambda: PyAlarm.init_timer(600, self))

        in_15_min_action = self.menu.addAction("In 00:15:00")
        in_15_min_action.triggered.connect(lambda: PyAlarm.init_timer(900, self))

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
