from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
# from rsc.widgets.widget_window.ui_main_window import Ui_MainWindow
# from rsc.widgets.widget_body import WidgetBody
# from rsc.widgets.widget_playlist import WidgetPlaylist
# from rsc.widgets.widget_control import WidgetControl
# from rsc.configuration_loader import configs as cf

from .ui_main_window import Ui_MainWindow
from ..widget_body import WidgetBody
from ..widget_playlist import WidgetPlaylist
from ..widget_control import WidgetControl
from ...configuration_loader import configs as cf


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
        self.__apply_configurations()

    def __add_wg_body(self):
        self.w_body = WidgetBody()
        self.vly_content.addWidget(self.w_body)

    def __add_wg_playlist(self):
        self.w_playlist = WidgetPlaylist()
        self.w_body.vly_playlist.addWidget(self.w_playlist)

    def __add_wg_control(self):
        self.w_control = WidgetControl()
        self.vly_content.addWidget(self.w_control)
        # self.vly_content.setStretchFactor(self.w_body, 20)
        self.w_control.setMaximumHeight(54)


    def __apply_configurations(self):
        self.setWindowTitle(cf.get('title', 'Sinergia'))
        width = cf.get('window.width', 600)
        height = cf.get('window.height', 380)
        self.resize(width,height)
        width_playlist = cf.get('w-playlist.width', 200)
        self.w_body.split_body.setSizes([width_playlist, width-width_playlist])
