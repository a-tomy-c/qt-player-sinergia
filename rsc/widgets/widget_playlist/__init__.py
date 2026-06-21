from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from rsc.widgets.widget_playlist.ui_widget_playlist import Ui_WidgetPlaylist


class WidgetPlaylist(QWidget, Ui_WidgetPlaylist):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.setupUi(self)
        self.__cnf_WidgetPlaylist()

    def __cnf_WidgetPlaylist(self):
        self.__fix_ui()

    def __fix_ui(self):
        self.fr_1.setHidden(True)

