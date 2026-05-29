from PySide6 import QtWidgets, QtCore

class Qt_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, /, parent=None):
        super().__init__(parent)

        self.setWindowTitle("ToDoList")
        self.setMinimumSize(300, 600)
        pass
