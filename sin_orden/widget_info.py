from PySide6.QtWidgets import QApplication, QTextEdit


class WidgetInfo(QTextEdit):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.__cnf_WidgetInfo()

    def __cnf_WidgetInfo(self):
        self.bg = "#0E0303"
        self.setStyleSheet(f'background-color:{self.bg};')
        self.green = "#a5ec6b"
        self.yellow = '#ffdf45'
        self.red = "#f8633e"
        self.skyblue = "#93d0d1"
        self.gray = '#b7b29d'
        self.gray1 = "#888266"
        self.white = '#ffffff'

        scroll_v = self.verticalScrollBar()
        scroll_v.rangeChanged.connect(lambda min,max:scroll_v.setValue(max))

    def _setText(self, text:str, fg:str='white', br=False, bold=False):
        if bold:
            text = f'<b>{text}</b>'
        br = '<br>' if br else ''
        self.insertHtml(f'<span style=color:{fg};>{text}</span>{br}')

    def msg(self, text:str, fg:str='#b7b29d', br=True, bold=False):
        """insertar texto """
        self._setText(text, fg, br, bold)

    def msg_n(self, text:str, num=5, **kw):
        """insertar texto por numero del 1 al 7
            1:green,
            2:yellow,
            3:red,
            4:skyblue,
            5:gray,
            6:gray1,
            7:white
        """
        case = {
            1: self.green,
            2: self.yellow,
            3: self.red,
            4: self.skyblue,
            5: self.gray,
            6: self.gray1,
            7: self.white
        }
        fg = case.get(num, self.gray)
        self.msg(text, fg, **kw)

    def error(self, title:str, text:str):
        self.msg(f'{title} ', fg=self.red, br=False, bold=True)
        self.msg(text, fg=self.white)

    def file(self, title:str, text:str):
        self.msg(f'{title} ', fg=self.gray1, br=False, bold=True)
        self.msg(text, fg=self.yellow, bold=True)

    def info(self, title:str, text:str):
        self.msg(f'{title} ', fg=self.skyblue, br=False, bold=True)
        self.msg(text, fg=self.white)

    def positive(self, title:str, text:str):
        self.msg(f'{title} ', fg=self.green, br=False, bold=True)
        self.msg(text, fg=self.gray)

    def config(self, title:str, text:str, bold_title=True, bold_text=False):
        self.msg(f'{title} ', fg=self.gray1, br=False, bold=bold_title)
        self.msg(text, fg=self.gray, bold=bold_text)

    def setHeight(self, h=6):
        self.setFixedHeight(h * 24)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mv = WidgetInfo()
    mv.resize(800, 220)

    mv.error('player', 'archivo de video no encontrado.')
    mv.file('folder', 'tiene 7 elementos.')
    mv.info('metadata', 'no se encontro datos')
    mv.msg('se cargo la configuracion de la playlist')
    mv.positive('playlist guardada', 'en mi folder-1')
    mv.msg_n("archivo incompatible", num=3, bold=True)
    mv.config('variable HISTORIA', 'tiene el valor de False')

    mv.show()
    sys.exit(app.exec())
    

