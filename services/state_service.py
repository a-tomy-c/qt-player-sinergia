# # services/state_service.py
# from PySide6.QtCore import QSettings

# class StateService:
#     def __init__(self):
#         self.settings = QSettings("Sinergia", "SinergiaPlay")

#     def save(self, key: str, value):
#         self.settings.setValue(key, value)

#     def load(self, key: str, default = None, type = None):
#         if type is not None:
#             return self.settings.value(key, default, type = type)
#         else:
#             return self.settings.value(key, default)

from PySide6.QtCore import QSettings
import logging  # Opcional: para logging avanzado; usa print si prefieres

class StateService:
    def __init__(self):
        self.settings = QSettings("Sinergia", "SinergiaPlay")

    def save(self, key: str, value):
        if not key or key.strip() == "":
            print(f"Error: Clave inválida para guardar: '{key}'")
            return
        try:
            self.settings.setValue(key, value)
            self.settings.sync()  # Fuerza escritura inmediata
        except Exception as e:
            print(f"Error al guardar '{key}': {e}")

    def load(self, key: str, default = None, type = None):
        if not key or key.strip() == "":
            print(f"Error: Clave inválida para cargar: '{key}'")
            return default
        try:
            if type is not None:
                return self.settings.value(key, default, type = type)
            else:
                return self.settings.value(key, default)
        except Exception as e:
            print(f"Error al cargar '{key}': {e}")
            return default
