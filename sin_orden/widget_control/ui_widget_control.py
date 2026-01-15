# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_control.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSlider, QVBoxLayout, QWidget)
import icons_rc

class Ui_WidgetControl(object):
    def setupUi(self, WidgetControl):
        if not WidgetControl.objectName():
            WidgetControl.setObjectName(u"WidgetControl")
        WidgetControl.resize(907, 80)
        self.vly_margin = QVBoxLayout(WidgetControl)
        self.vly_margin.setObjectName(u"vly_margin")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.slTiempo = QSlider(WidgetControl)
        self.slTiempo.setObjectName(u"slTiempo")
        self.slTiempo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.slTiempo.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout.addWidget(self.slTiempo)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btSkipBack = QPushButton(WidgetControl)
        self.btSkipBack.setObjectName(u"btSkipBack")
        self.btSkipBack.setMinimumSize(QSize(37, 37))
        self.btSkipBack.setMaximumSize(QSize(37, 16777215))
        self.btSkipBack.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/views/icons/skip-back.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btSkipBack.setIcon(icon)
        self.btSkipBack.setIconSize(QSize(25, 25))
        self.btSkipBack.setFlat(True)

        self.horizontalLayout.addWidget(self.btSkipBack)

        self.btBack = QPushButton(WidgetControl)
        self.btBack.setObjectName(u"btBack")
        self.btBack.setMinimumSize(QSize(37, 37))
        self.btBack.setMaximumSize(QSize(37, 16777215))
        self.btBack.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/views/icons/back.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btBack.setIcon(icon1)
        self.btBack.setIconSize(QSize(25, 25))
        self.btBack.setFlat(True)

        self.horizontalLayout.addWidget(self.btBack)

        self.btPlay = QPushButton(WidgetControl)
        self.btPlay.setObjectName(u"btPlay")
        self.btPlay.setMinimumSize(QSize(37, 37))
        self.btPlay.setMaximumSize(QSize(37, 16777215))
        self.btPlay.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/views/icons/play.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btPlay.setIcon(icon2)
        self.btPlay.setIconSize(QSize(25, 25))
        self.btPlay.setCheckable(True)
        self.btPlay.setFlat(True)

        self.horizontalLayout.addWidget(self.btPlay)

        self.btStop = QPushButton(WidgetControl)
        self.btStop.setObjectName(u"btStop")
        self.btStop.setMinimumSize(QSize(37, 37))
        self.btStop.setMaximumSize(QSize(37, 16777215))
        self.btStop.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/views/icons/stop.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btStop.setIcon(icon3)
        self.btStop.setIconSize(QSize(25, 25))
        self.btStop.setFlat(True)

        self.horizontalLayout.addWidget(self.btStop)

        self.btForward = QPushButton(WidgetControl)
        self.btForward.setObjectName(u"btForward")
        self.btForward.setMinimumSize(QSize(37, 37))
        self.btForward.setMaximumSize(QSize(37, 16777215))
        self.btForward.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/views/icons/forward.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btForward.setIcon(icon4)
        self.btForward.setIconSize(QSize(25, 25))
        self.btForward.setFlat(True)

        self.horizontalLayout.addWidget(self.btForward)

        self.btSkipForward = QPushButton(WidgetControl)
        self.btSkipForward.setObjectName(u"btSkipForward")
        self.btSkipForward.setMinimumSize(QSize(37, 37))
        self.btSkipForward.setMaximumSize(QSize(37, 16777215))
        self.btSkipForward.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/views/icons/skip-forward.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btSkipForward.setIcon(icon5)
        self.btSkipForward.setIconSize(QSize(25, 25))
        self.btSkipForward.setFlat(True)

        self.horizontalLayout.addWidget(self.btSkipForward)

        self.btArchivo = QPushButton(WidgetControl)
        self.btArchivo.setObjectName(u"btArchivo")
        self.btArchivo.setMinimumSize(QSize(37, 37))
        self.btArchivo.setMaximumSize(QSize(37, 16777215))
        self.btArchivo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/views/icons/file-add.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btArchivo.setIcon(icon6)
        self.btArchivo.setIconSize(QSize(25, 25))
        self.btArchivo.setFlat(True)

        self.horizontalLayout.addWidget(self.btArchivo)

        self.btCarpeta = QPushButton(WidgetControl)
        self.btCarpeta.setObjectName(u"btCarpeta")
        self.btCarpeta.setMinimumSize(QSize(37, 37))
        self.btCarpeta.setMaximumSize(QSize(37, 16777215))
        self.btCarpeta.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/views/icons/add-folder.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btCarpeta.setIcon(icon7)
        self.btCarpeta.setIconSize(QSize(25, 25))
        self.btCarpeta.setFlat(True)

        self.horizontalLayout.addWidget(self.btCarpeta)

        self.btShuffle = QPushButton(WidgetControl)
        self.btShuffle.setObjectName(u"btShuffle")
        self.btShuffle.setMinimumSize(QSize(37, 37))
        self.btShuffle.setMaximumSize(QSize(37, 16777215))
        self.btShuffle.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/views/icons/shuffle-off.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btShuffle.setIcon(icon8)
        self.btShuffle.setIconSize(QSize(25, 25))
        self.btShuffle.setCheckable(False)
        self.btShuffle.setFlat(True)

        self.horizontalLayout.addWidget(self.btShuffle)

        self.btRepetir = QPushButton(WidgetControl)
        self.btRepetir.setObjectName(u"btRepetir")
        self.btRepetir.setMinimumSize(QSize(37, 37))
        self.btRepetir.setMaximumSize(QSize(37, 16777215))
        self.btRepetir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/views/icons/repeat.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btRepetir.setIcon(icon9)
        self.btRepetir.setIconSize(QSize(25, 25))
        self.btRepetir.setFlat(True)

        self.horizontalLayout.addWidget(self.btRepetir)

        self.lbTiempo = QLabel(WidgetControl)
        self.lbTiempo.setObjectName(u"lbTiempo")
        self.lbTiempo.setEnabled(True)
        font = QFont()
        font.setPointSize(16)
        self.lbTiempo.setFont(font)
        self.lbTiempo.setIndent(14)

        self.horizontalLayout.addWidget(self.lbTiempo)

        self.btLista = QPushButton(WidgetControl)
        self.btLista.setObjectName(u"btLista")
        self.btLista.setMinimumSize(QSize(37, 37))
        self.btLista.setMaximumSize(QSize(37, 16777215))
        self.btLista.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/views/icons/box-list.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btLista.setIcon(icon10)
        self.btLista.setIconSize(QSize(25, 25))
        self.btLista.setCheckable(True)
        self.btLista.setChecked(True)
        self.btLista.setFlat(True)

        self.horizontalLayout.addWidget(self.btLista)

        self.btPanel = QPushButton(WidgetControl)
        self.btPanel.setObjectName(u"btPanel")
        self.btPanel.setMinimumSize(QSize(37, 37))
        self.btPanel.setMaximumSize(QSize(37, 16777215))
        self.btPanel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/views/icons/setting.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btPanel.setIcon(icon11)
        self.btPanel.setIconSize(QSize(25, 25))
        self.btPanel.setFlat(True)

        self.horizontalLayout.addWidget(self.btPanel)

        self.btVolumen = QPushButton(WidgetControl)
        self.btVolumen.setObjectName(u"btVolumen")
        self.btVolumen.setMinimumSize(QSize(37, 37))
        self.btVolumen.setMaximumSize(QSize(37, 16777215))
        self.btVolumen.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/views/icons/volume-medium.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btVolumen.setIcon(icon12)
        self.btVolumen.setIconSize(QSize(25, 25))
        self.btVolumen.setCheckable(True)
        self.btVolumen.setChecked(True)
        self.btVolumen.setFlat(True)

        self.horizontalLayout.addWidget(self.btVolumen)

        self.slVolumen = QSlider(WidgetControl)
        self.slVolumen.setObjectName(u"slVolumen")
        self.slVolumen.setMinimumSize(QSize(120, 0))
        self.slVolumen.setMaximumSize(QSize(120, 16777215))
        self.slVolumen.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.slVolumen.setMaximum(100)
        self.slVolumen.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout.addWidget(self.slVolumen)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.vly_margin.addLayout(self.verticalLayout)


        self.retranslateUi(WidgetControl)

        QMetaObject.connectSlotsByName(WidgetControl)
    # setupUi

    def retranslateUi(self, WidgetControl):
        WidgetControl.setWindowTitle(QCoreApplication.translate("WidgetControl", u"Form", None))
