from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QLineEdit, QWizard
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from services.playlist_widget import PlaylistWidget


class TestPlaylist(PlaylistWidget):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.__cnf_TestPlaylist()

    def __cnf_TestPlaylist(self):
        self.lnBuscar.addAction(QIcon(u':/views/icons/search.svg'), QLineEdit.LeadingPosition)
        self.btBajar.clicked.connect(self.item_move_down)
        self.btSubir.clicked.connect(self.item_move_up)
        self.btEliminar.clicked.connect(self.delete_item)
        self.btOrdenar.clicked.connect(self.toggle_order_items)
        self.lnBuscar.textChanged.connect(self.model.filter_text)
        self.btPrimero.clicked.connect(self.select_first_item)
        self.btUltimo.clicked.connect(self.select_last_item)
        self.__show_data_initial() # si quieres testear coloca rutas a tus archivos en items

    def __show_data_initial(self):
        """test agregando archivos"""
        items = [
            'E:/Videos/musica/Something Else by element a440 b.mp4',
            'E:/Videos/musica/New World Order-(1080p25).mp4',
            'E:/Videos/musica/CARPENTER BRUT - LEATHER TEMPLE b.mp4',
            'E:/Videos/musica/IGORRR - VERY NOISE-b.mp4'
        ]
        for text in items:
            self.append(text)

        
class Ventana(QWidget):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.__cnf_Ventana()

    def __cnf_Ventana(self):
        vly = QVBoxLayout(self)
        vly.setContentsMargins(0,0,0,0)
        
        # TEST PLAYLIST
        wg = TestPlaylist()
        # TEST PLAYLIST
        

        vly.addWidget(wg)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    wg = Ventana()
    wg.show()
    sys.exit(app.exec())
