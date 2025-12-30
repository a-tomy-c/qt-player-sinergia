    # def _composeCoverWithMeta(self, img: QImage, texto: str, target_size: QSize) -> QPixmap:
    #     # Escalar la portada al tamaño del QLabel
    #     base_pix = QPixmap.fromImage(img)
    #     scaled = base_pix.scaled(target_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)

    #     # Crear un lienzo del mismo tamaño
    #     canvas = QPixmap(scaled.size())
    #     canvas.fill(Qt.black)  # fondo seguro

    #     painter = QPainter(canvas)
    #     painter.setRenderHint(QPainter.Antialiasing, True)
    #     painter.setRenderHint(QPainter.TextAntialiasing, True)

    #     # Dibujar la portada
    #     painter.drawPixmap(0, 0, scaled)

    #     # Dibujar barra semitransparente inferior
    #     bar_height = max(40, scaled.height() // 6)
    #     overlay_rect = QRect(0, scaled.height() - bar_height, scaled.width(), bar_height)
    #     painter.fillRect(overlay_rect, QColor(0, 0, 0, 160))

    #     # Configurar fuente y color del texto
    #     font = QFont()
    #     font.setPointSize(10)
    #     font.setBold(True)
    #     painter.setFont(font)
    #     painter.setPen(QColor(255, 165, 0))  # naranja

    #     # Rectángulo para el texto con margen
    #     margin = 8
    #     text_rect = QRect(
    #         margin,
    #         scaled.height() - bar_height + margin,
    #         scaled.width() - 2 * margin,
    #         bar_height - 2 * margin
    #     )
    #     painter.drawText(text_rect, Qt.AlignLeft | Qt.AlignVCenter | Qt.TextWordWrap, texto)

    #     painter.end()
    #     return canvas


# def _updateCoverWithMeta(self):
#     meta = self.player_service.player.metaData()
#     self.lbCover.hide()
#     self.lbCover.clear()

#     if not meta:
#         return

#     # Usar ThumbnailImage en PySide6
#     img = meta.value(QMediaMetaData.ThumbnailImage)
#     if img and not img.isNull():
#         pix = QPixmap.fromImage(img)
#         # self.lbCover.setPixmap(pix.scaled(
#         #     # self.lbCover.size(),
#         #     self.lbCover.setFixedSize(400, 400),
#         #     Qt.KeepAspectRatio
#         #     # Qt.SmoothTransformation
#         # ))
#         self.lbCover.setPixmap(pix.scaled(
#             self.lbCover.size(),
#             Qt.KeepAspectRatio,
#             Qt.SmoothTransformation
#         ))
#         self.lbCover.show()

# def _updateLogoWithMeta(self, file_path: str = None):
#     print("⏺️ _updateLogoWithMeta llamado")
#     meta = self.player_service.player.metaData()

#     title = meta.stringValue(QMediaMetaData.Title) if meta else ""
#     artist = meta.stringValue(QMediaMetaData.ContributingArtist) if meta else ""
#     album = meta.stringValue(QMediaMetaData.AlbumTitle) if meta else ""

#     print(f"🎵 Metadatos: title={title}, artist={artist}, album={album}")

#     # Construir texto
#     texto = ""
#     if title:
#         texto += f"{title}\n"
#     if artist:
#         texto += f"{artist}\n"
#     if album:
#         texto += f"{album}"

#     # Fallback: nombre del archivo
#     if not texto.strip():
#         if file_path:
#             texto = os.path.basename(file_path)
#         else:
#             idx = self.player_service.current_index
#             if 0 <= idx < len(self.player_service.playlist):
#                 texto = os.path.basename(self.player_service.playlist[idx])
#             else:
#                 texto = "Sinergia"

#     self.lbLogo.setText(texto)