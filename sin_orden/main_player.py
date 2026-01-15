from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLineEdit, QSizePolicy
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QKeySequence, QShortcut
from sin_orden.window_frameless import WindowFrameless
from sin_orden.widget_body import WidgetBody
from sin_orden.widget_info import WidgetInfo
from sin_orden.widget_playlist import  WidgetPlaylist
from sin_orden.widget_player import WidgetPlayer
from sin_orden.widget_control import WidgetControl
from sin_orden.dialog_files import DialogFiles


class MainPlayer(WindowFrameless):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.__cnf_MainPlayer()

    def __cnf_MainPlayer(self):
        self.wbody = WidgetBody()
        self.winfo = WidgetInfo()
        self.winfo.setHeight(5)
        self.vly_content.addWidget(self.wbody)
        self.vly_content.addWidget(self.winfo)

        self.wplaylist = WidgetPlaylist()
        self.wbody.vly_playlist.addWidget(self.wplaylist)
        self.wplayer = WidgetPlayer()
        self.wbody.vly_player.addWidget(self.wplayer.getWidget())
        self._hotkeysPlayer()
        self.wbody.splitter.setSizes([300, 800])
        self.wbody.splitter.setStretchFactor(0, 1)
        self.wbody.splitter.setStretchFactor(1, 3)

        self.wcontrol = WidgetControl()
        self.vly_content.addWidget(self.wcontrol)
        self.vly_content.setStretch(0, 10)
        self.vly_content.setStretch(2, 1)
        self.wcontrol.btArchivo.clicked.connect(self.showDialogFiles)
        self.wcontrol.btCarpeta.clicked.connect(self.showDialogDir)
        self.wcontrol.btLista.toggled.connect(self.togglePlaylist)

        self.wplaylist.ltLista.doubleClicked.connect(self.playlist_item_selected)
        self.wcontrol.btStop.clicked.connect(self.stop)
        self.wcontrol.btPlay.clicked.connect(self.togglePlayback)

    def _hotkeysPlayer(self):
        self.hk_toggle_logo = QShortcut(QKeySequence("t"), self)
        self.hk_toggle_logo.activated.connect(self.wbody.toggleLogo)
        self.hk_toggle_info = QShortcut(QKeySequence("y"), self)
        self.hk_toggle_info.activated.connect(self.toggleInfo)

    def toggleInfo(self):
        b = not self.winfo.isHidden()
        self.winfo.setHidden(b)

    def showInfo(self, show:bool=True):
        self.winfo.setHidden(show)

    def _dialogSelect(self, dir:bool=False):
        dg = DialogFiles()
        try:
            if dir:dg.show_dialog_select_dir()
            else:dg.show_dialog_select_files()

            selected = dg.get_selected_files()
            if selected:
                self.wplaylist.set_paths(selected)
        except Exception as e:
            self.winfo.error('Dialog Files', e)
        finally:
            for msg in dg._state:
                self.winfo.msg_n(msg, num=6, br=True)

    def showDialogFiles(self):
        self._dialogSelect()
    
    def showDialogDir(self):
        self._dialogSelect(dir=True)

    def togglePlaylist(self, b:bool):
        """alternar visibilidad de la playlist"""
        self.wbody.frLista.setHidden(not b)

    def playlist_item_selected(self, index=None):
        """doble click reproduce el archivo seleccionado"""
        path = self.wplaylist.get_path_from_index(index)
        self.winfo.file('FILE: ', path)
        self.wplayer.setMedia(file=path)
        self.play()

    def togglePlayback(self):
        """alterna entre play y pause"""
        self.play() if self.wcontrol.btPlay.isChecked() else self.pause()
        self.winfo.config('[wplayer]', f'playing:{self.wcontrol.btPlay.isChecked()}')

    def play(self):
        self.wplayer.play()
        self.wbody.showLogo(False)
        self.wcontrol.btPlay.setChecked(True)

    def pause(self):
        self.wplayer.pause()
        self.wcontrol.btPlay.setChecked(False)

    def stop(self):
        self.wplayer.stop()
        self.wcontrol.btPlay.setChecked(False)
        self.winfo.config('[wplayer]', 'stopped...')

    def closeEvent(self, event):
        self.stop()