#if QT_CONFIG(tooltip)
        self.btSkipBack.setToolTip(QCoreApplication.translate("WidgetControl", u"Regresar canci\u00f3n anterior", None))
#endif // QT_CONFIG(tooltip)
        self.btSkipBack.setText("")
#if QT_CONFIG(tooltip)
        self.btBack.setToolTip(QCoreApplication.translate("WidgetControl", u"Regresar sobre misma canci\u00f3n (5,10) segundos", None))
#endif // QT_CONFIG(tooltip)
        self.btBack.setText("")
#if QT_CONFIG(tooltip)
        self.btPlay.setToolTip(QCoreApplication.translate("WidgetControl", u"Reproducir canci\u00f3n", None))
#endif // QT_CONFIG(tooltip)
        self.btPlay.setText("")
#if QT_CONFIG(tooltip)
        self.btStop.setToolTip(QCoreApplication.translate("WidgetControl", u"Detener canci\u00f3n", None))
#endif // QT_CONFIG(tooltip)
        self.btStop.setText("")
#if QT_CONFIG(tooltip)
        self.btForward.setToolTip(QCoreApplication.translate("WidgetControl", u"Continuar sobre misma canci\u00f3n (5,10) segundos", None))
#endif // QT_CONFIG(tooltip)
        self.btForward.setText("")
