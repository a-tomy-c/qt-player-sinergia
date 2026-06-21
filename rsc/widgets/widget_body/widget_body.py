from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
# from rsc.widgets.widget_body.ui_widget_body import Ui_WidgetBody
from .ui_widget_body import Ui_WidgetBody


class WidgetBody(QWidget, Ui_WidgetBody):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.setupUi(self)
        self.__cnf_WidgetBody()

    def __cnf_WidgetBody(self):
        ...
        # self.setWindowTitle('WidgetBody')
        

