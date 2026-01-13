from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from sin_orden.widget_control.ui_widget_control import Ui_WidgetControl


class WidgetControl(QWidget, Ui_WidgetControl):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.setupUi(self)
        self.__cnf_WidgetControl()

    def __cnf_WidgetControl(self):
        ...

