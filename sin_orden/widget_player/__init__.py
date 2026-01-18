from PySide6.QtWidgets import QLineEdit, QFileDialog, QDialog
from PySide6.QtCore import Qt, QUrl, QSize, QTime
from PySide6.QtMultimedia import QMediaPlayer, QMediaMetaData, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget


class WidgetPlayer(QMediaPlayer):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.__cnf_WidgetPlayer()

    def __cnf_WidgetPlayer(self):
        self.audio_output = QAudioOutput()
        self.video_widget = QVideoWidget()
        self.setVideoOutput(self.video_widget)
        self.setAudioOutput(self.audio_output)
        self._JUMP = 5000
        self.VOL = 0

    def setMedia(self, file:str):
        """asignamos el archivo de video"""
        self.setSource(QUrl.fromLocalFile(file))

    def togglePlayback(self):
        """cambia entre play y pause"""
        self.pause() if self.isPlaying() else self.play()

    def msecToTs(self, msec:int) -> str:
        """convierte milisegundos a timestamp hh:mm:ss.zzz"""
        return QTime(0, 0).addMSecs(msec).toString('hh:mm:ss.zzz')
    
    def _positionMove(self, msec:int):
        """adelanta o retrasa el video en milisegundos"""
        if self.source().isValid():
            new_position:int = self.position() + msec
            duration:int = self.duration()
            if new_position < 0:
                new_position = 0
            elif new_position > duration:
                new_position = duration
            self.setPosition(new_position)

    def backward(self):
        """retrocede el video en milisegundos"""
        self._positionMove(-self._JUMP)

    def forward(self):
        """adelanta el video en milisegundos"""
        self._positionMove(self._JUMP)

    def setVolume(self, value:int, mod:int=0):
        """asigna volumen, mod:modificador"""
        self.audio_output.setVolume((value+mod)/100)

    def getVolume(self) -> int:
        """retorna el valor actual del volumen"""
        return int(self.audio_output.volume()*100)
    
    def getWidget(self) -> QVideoWidget:
        """retorna el widget para agregar a la ui"""
        return self.video_widget
    
    def setMuted(self, muted:bool=True):
        self.audio_output.setMuted(muted)
        
    def currentMedia(self) -> str:
        """retorna la ruta del archivo actual"""
        source = self.source()
        return source.toLocalFile() if source.isValid() else ''

    def get_state(self) -> str:
        match self.playbackState():
            case QMediaPlayer.PlaybackState.StoppedState:
                return "stopped"
            case QMediaPlayer.PlaybackState.PlayingState:
                return "playing"
            case QMediaPlayer.PlaybackState.PausedState:
                return "paused"
            
    def is_playing(self) -> bool:
        return self.isPlaying()
    
    def is_paused(self) -> bool:
        return True if self.get_state() == "paused" else False
    
    def is_stopped(self) -> bool:
        return True if self.get_state() == "stopped" else False
    