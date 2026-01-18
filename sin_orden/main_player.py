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
from sin_orden.read_configs import ReadConfigs


class MainPlayer(WindowFrameless):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.__cnf_MainPlayer()

    def __cnf_MainPlayer(self):
        self.cnf = ReadConfigs()
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
        self.wcontrol.btSkipForward.clicked.connect(self._next)
        self.wcontrol.btSkipBack.clicked.connect(self.previous)
        self.wcontrol.btForward.clicked.connect(self.forward)
        self.wcontrol.btBack.clicked.connect(self.backward)
        self.wcontrol.btVolumen.toggled.connect(self.toggleMuted)
        self.wcontrol.slVolumen.valueChanged.connect(self.setVolume)
        self.setVolume(self.cnf.get('volume-init'), move_sld=True)

        self.wplaylist.btBajar.clicked.connect(self._next)
        self.wplaylist.btSubir.clicked.connect(self.previous)
        self.wplaylist.btPrimero.clicked.connect(self.wplaylist.select_first_item)
        self.wplaylist.btUltimo.clicked.connect(self.wplaylist.select_last_item)
        self.wplaylist.btOrdenar.clicked.connect(self.toggle_order_items)
        self.wplaylist.btAgregar.clicked.connect(self.showDialogFiles)
        self.wplaylist.btEliminar.clicked.connect(self.wplaylist.delete_item)
        self.wplaylist.lnBuscar.textChanged.connect(self.wplaylist.model.filter_text)

        self.wplayer.durationChanged.connect(self._duration_changed)
        self.wplayer.positionChanged.connect(self._positionChanged)

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

    def _next(self):
        self.wplaylist.selection_step_down()
        self._play_select_item()

    def previous(self):
        self.wplaylist.selection_step_up()
        self._play_select_item()

    def playlist_item_selected(self, index=None):
        """doble click reproduce el archivo seleccionado"""
        path = self.wplaylist.get_path_from_index(index)
        self.winfo.file('FILE: ', path)
        if path:
            self.wplayer.setMedia(file=path)
            self.play()

    def _play_select_item(self):
        media = self.wplayer.currentMedia()
        index = self.wplaylist.current_index()
        select_media = self.wplaylist.get_path_from_index(index)
        self.winfo.msg(f'playlist index: {index} | {select_media}')

        if (self.wplayer.is_playing() or self.wplayer.is_paused())\
            and media == select_media:
            self.winfo.config('play selected [limit]: ', 'mismo archivo, limite alcanzado')
            return
        else:
            path = self.wplaylist.get_path_from_index(index)
            self.winfo.file('FILE: ', path)
            if path:
                self.wplayer.setMedia(file=path)
                self.play()


    def forward(self):
        self.wplayer.forward()

    def backward(self):
        self.wplayer.backward()

    def toggleMuted(self, muted:bool):
        muted = not muted
        value = 0
        if muted:self.wplayer.VOL = self.wplayer.getVolume()
        else:value = self.wplayer.VOL

        self.winfo.config('MUTED: ', f'{muted} ({value})')
        self.wcontrol.slVolumen.setValue(value)
        self.wplayer.setMuted(muted)

    def setVolume(self, volume:int, move_sld:bool=False):
        self.wplayer.setVolume(volume)
        if move_sld:
            self.wplayer.VOL = volume
            self.wcontrol.slVolumen.setValue(volume)
        
    def _duration_changed(self, msec:int):
        self.wcontrol.slTiempo.setRange(0, msec)
        duration_timestamp = self.wplayer.msecToTs(msec)
        self.winfo.config('duration: ', duration_timestamp)

    def _positionChanged(self, pos:int):
        def cut(ts:str) -> str:
            return ts.split('.')[0]
        self.wcontrol.slTiempo.setValue(pos)
        duration = self.wplayer.duration()
        duration_timestamp = self.wplayer.msecToTs(duration)
        current_timestamp = self.wplayer.msecToTs(pos)
        time = f'{cut(current_timestamp)} / {cut(duration_timestamp)}'
        self.wcontrol.lbTiempo.setText(time)

    def toggle_order_items(self):
        name = self.wplaylist.current_item_text()
        self.wplaylist.toggle_order_items()
        self.wplaylist.select_match(name)

    def toggleOnTop(self, onTop:bool):
        """sobre otras ventanas (alternar)"""
        self.winfo.error('deshabilitado', 'causa que el video no se muestre')
    
