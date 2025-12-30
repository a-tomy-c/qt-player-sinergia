# # services/player_service.py
# from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
# from PySide6.QtCore import QUrl, Signal, QObject
# from services.state_service import StateService
# import random

# class PlayerService(QObject):
#     """Service layer for multimedia playback using QMediaPlayer."""
#     currentIndexChanged = Signal(int)

#     def __init__(self):
#         super().__init__() # 🔔 inicializa QObject
#         self.player = QMediaPlayer()
#         self.audio_output = QAudioOutput()
#         self.player.setAudioOutput(self.audio_output)

#         # Volumen inicial razonable (50%)
#         self.audio_output.setVolume(0.5)
#         self.audio_output.setMuted(False)

#         # --- Persistencia centralizada ---
#         self.state_service = StateService()
#         self.repeat_mode = self.state_service.load("repeat_mode", "none")
#         self.shuffle_mode = self.state_service.load("shuffle_mode", False, type = bool)


#         # Lista de archivos gestionada en Python
#         self.playlist = []
#         self.current_index = -1

#         self.player.mediaStatusChanged.connect(self._handleMediaStatus)

#     def set_shuffle_mode(self, enabled: bool):
#         self.shuffle_mode = enabled
#         self.state_service.save("shuffle_mode", enabled)

#     def set_video_output(self, video_widget):
#         self.player.setVideoOutput(video_widget)

#     def _handleMediaStatus(self, status):
#         if status == QMediaPlayer.MediaStatus.EndOfMedia:
#             if self.repeat_mode == "one":
#                 self.play()
#             elif self.repeat_mode == "all":
#                 self.next()

#     # --- Carga y playlist ---
#     def load(self, file_path: str):
#         self.playlist.append(file_path)
#         if self.current_index == -1:
#             self.set_current_index(0)

#     def clear_playlist(self):
#         self.playlist.clear()
#         self.current_index = -1
#         self.stop()


#     def set_current_index(self, index: int):
#         if 0 <= index < len(self.playlist):
#             self.current_index = index
#             file_path = self.playlist[index]
#             self.player.setSource(QUrl.fromLocalFile(file_path))
#             self.currentIndexChanged.emit(self.current_index)   # 🔔 emitir


#     # --- Control de reproducción ---
#     def play(self): self.player.play()
#     def pause(self): self.player.pause()
#     def stop(self): self.player.stop()

#     def next(self):
#         if not self.playlist:
#             return
#         if self.shuffle_mode:
#             self.current_index = random.randint(0, len(self.playlist) - 1)
#         else:
#             self.current_index += 1
#             if self.current_index >= len(self.playlist):
#                 self.current_index = 0
#         self._apply_current_and_play()
#         self.currentIndexChanged.emit(self.current_index)   # 🔔 emitir

#     def previous(self):
#         if not self.playlist:
#             return
#         self.current_index -= 1
#         if self.current_index < 0:
#             self.current_index = len(self.playlist) - 1
#         self._apply_current_and_play()
#         self.currentIndexChanged.emit(self.current_index)   # 🔔 emitir

#     def _apply_current_and_play(self):
#         qurl = self.playlist[self.current_index]
#         self.player.setSource(QUrl.fromLocalFile(qurl))
#         self.play()

#     # --- Audio ---
#     def set_volume(self, value: int):
#         self.audio_output.setVolume(max(0, min(value, 100)) / 100.0)
#         self.state_service.save("volume", value)

#     def mute(self, state: bool = True):
#         self.audio_output.setMuted(state)

#     # --- Estado ---
#     def set_repeat_mode(self, mode: str):
#         self.repeat_mode = mode
#         self.state_service.save("repeat_mode", mode)

#     def is_playing(self) -> bool:
#         return self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState

#     def duration(self) -> int: return self.player.duration()
#     def position(self) -> int: return self.player.position()
#     def seek(self, ms: int): self.player.setPosition(ms)


from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl, Signal, QObject
from PySide6.QtWidgets import QMessageBox

from services.state_service import StateService
import random
import os  # Agregado para validación de archivos

