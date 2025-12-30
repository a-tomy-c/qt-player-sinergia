# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'playerUi.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QListView, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QSplitter, QWidget)
import icons_rc

class Ui_Player(object):
    def setupUi(self, Player):
        if not Player.objectName():
            Player.setObjectName(u"Player")
        Player.resize(994, 657)
        self.centralWidget = QWidget(Player)
        self.centralWidget.setObjectName(u"centralWidget")
        self.gridCentral = QGridLayout(self.centralWidget)
        self.gridCentral.setObjectName(u"gridCentral")
        self.frBarra = QFrame(self.centralWidget)
        self.frBarra.setObjectName(u"frBarra")
        self.frBarra.setMinimumSize(QSize(0, 52))
        self.frBarra.setMaximumSize(QSize(16777215, 52))
        self.frBarra.setFrameShape(QFrame.Shape.StyledPanel)
        self.frBarra.setFrameShadow(QFrame.Shadow.Raised)
        self.gridBarra = QGridLayout(self.frBarra)
        self.gridBarra.setObjectName(u"gridBarra")
        self.gridBarra.setHorizontalSpacing(1)
        self.gridBarra.setVerticalSpacing(6)
        self.gridBarra.setContentsMargins(2, 2, 2, 2)
        self.frTitulo = QFrame(self.frBarra)
        self.frTitulo.setObjectName(u"frTitulo")
        self.frTitulo.setMinimumSize(QSize(120, 32))
        self.frTitulo.setMaximumSize(QSize(120, 32))
        self.frTitulo.setFrameShape(QFrame.Shape.NoFrame)
        self.frTitulo.setFrameShadow(QFrame.Shadow.Raised)
        self.gridTitulo = QGridLayout(self.frTitulo)
        self.gridTitulo.setObjectName(u"gridTitulo")
        self.gridTitulo.setContentsMargins(2, 0, 2, 0)
        self.lbTitulo = QLabel(self.frTitulo)
        self.lbTitulo.setObjectName(u"lbTitulo")
        self.lbTitulo.setMinimumSize(QSize(0, 33))
        self.lbTitulo.setTextFormat(Qt.TextFormat.AutoText)
        self.lbTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridTitulo.addWidget(self.lbTitulo, 0, 0, 1, 1)

        self.btMenu = QPushButton(self.frTitulo)
        self.btMenu.setObjectName(u"btMenu")
        self.btMenu.setMinimumSize(QSize(25, 34))
        self.btMenu.setMaximumSize(QSize(25, 34))
        self.btMenu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/right-arrow.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btMenu.setIcon(icon)
        self.btMenu.setIconSize(QSize(10, 32))
        self.btMenu.setFlat(True)

        self.gridTitulo.addWidget(self.btMenu, 0, 1, 1, 1)


        self.gridBarra.addWidget(self.frTitulo, 0, 0, 1, 1)

        self.lbExtension = QLabel(self.frBarra)
        self.lbExtension.setObjectName(u"lbExtension")
        self.lbExtension.setMinimumSize(QSize(40, 32))
        self.lbExtension.setMaximumSize(QSize(40, 32))
        self.lbExtension.setFrameShape(QFrame.Shape.NoFrame)

        self.gridBarra.addWidget(self.lbExtension, 0, 1, 1, 1)

        self.lbDatos = QLabel(self.frBarra)
        self.lbDatos.setObjectName(u"lbDatos")
        self.lbDatos.setMinimumSize(QSize(0, 32))
        self.lbDatos.setMaximumSize(QSize(16777215, 32))
        self.lbDatos.setFrameShape(QFrame.Shape.NoFrame)

        self.gridBarra.addWidget(self.lbDatos, 0, 2, 1, 1)

        self.btPin = QPushButton(self.frBarra)
        self.btPin.setObjectName(u"btPin")
        self.btPin.setMinimumSize(QSize(0, 0))
        self.btPin.setMaximumSize(QSize(36, 16777215))
        self.btPin.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/pin-a.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btPin.setIcon(icon1)
        self.btPin.setIconSize(QSize(20, 26))
        self.btPin.setAutoRepeatInterval(300)

        self.gridBarra.addWidget(self.btPin, 0, 3, 1, 1)

        self.btMin = QPushButton(self.frBarra)
        self.btMin.setObjectName(u"btMin")
        self.btMin.setMinimumSize(QSize(0, 0))
        self.btMin.setMaximumSize(QSize(36, 16777215))
        self.btMin.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/minimize.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btMin.setIcon(icon2)
        self.btMin.setIconSize(QSize(20, 26))

        self.gridBarra.addWidget(self.btMin, 0, 4, 1, 1)

        self.btMax = QPushButton(self.frBarra)
        self.btMax.setObjectName(u"btMax")
        self.btMax.setMinimumSize(QSize(0, 0))
        self.btMax.setMaximumSize(QSize(36, 16777215))
        self.btMax.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/maximize.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btMax.setIcon(icon3)
        self.btMax.setIconSize(QSize(20, 26))

        self.gridBarra.addWidget(self.btMax, 0, 5, 1, 1)

        self.btSquare = QPushButton(self.frBarra)
        self.btSquare.setObjectName(u"btSquare")
        self.btSquare.setMinimumSize(QSize(0, 0))
        self.btSquare.setMaximumSize(QSize(36, 16777215))
        self.btSquare.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/square.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btSquare.setIcon(icon4)
        self.btSquare.setIconSize(QSize(20, 26))

        self.gridBarra.addWidget(self.btSquare, 0, 6, 1, 1)

        self.btClose = QPushButton(self.frBarra)
        self.btClose.setObjectName(u"btClose")
        self.btClose.setMinimumSize(QSize(0, 0))
        self.btClose.setMaximumSize(QSize(36, 16777215))
        self.btClose.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/close.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btClose.setIcon(icon5)
        self.btClose.setIconSize(QSize(20, 26))

        self.gridBarra.addWidget(self.btClose, 0, 7, 1, 1)


        self.gridCentral.addWidget(self.frBarra, 0, 0, 1, 1)

        self.frControles = QFrame(self.centralWidget)
        self.frControles.setObjectName(u"frControles")
        self.frControles.setMinimumSize(QSize(0, 52))
        self.frControles.setMaximumSize(QSize(16777215, 52))
        self.frControles.setFrameShape(QFrame.Shape.StyledPanel)
        self.frControles.setFrameShadow(QFrame.Shadow.Raised)
        self.gridControles = QGridLayout(self.frControles)
        self.gridControles.setObjectName(u"gridControles")
        self.gridControles.setContentsMargins(0, 1, -1, 1)
        self.btBack = QPushButton(self.frControles)
        self.btBack.setObjectName(u"btBack")
        self.btBack.setMinimumSize(QSize(35, 35))
        self.btBack.setMaximumSize(QSize(30, 35))
        self.btBack.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/skip-back.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btBack.setIcon(icon6)
        self.btBack.setIconSize(QSize(20, 30))

        self.gridControles.addWidget(self.btBack, 0, 0, 1, 1)

        self.btPlay = QPushButton(self.frControles)
        self.btPlay.setObjectName(u"btPlay")
        self.btPlay.setMinimumSize(QSize(35, 35))
        self.btPlay.setMaximumSize(QSize(30, 35))
        self.btPlay.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/play.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btPlay.setIcon(icon7)
        self.btPlay.setIconSize(QSize(22, 30))

        self.gridControles.addWidget(self.btPlay, 0, 1, 1, 1)

        self.btStop = QPushButton(self.frControles)
        self.btStop.setObjectName(u"btStop")
        self.btStop.setMinimumSize(QSize(35, 35))
        self.btStop.setMaximumSize(QSize(30, 35))
        self.btStop.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/stop.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btStop.setIcon(icon8)
        self.btStop.setIconSize(QSize(20, 30))

        self.gridControles.addWidget(self.btStop, 0, 2, 1, 1)

        self.btForward = QPushButton(self.frControles)
        self.btForward.setObjectName(u"btForward")
        self.btForward.setMinimumSize(QSize(35, 35))
        self.btForward.setMaximumSize(QSize(30, 35))
        self.btForward.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/skip-forward.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btForward.setIcon(icon9)
        self.btForward.setIconSize(QSize(20, 30))

        self.gridControles.addWidget(self.btForward, 0, 3, 1, 1)

        self.btEject = QPushButton(self.frControles)
        self.btEject.setObjectName(u"btEject")
        self.btEject.setMinimumSize(QSize(35, 35))
        self.btEject.setMaximumSize(QSize(30, 35))
        self.btEject.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/icons/eject.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btEject.setIcon(icon10)
        self.btEject.setIconSize(QSize(20, 30))

        self.gridControles.addWidget(self.btEject, 0, 4, 1, 1)

        self.btShuffle = QPushButton(self.frControles)
        self.btShuffle.setObjectName(u"btShuffle")
        self.btShuffle.setMinimumSize(QSize(35, 35))
        self.btShuffle.setMaximumSize(QSize(30, 35))
        self.btShuffle.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/icons/shuffle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btShuffle.setIcon(icon11)
        self.btShuffle.setIconSize(QSize(20, 30))

        self.gridControles.addWidget(self.btShuffle, 0, 5, 1, 1)

        self.btRepeat = QPushButton(self.frControles)
        self.btRepeat.setObjectName(u"btRepeat")
        self.btRepeat.setMinimumSize(QSize(35, 35))
        self.btRepeat.setMaximumSize(QSize(30, 35))
        self.btRepeat.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/icons/repeat.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btRepeat.setIcon(icon12)
        self.btRepeat.setIconSize(QSize(20, 30))

        self.gridControles.addWidget(self.btRepeat, 0, 6, 1, 1)

        self.lbInfoControls = QLabel(self.frControles)
        self.lbInfoControls.setObjectName(u"lbInfoControls")
        self.lbInfoControls.setMinimumSize(QSize(35, 35))
        self.lbInfoControls.setMaximumSize(QSize(16777215, 35))
        self.lbInfoControls.setIndent(7)

        self.gridControles.addWidget(self.lbInfoControls, 0, 7, 1, 1)

        self.btLista = QPushButton(self.frControles)
        self.btLista.setObjectName(u"btLista")
        self.btLista.setMinimumSize(QSize(35, 35))
        self.btLista.setMaximumSize(QSize(35, 35))
        self.btLista.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u":/icons/menu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btLista.setIcon(icon13)
        self.btLista.setIconSize(QSize(20, 30))

        self.gridControles.addWidget(self.btLista, 0, 8, 1, 1)

        self.btSetting = QPushButton(self.frControles)
        self.btSetting.setObjectName(u"btSetting")
        self.btSetting.setMinimumSize(QSize(35, 35))
        self.btSetting.setMaximumSize(QSize(35, 35))
        self.btSetting.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon14 = QIcon()
        icon14.addFile(u":/icons/setting.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btSetting.setIcon(icon14)
        self.btSetting.setIconSize(QSize(20, 30))

        self.gridControles.addWidget(self.btSetting, 0, 9, 1, 1)

        self.btVolumen = QPushButton(self.frControles)
        self.btVolumen.setObjectName(u"btVolumen")
        self.btVolumen.setMinimumSize(QSize(35, 35))
        self.btVolumen.setMaximumSize(QSize(35, 35))
        self.btVolumen.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon15 = QIcon()
        icon15.addFile(u":/icons/volume-medium.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btVolumen.setIcon(icon15)
        self.btVolumen.setIconSize(QSize(29, 30))
        self.btVolumen.setFlat(True)

        self.gridControles.addWidget(self.btVolumen, 0, 10, 1, 1)

        self.slVolumen = QSlider(self.frControles)
        self.slVolumen.setObjectName(u"slVolumen")
        self.slVolumen.setMinimumSize(QSize(120, 0))
        self.slVolumen.setMaximumSize(QSize(120, 16777215))
        self.slVolumen.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.slVolumen.setOrientation(Qt.Orientation.Horizontal)

        self.gridControles.addWidget(self.slVolumen, 0, 11, 1, 1)


        self.gridCentral.addWidget(self.frControles, 4, 0, 1, 1)

        self.frSliders = QFrame(self.centralWidget)
        self.frSliders.setObjectName(u"frSliders")
        self.frSliders.setMinimumSize(QSize(0, 27))
        self.frSliders.setMaximumSize(QSize(16777215, 27))
        self.frSliders.setFrameShape(QFrame.Shape.StyledPanel)
        self.frSliders.setFrameShadow(QFrame.Shadow.Raised)
        self.gridSliders = QGridLayout(self.frSliders)
        self.gridSliders.setObjectName(u"gridSliders")
        self.gridSliders.setContentsMargins(0, 0, -1, 0)
        self.slVideo = QSlider(self.frSliders)
        self.slVideo.setObjectName(u"slVideo")
        self.slVideo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.slVideo.setOrientation(Qt.Orientation.Horizontal)

        self.gridSliders.addWidget(self.slVideo, 0, 0, 1, 1)


        self.gridCentral.addWidget(self.frSliders, 3, 0, 1, 1)

        self.splitter = QSplitter(self.centralWidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.frLista = QFrame(self.splitter)
        self.frLista.setObjectName(u"frLista")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frLista.sizePolicy().hasHeightForWidth())
        self.frLista.setSizePolicy(sizePolicy)
        self.frLista.setMinimumSize(QSize(300, 0))
        self.frLista.setMaximumSize(QSize(16777215, 16777215))
        self.frLista.setFrameShape(QFrame.Shape.StyledPanel)
        self.frLista.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLista = QGridLayout(self.frLista)
        self.gridLista.setObjectName(u"gridLista")
        self.ltLista = QListView(self.frLista)
        self.ltLista.setObjectName(u"ltLista")
        self.ltLista.setMinimumSize(QSize(0, 0))
        self.ltLista.setMaximumSize(QSize(16777215, 16777215))

        self.gridLista.addWidget(self.ltLista, 0, 0, 1, 7)

        self.lnBuscar = QLineEdit(self.frLista)
        self.lnBuscar.setObjectName(u"lnBuscar")
        self.lnBuscar.setMinimumSize(QSize(0, 30))
        self.lnBuscar.setMaximumSize(QSize(16777215, 30))

        self.gridLista.addWidget(self.lnBuscar, 1, 0, 1, 7)

        self.btPrimero = QPushButton(self.frLista)
        self.btPrimero.setObjectName(u"btPrimero")
        self.btPrimero.setMinimumSize(QSize(30, 30))
        self.btPrimero.setMaximumSize(QSize(30, 30))
        self.btPrimero.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon16 = QIcon()
        icon16.addFile(u":/icons/skip-up.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btPrimero.setIcon(icon16)
        self.btPrimero.setIconSize(QSize(13, 25))

        self.gridLista.addWidget(self.btPrimero, 2, 0, 1, 1)

        self.btSubir = QPushButton(self.frLista)
        self.btSubir.setObjectName(u"btSubir")
        self.btSubir.setMinimumSize(QSize(30, 30))
        self.btSubir.setMaximumSize(QSize(30, 30))
        self.btSubir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon17 = QIcon()
        icon17.addFile(u":/icons/play-up.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btSubir.setIcon(icon17)
        self.btSubir.setIconSize(QSize(13, 25))

        self.gridLista.addWidget(self.btSubir, 2, 1, 1, 1)

        self.btBajar = QPushButton(self.frLista)
        self.btBajar.setObjectName(u"btBajar")
        self.btBajar.setMinimumSize(QSize(30, 30))
        self.btBajar.setMaximumSize(QSize(30, 30))
        self.btBajar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon18 = QIcon()
        icon18.addFile(u":/icons/play-dow.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btBajar.setIcon(icon18)
        self.btBajar.setIconSize(QSize(13, 25))

        self.gridLista.addWidget(self.btBajar, 2, 2, 1, 1)

        self.btUltimo = QPushButton(self.frLista)
        self.btUltimo.setObjectName(u"btUltimo")
        self.btUltimo.setMinimumSize(QSize(30, 30))
        self.btUltimo.setMaximumSize(QSize(30, 30))
        self.btUltimo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btUltimo.setIcon(icon16)
        self.btUltimo.setIconSize(QSize(13, 25))

        self.gridLista.addWidget(self.btUltimo, 2, 3, 1, 1)

        self.btAgregar = QPushButton(self.frLista)
        self.btAgregar.setObjectName(u"btAgregar")
        self.btAgregar.setMinimumSize(QSize(0, 30))
        self.btAgregar.setMaximumSize(QSize(16777215, 30))

        self.gridLista.addWidget(self.btAgregar, 2, 4, 1, 1)

        self.btOrdenar = QPushButton(self.frLista)
        self.btOrdenar.setObjectName(u"btOrdenar")
        self.btOrdenar.setMinimumSize(QSize(0, 30))
        self.btOrdenar.setMaximumSize(QSize(16777215, 30))

        self.gridLista.addWidget(self.btOrdenar, 2, 5, 1, 1)

        self.btEliminar = QPushButton(self.frLista)
        self.btEliminar.setObjectName(u"btEliminar")
        self.btEliminar.setMinimumSize(QSize(0, 30))
        self.btEliminar.setMaximumSize(QSize(16777215, 30))

        self.gridLista.addWidget(self.btEliminar, 2, 6, 1, 1)

        self.splitter.addWidget(self.frLista)
        self.frPlayer = QFrame(self.splitter)
        self.frPlayer.setObjectName(u"frPlayer")
        sizePolicy.setHeightForWidth(self.frPlayer.sizePolicy().hasHeightForWidth())
        self.frPlayer.setSizePolicy(sizePolicy)
        self.frPlayer.setFrameShape(QFrame.Shape.StyledPanel)
        self.frPlayer.setFrameShadow(QFrame.Shadow.Raised)
        self.gridPlayer = QGridLayout(self.frPlayer)
        self.gridPlayer.setObjectName(u"gridPlayer")
        self.gridVideo = QGridLayout()
        self.gridVideo.setObjectName(u"gridVideo")

        self.gridPlayer.addLayout(self.gridVideo, 0, 0, 1, 1)

        self.splitter.addWidget(self.frPlayer)

        self.gridCentral.addWidget(self.splitter, 1, 0, 1, 1)

        Player.setCentralWidget(self.centralWidget)

        self.retranslateUi(Player)

        QMetaObject.connectSlotsByName(Player)
    # setupUi

    def retranslateUi(self, Player):
        Player.setWindowTitle(QCoreApplication.translate("Player", u"MainWindow", None))
        self.lbTitulo.setText(QCoreApplication.translate("Player", u"Sinergia", None))
        self.btMenu.setText("")
        self.lbExtension.setText("")
        self.lbDatos.setText("")
        self.btPin.setText("")
        self.btMin.setText("")
        self.btMax.setText("")
        self.btSquare.setText("")
        self.btClose.setText("")
        self.btBack.setText("")
        self.btPlay.setText("")
        self.btStop.setText("")
        self.btForward.setText("")
        self.btEject.setText("")
        self.btShuffle.setText("")
        self.btRepeat.setText("")
        self.lbInfoControls.setText(QCoreApplication.translate("Player", u"00:00:00/00:00:00", None))
        self.btSetting.setText("")
        self.btVolumen.setText("")
        self.lnBuscar.setPlaceholderText(QCoreApplication.translate("Player", u"Buscar ...", None))
        self.btPrimero.setText("")
        self.btSubir.setText("")
        self.btBajar.setText("")
        self.btUltimo.setText("")
        self.btAgregar.setText(QCoreApplication.translate("Player", u"A\u00f1adir", None))
        self.btOrdenar.setText(QCoreApplication.translate("Player", u"Ordenar", None))
        self.btEliminar.setText(QCoreApplication.translate("Player", u"Eliminar", None))
    # retranslateUi

