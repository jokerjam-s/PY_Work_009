import sys
from PyQt6 import QtGui, QtCore, uic, QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        uic.load_ui('zero_cross.ui', self)

def main():
    app = QtWidgets.QApplication([])
    main_window = MainWindow()
    main_window.show()

    app.quit()


if __name__ == '__main__':
    main()