class PlayerService(QObject):
    """Service layer for multimedia playback using QMediaPlayer."""
    currentIndexChanged = Signal(int)

    def __init__(self):
        super().__init__()  # 🔔 inicializa QObject

        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)

        self.player.errorOccurred.connect(self._handlePlayerError)

        # Volumen inicial razonable (50%)
        self.audio_output.setVolume(0.5)
        self.audio_output.setMuted(False)

        # --- Persistencia centralizada ---
        self.state_service = StateService()
        self.repeat_mode = self.state_service.load("repeat_mode", "none")
        self.shuffle_mode = self.state_service.load("shuffle_mode", False, type = bool)

        # Lista de archivos gestionada en Python
        self.playlist = []
        self.current_index = -1

        self.player.mediaStatusChanged.connect(self._handleMediaStatus)
    # **************************************************************************

    
    def _handlePlayerError(self, error, errorString):
        """
        Maneja errores específicos de QMediaPlayer y muestra mensajes al usuario.
        """
        if error == QMediaPlayer.ResourceError:
            QMessageBox.warning(None, "Error de Codec", f"Codec faltante o recurso no disponible: {errorString}.\n\nInstala FFmpeg o codecs compatibles con PySide6/Qt.")
        elif error == QMediaPlayer.FormatError:
            QMessageBox.warning(None, "Error de Formato", f"El formato del archivo no es soportado: {errorString}.\n\nVerifica que el archivo sea válido o conviértelo a un formato compatible (e.g., MP4, AVI).")
        elif error == QMediaPlayer.NetworkError:
            QMessageBox.warning(None, "Error de Red", f"Problema de conexión de red: {errorString}.\n\nVerifica tu conexión a internet si es un stream remoto.")
        elif error == QMediaPlayer.AccessDeniedError:
            QMessageBox.warning(None, "Error de Acceso", f"Acceso denegado al archivo: {errorString}.\n\nAsegúrate de tener permisos para leer el archivo o que no esté en uso.")
        elif error == QMediaPlayer.ServiceMissingError:
            QMessageBox.warning(None, "Error de Servicio", f"Servicio multimedia faltante: {errorString}.\n\nReinstala PySide6 o verifica que Qt Multimedia esté disponible en tu sistema.")
        else:
            # Para errores no específicos o desconocidos
            QMessageBox.warning(None, "Error Desconocido", f"Error al reproducir: {errorString}.\n\nIntenta con otro archivo o verifica la configuración del sistema.")

    def set_shuffle_mode(self, enabled: bool):
        self.shuffle_mode = enabled
        self.state_service.save("shuffle_mode", enabled)

    def set_video_output(self, video_widget):
        print(f"DEBUG: set_video_output llamado con {video_widget}")
        self.player.setVideoOutput(video_widget)

    def _handleMediaStatus(self, status):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            if self.repeat_mode == "one":
                self.play()
            elif self.repeat_mode == "all":
                self.next()

    # --- Carga y playlist ---
    def load(self, file_path: str):
        # --- NUEVA VALIDACIÓN: Verificar si el archivo existe ---
        if not os.path.exists(file_path):
            print(f"Advertencia: Archivo '{file_path}' no encontrado. No se agrega a la playlist.")
            return
        # -------------------------------------------------------
        self.playlist.append(file_path)
        if self.current_index == -1:
            self.set_current_index(0)

    def clear_playlist(self):
        self.playlist.clear()
        self.current_index = -1
        self.stop()

    def set_current_index(self, index: int):
        if 0 <= index < len(self.playlist):
            self.current_index = index
            file_path = self.playlist[index]
            try:
                self.player.setSource(QUrl.fromLocalFile(file_path))
            except Exception as e:
                print(f"Error al cargar archivo '{file_path}': {e}")
                # Opcional: Emitir señal de error o mostrar mensaje
                return  # No emitir currentIndexChanged si falla
            self.currentIndexChanged.emit(self.current_index)

    # --- Control de reproducción ---
    def play(self): self.player.play()
    def pause(self): self.player.pause()
    def stop(self): self.player.stop()

    def next(self):
        if not self.playlist:
            return
        if self.shuffle_mode:
            self.current_index = random.randint(0, len(self.playlist) - 1)
        else:
            self.current_index += 1
            if self.current_index >= len(self.playlist):
                self.current_index = 0
        self._apply_current_and_play()
        # Eliminado: self.currentIndexChanged.emit(self.current_index)  # Evita doble emisión

    def previous(self):
        if not self.playlist:
            return
        self.current_index -= 1
        if self.current_index < 0:
            self.current_index = len(self.playlist) - 1
        self._apply_current_and_play()
        # Eliminado: self.currentIndexChanged.emit(self.current_index)  # Evita doble emisión

    def _apply_current_and_play(self):
        file_path = self.playlist[self.current_index]  # Renombrado de qurl para claridad
        try:
            self.player.setSource(QUrl.fromLocalFile(file_path))
            self.play()
            self.currentIndexChanged.emit(self.current_index)
        except Exception as e:
            print(f"Error al reproducir '{file_path}': {e}")

    # --- Audio ---
    def set_volume(self, value: int):
        self.audio_output.setVolume(max(0, min(value, 100)) / 100.0)
        self.state_service.save("volume", value)

    def mute(self, state: bool = True):
        self.audio_output.setMuted(state)

    # --- Estado ---
    def set_repeat_mode(self, mode: str):
        self.repeat_mode = mode
        self.state_service.save("repeat_mode", mode)

    def is_playing(self) -> bool:
        return self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState

    def duration(self) -> int: return self.player.duration()
    def position(self) -> int: return self.player.position()
    def seek(self, ms: int): self.player.setPosition(ms)