import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

sys.path.insert(0, str(Path(__file__).parent / "src"))
from rsc.widgets.widget_window import WidgetWindow


class SinergiaPlayer(WidgetWindow):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.__cnf_SinergiaPlayer()

    def __cnf_SinergiaPlayer(self):
        ...

    


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mv = SinergiaPlayer()
    mv.show()
    sys.exit(app.exec())
    
