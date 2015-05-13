# import time
# from threading import Timer
#
#
# def print_time():
#     print "From print_time", time.time()
#
#
# def print_some_times():
#     print time.time()
#     Timer(5, print_time, ()).start()
#     Timer(10, print_time, ()).start()
#     time.sleep(11)  # sleep while time-delay events execute
#     print time.time()
#
#
# #print_some_times()
#
# import sys
# from PyQt4 import QtGui, QtCore
#
# class WithQuitButton(QtGui.QWidget):
#     def __init__(self, parent=None):
#         QtGui.QWidget.__init__(self, parent)
#
#         self.setGeometry(300, 300, 220, 100)
#         self.setWindowTitle(self.trUtf8('Window with button'))
#
#         quit = QtGui.QPushButton(self.trUtf8('Exit!'), self)
#         quit.setGeometry(100, 90, 60, 35)
#
#         main_font = QtGui.QFont(self)
#         main_font.setBold(True)
#         main_font.setPixelSize(42)
#
#
#         label_hours = QtGui.QLabel(self)
#         label_hours.setText("00")
#         label_hours.setGeometry(10, 00, 60, 50)
#         label_hours.setFont(main_font)
#
#         # label_first_delim = QtGui.QLabel(self)
#         # label_first_delim.setText(":")
#         # label_first_delim.setGeometry(40, 10, 10, 10)
#         # label_first_delim.setFont(main_font)
#
#         label_minutes = QtGui.QLabel(self)
#         label_minutes.setText("00")
#         label_minutes.setGeometry(80, 0, 60, 50)
#         label_minutes.setFont(main_font)
#
#         label_seconds = QtGui.QLabel(self)
#         label_seconds.setText("00")
#         label_seconds.setGeometry(150, 0, 60, 50)
#         label_seconds.setFont(main_font)
#
#         #QtCore.SLOT('quit()')
#         #self.connect(quit, QtCore.SIGNAL('clicked()'),
#         #             QtGui.qApp, self.wrapper)
#
#         quit.clicked.connect(self.test)
#
#     def test(self):
#         self.setWindowTitle("TEST!!!!")
#
# # import pyglet
# # song = pyglet.media.load('notify_sound.wav')
# # song.play()
# # pyglet.app.run()
# # pyglet.app.exit()
#
# #notify-send "Hello world!"
#
#
# import pygame
# pygame.init()
# wav = 'notify_sound.wav'
# song = pygame.mixer.Sound("Mallet.ogg")
# clock = pygame.time.Clock()
# #song.play()
# #while True:
# #    clock.tick(60)
# #pygame.quit()
#
#
# app = QtGui.QApplication(sys.argv)
# qb = WithQuitButton()
# qb.show()
# #song.play()
# sys.exit(app.exec_())
#
#
# #time.sleep(1000)