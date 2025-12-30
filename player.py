# from PySide6.QtWidgets import QApplication, QStyleFactory
# from PySide6.QtCore import QTranslator, QLibraryInfo, QLocale
# from controllers.player_controller import PlayerController

# import sys

# if __name__ == "__main__":
#     app = QApplication([])

#     # --- TRADUCCIÓN AL ESPAÑOL ---
#     translator = QTranslator(app)
#     # Buscamos la ruta de las traducciones oficiales de Qt
#     path = QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath)

#     # Intentamos cargar el archivo de traducción al español
#     # if translator.load(QLocale("es_ES"), "qtbase", "_", path):
#     #     app.installTranslator(translator)

#     try:
#         if translator.load(QLocale("es_ES"), "qtbase", "_", path):
#             app.installTranslator(translator)
#     except Exception as e:
#         print(f"Error cargando traducción: {e}")
#     # ------------------------------
#     sr = PlayerController()
#     app.setStyle('Fusion')
#     sr.show()
#     # Obtener la lista de nombres de estilos disponibles
#     # estilos_disponibles = QStyleFactory.keys()
#     # print(estilos_disponibles)
#     # ['windows11', 'windowsvista', 'Windows', 'Fusion']
#     app.exec()


from PySide6.QtWidgets import QApplication, QStyleFactory
from PySide6.QtCore import QTranslator, QLibraryInfo, QLocale
from controllers.player_controller import PlayerController
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Mejor usar sys.argv

    # Traducción
    translator = QTranslator(app)
    path = QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath)
    if translator.load(QLocale("es_ES"), "qtbase", "_", path):
        app.installTranslator(translator)

    app.setStyle('Fusion')  # Mover antes de mostrar la ventana
    sr = PlayerController()
    sr.show()
    app.exec()