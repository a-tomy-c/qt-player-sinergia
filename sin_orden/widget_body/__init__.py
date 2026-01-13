from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from sin_orden.widget_body.ui_widget_body import Ui_WidgetBody


class WidgetBody(QWidget, Ui_WidgetBody):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.setupUi(self)
        self.__cnf_WidgetBody()

    def __cnf_WidgetBody(self):
        ...
        # self.setWindowTitle('WidgetBody')
        # self.resize(450, 180)

    def showLogo(self, show:bool=True):
        index = 0 if show else 1
        self.sw_player.setCurrentIndex(index)

    def toggleLogo(self):
        index = self.sw_player.currentIndex()
        new_index = 1 if index==0 else 0
        self.sw_player.setCurrentIndex(new_index)

