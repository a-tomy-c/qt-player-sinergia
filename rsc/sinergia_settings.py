from PySide6.QtCore import QSettings
from typing import Any

class SinergiaSettings:
    def __init__(self):
        self.settings = QSettings('Sinergia', 'SinergiaPlay')

    def save(self, key:str, value:Any):
        if not key or key.strip()=='':
            ...
