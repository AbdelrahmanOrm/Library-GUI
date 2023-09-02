from PySide2 import QtWidgets
from ui_guidesign import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)                   # Access to the main window and its widgets

# To run the GUI design interface
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()