# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_body.ui'
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
    QSizePolicy, QSplitter, QStackedWidget, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_WidgetBody(object):
    def setupUi(self, WidgetBody):
        if not WidgetBody.objectName():
            WidgetBody.setObjectName(u"WidgetBody")
        WidgetBody.resize(720, 526)
        self.verticalLayout_3 = QVBoxLayout(WidgetBody)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(WidgetBody)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.frLista = QFrame(self.splitter)
        self.frLista.setObjectName(u"frLista")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frLista.sizePolicy().hasHeightForWidth())
        self.frLista.setSizePolicy(sizePolicy)
        self.frLista.setMinimumSize(QSize(300, 0))
        self.frLista.setMaximumSize(QSize(16777215, 16777215))
        self.frLista.setFrameShape(QFrame.Shape.NoFrame)
        self.frLista.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frLista)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.vly_playlist = QVBoxLayout()
        self.vly_playlist.setObjectName(u"vly_playlist")

        self.verticalLayout_2.addLayout(self.vly_playlist)

        self.splitter.addWidget(self.frLista)
        self.frPlayer = QFrame(self.splitter)
        self.frPlayer.setObjectName(u"frPlayer")
        sizePolicy.setHeightForWidth(self.frPlayer.sizePolicy().hasHeightForWidth())
        self.frPlayer.setSizePolicy(sizePolicy)
        self.frPlayer.setMinimumSize(QSize(0, 0))
        self.frPlayer.setFrameShape(QFrame.Shape.StyledPanel)
        self.frPlayer.setFrameShadow(QFrame.Shadow.Raised)
        self.gridPlayer = QGridLayout(self.frPlayer)
        self.gridPlayer.setObjectName(u"gridPlayer")
        self.gridPlayer.setHorizontalSpacing(6)
        self.gridPlayer.setContentsMargins(0, 0, 0, 0)
        self.teMeta = QTextEdit(self.frPlayer)
        self.teMeta.setObjectName(u"teMeta")
        self.teMeta.setMaximumSize(QSize(16777215, 60))
        self.teMeta.setFrameShape(QFrame.Shape.NoFrame)
        self.teMeta.setFrameShadow(QFrame.Shadow.Plain)
        self.teMeta.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.teMeta.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.teMeta.setReadOnly(True)
        self.teMeta.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridPlayer.addWidget(self.teMeta, 1, 0, 1, 1)

        self.widgetArchivos = QWidget(self.frPlayer)
        self.widgetArchivos.setObjectName(u"widgetArchivos")
        self.widgetArchivos.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.widgetArchivos)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.sw_player = QStackedWidget(self.widgetArchivos)
        self.sw_player.setObjectName(u"sw_player")
        self.page_logo = QWidget()
        self.page_logo.setObjectName(u"page_logo")
        self.vly_logo = QVBoxLayout(self.page_logo)
        self.vly_logo.setSpacing(0)
        self.vly_logo.setObjectName(u"vly_logo")
        self.vly_logo.setContentsMargins(0, 0, 0, 0)
        self.lbLogo = QLabel(self.page_logo)
        self.lbLogo.setObjectName(u"lbLogo")
        self.lbLogo.setMinimumSize(QSize(0, 0))
        self.lbLogo.setMaximumSize(QSize(16777215, 16777215))
        self.lbLogo.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"Hack"])
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        self.lbLogo.setFont(font)
        self.lbLogo.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lbLogo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbLogo.setWordWrap(True)
        self.lbLogo.setMargin(7)

        self.vly_logo.addWidget(self.lbLogo)

        self.sw_player.addWidget(self.page_logo)
        self.page_player = QWidget()
        self.page_player.setObjectName(u"page_player")
        self.verticalLayout_4 = QVBoxLayout(self.page_player)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.vly_player = QVBoxLayout()
        self.vly_player.setObjectName(u"vly_player")

        self.verticalLayout_4.addLayout(self.vly_player)

        self.sw_player.addWidget(self.page_player)

        self.verticalLayout.addWidget(self.sw_player)


        self.gridPlayer.addWidget(self.widgetArchivos, 0, 0, 1, 1)

        self.splitter.addWidget(self.frPlayer)

        self.verticalLayout_3.addWidget(self.splitter)


        self.retranslateUi(WidgetBody)

        QMetaObject.connectSlotsByName(WidgetBody)
    # setupUi

    def retranslateUi(self, WidgetBody):
        WidgetBody.setWindowTitle(QCoreApplication.translate("WidgetBody", u"Form", None))
        self.lbLogo.setText(QCoreApplication.translate("WidgetBody", u"Sinergia ...", None))
    # retranslateUi