#if QT_CONFIG(tooltip)
        self.btSkipForward.setToolTip(QCoreApplication.translate("WidgetControl", u"Continuar canci\u00f3n siguiente", None))
#endif // QT_CONFIG(tooltip)
        self.btSkipForward.setText("")
#if QT_CONFIG(tooltip)
        self.btArchivo.setToolTip(QCoreApplication.translate("WidgetControl", u"Agregar Archivo(s)", None))
#endif // QT_CONFIG(tooltip)
        self.btArchivo.setText("")
#if QT_CONFIG(tooltip)
        self.btCarpeta.setToolTip(QCoreApplication.translate("WidgetControl", u"Agregar Carpeta(s)", None))
#endif // QT_CONFIG(tooltip)
        self.btCarpeta.setText("")
#if QT_CONFIG(tooltip)
        self.btShuffle.setToolTip(QCoreApplication.translate("WidgetControl", u"Reproducir aleatoriamente", None))
#endif // QT_CONFIG(tooltip)
        self.btShuffle.setText("")
#if QT_CONFIG(tooltip)
        self.btRepetir.setToolTip(QCoreApplication.translate("WidgetControl", u"Repetir una canci\u00f3n o la lista completa", None))
#endif // QT_CONFIG(tooltip)
        self.btRepetir.setText("")
        self.lbTiempo.setText(QCoreApplication.translate("WidgetControl", u"00:00:00/00:00:00", None))
#if QT_CONFIG(tooltip)
        self.btLista.setToolTip(QCoreApplication.translate("WidgetControl", u"Abrir, cerrar lista", None))
#endif // QT_CONFIG(tooltip)
        self.btLista.setText("")
#if QT_CONFIG(tooltip)
        self.btPanel.setToolTip(QCoreApplication.translate("WidgetControl", u"Abrir panel", None))
#endif // QT_CONFIG(tooltip)
        self.btPanel.setText("")
#if QT_CONFIG(tooltip)
        self.btVolumen.setToolTip(QCoreApplication.translate("WidgetControl", u"Si das clic, enciendes o apagas el volumen", None))
#endif // QT_CONFIG(tooltip)
        self.btVolumen.setText("")
    # retranslateUi

