from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from rsc.widgets.widget_window.ui_main_window import Ui_MainWindow
from rsc.widgets.widget_body import WidgetBody
from rsc.widgets.widget_playlist import WidgetPlaylist
from rsc.widgets.widget_control import WidgetControl


class WidgetWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.setupUi(self)
        self.__cnf_WidgetWindow()

    def __cnf_WidgetWindow(self):
        self.setWindowTitle('WidgetWindow')
        self.__add_wg_body()
        self.__add_wg_playlist()
        self.__add_wg_control()

    def __add_wg_body(self):
        self.w_body = WidgetBody()
        self.vly_content.addWidget(self.w_body)

    def __add_wg_playlist(self):
        self.w_playlist = WidgetPlaylist()
        self.w_body.vly_playlist.addWidget(self.w_playlist)

    def __add_wg_control(self):
        self.w_control = WidgetControl()
        self.vly_content.addWidget(self.w_control)