from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from rsc.widgets.widget_window.ui_main_window import Ui_MainWindow


class WidgetWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.setupUi(self)
        self.__cnf_WidgetWindow()

    def __cnf_WidgetWindow(self):
        self.setWindowTitle('WidgetWindow')
        # self.resize(450, 180)



