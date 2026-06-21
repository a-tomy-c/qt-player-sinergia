from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from rsc.widgets.widget_control.ui_widget_control import Ui_WidgetControl


class WidgetControl(QWidget, Ui_WidgetControl):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.setupUi(self)
        self.__cnf_WidgetControl()

    def __cnf_WidgetControl(self):
        ...
        # self.__fix_ui()
        # self.setWindowTitle('WidgetControl')
        # self.resize(450, 180)

    # def __fix_ui(self):
    #     self.fr_btns.setMaximumHeight(36)
    #     self.fr_btns.setStyleSheet('background-color: blue;')
