# sinergia/views/ui/folder_browser_dialog.py
import os
from PySide6.QtCore import QDir, QModelIndex, Qt
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QSplitter, QTreeView, QListView,
    QPushButton, QFileSystemModel, QAbstractItemView
)

class FolderBrowserDialog(QDialog):
    def __init__(self, parent=None, start_path="D:/Música"):
        super().__init__(parent)
        self.setWindowTitle("Seleccionar carpeta(s) multimedia")
        self.resize(900, 560)
        self.setStyleSheet("QTreeView, QListView { background-color: white; }")

        # Modelo árbol (izquierda)
        self.tree_model = QFileSystemModel()
        self.tree_model.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot)
        self.tree_model.setRootPath(start_path)

        # Modelo lista (derecha)
        self.list_model = QFileSystemModel()
        self.list_model.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot)
        self.list_model.setRootPath(start_path)

        # Árbol izquierdo
        self.tree = QTreeView()
        self.tree.setModel(self.tree_model)
        self.tree.setRootIndex(self.tree_model.index(start_path))
        self.tree.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tree.setColumnHidden(1, True)
        self.tree.setColumnHidden(2, True)
        self.tree.setColumnHidden(3, True)

        # Lista derecha
        self.list = QListView()
        self.list.setModel(self.list_model)
        self.list.setRootIndex(self.list_model.index(start_path))
        self.list.setSelectionMode(QAbstractItemView.ExtendedSelection)

        # Sincronizar lista al seleccionar en árbol
        self.tree.selectionModel().selectionChanged.connect(self._sync_list_root)

        # Splitter
        splitter = QSplitter(self)
        splitter.addWidget(self.tree)
        splitter.addWidget(self.list)

        # Botones
        buttons = QHBoxLayout()
        btnOk = QPushButton("Abrir")
        btnCancel = QPushButton("Cancelar")
        btnOk.clicked.connect(self.accept)
        btnCancel.clicked.connect(self.reject)
        buttons.addStretch(1)
        buttons.addWidget(btnOk)
        buttons.addWidget(btnCancel)

        # Layout principal
        layout = QVBoxLayout(self)
        layout.addWidget(splitter)
        layout.addLayout(buttons)

    def _sync_list_root(self):
        """Panel derecho muestra subcarpetas de la última carpeta seleccionada en el árbol."""
        indexes = self.tree.selectionModel().selectedRows(0)
        if not indexes:
            return
        last_idx: QModelIndex = indexes[-1]
        path = self.tree_model.filePath(last_idx)
        if os.path.isdir(path):
            self.list.setRootIndex(self.list_model.index(path))

    def selectedFolders(self):
        """Combina selección del árbol y de la lista."""
        folders = set()
        for idx in self.tree.selectionModel().selectedRows(0):
            path = self.tree_model.filePath(idx)
            if os.path.isdir(path):
                folders.add(path)
        for idx in self.list.selectionModel().selectedIndexes():
            path = self.list_model.filePath(idx)
            if os.path.isdir(path):
                folders.add(path)
        return list(folders)