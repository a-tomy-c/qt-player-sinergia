# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_body.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QSplitter, QStackedWidget, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_WidgetBody(object):
    def setupUi(self, WidgetBody):
        if not WidgetBody.objectName():
            WidgetBody.setObjectName(u"WidgetBody")
        WidgetBody.resize(720, 404)
        self.vly_margin = QVBoxLayout(WidgetBody)
        self.vly_margin.setSpacing(0)
        self.vly_margin.setObjectName(u"vly_margin")
        self.vly_margin.setContentsMargins(0, 0, 0, 0)
        self.split_body = QSplitter(WidgetBody)
        self.split_body.setObjectName(u"split_body")
        self.split_body.setOrientation(Qt.Orientation.Horizontal)
        self.split_body.setHandleWidth(2)
        self.fr_playlist = QFrame(self.split_body)
        self.fr_playlist.setObjectName(u"fr_playlist")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fr_playlist.sizePolicy().hasHeightForWidth())
        self.fr_playlist.setSizePolicy(sizePolicy)
        self.fr_playlist.setMinimumSize(QSize(250, 0))
        self.fr_playlist.setMaximumSize(QSize(16777215, 16777215))
        self.fr_playlist.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_playlist.setFrameShadow(QFrame.Shadow.Plain)
        self.vly_margin_playlist = QVBoxLayout(self.fr_playlist)
        self.vly_margin_playlist.setSpacing(0)
        self.vly_margin_playlist.setObjectName(u"vly_margin_playlist")
        self.vly_margin_playlist.setContentsMargins(0, 0, 0, 0)
        self.vly_playlist = QVBoxLayout()
        self.vly_playlist.setSpacing(0)
        self.vly_playlist.setObjectName(u"vly_playlist")

        self.vly_margin_playlist.addLayout(self.vly_playlist)

        self.split_body.addWidget(self.fr_playlist)
        self.fr_player = QFrame(self.split_body)
        self.fr_player.setObjectName(u"fr_player")
        sizePolicy.setHeightForWidth(self.fr_player.sizePolicy().hasHeightForWidth())
        self.fr_player.setSizePolicy(sizePolicy)
        self.fr_player.setMinimumSize(QSize(0, 0))
        self.fr_player.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_player.setFrameShadow(QFrame.Shadow.Plain)
        self.hly_fr_player = QHBoxLayout(self.fr_player)
        self.hly_fr_player.setSpacing(4)
        self.hly_fr_player.setObjectName(u"hly_fr_player")
        self.hly_fr_player.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.sw_player = QStackedWidget(self.fr_player)
        self.sw_player.setObjectName(u"sw_player")
        self.page_logo = QWidget()
        self.page_logo.setObjectName(u"page_logo")
        self.vly_logo = QVBoxLayout(self.page_logo)
        self.vly_logo.setSpacing(0)
        self.vly_logo.setObjectName(u"vly_logo")
        self.vly_logo.setContentsMargins(0, 0, 0, 0)
        self.lb_logo = QLabel(self.page_logo)
        self.lb_logo.setObjectName(u"lb_logo")
        self.lb_logo.setMinimumSize(QSize(0, 0))
        self.lb_logo.setMaximumSize(QSize(16777215, 16777215))
        self.lb_logo.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"Hack"])
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        self.lb_logo.setFont(font)
        self.lb_logo.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lb_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lb_logo.setWordWrap(True)
        self.lb_logo.setMargin(7)

        self.vly_logo.addWidget(self.lb_logo)

        self.sw_player.addWidget(self.page_logo)
        self.page_player = QWidget()
        self.page_player.setObjectName(u"page_player")
        self.verticalLayout_4 = QVBoxLayout(self.page_player)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.vly_player = QVBoxLayout()
        self.vly_player.setSpacing(0)
        self.vly_player.setObjectName(u"vly_player")

        self.verticalLayout_4.addLayout(self.vly_player)

        self.sw_player.addWidget(self.page_player)

        self.verticalLayout.addWidget(self.sw_player)

        self.te_meta = QTextEdit(self.fr_player)
        self.te_meta.setObjectName(u"te_meta")
        self.te_meta.setMaximumSize(QSize(16777215, 60))
        self.te_meta.setFrameShape(QFrame.Shape.NoFrame)
        self.te_meta.setFrameShadow(QFrame.Shadow.Plain)
        self.te_meta.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.te_meta.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.te_meta.setReadOnly(True)
        self.te_meta.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.te_meta)


        self.hly_fr_player.addLayout(self.verticalLayout)

        self.split_body.addWidget(self.fr_player)

        self.vly_margin.addWidget(self.split_body)


        self.retranslateUi(WidgetBody)

        QMetaObject.connectSlotsByName(WidgetBody)
    # setupUi

    def retranslateUi(self, WidgetBody):
        WidgetBody.setWindowTitle(QCoreApplication.translate("WidgetBody", u"Form", None))
        self.lb_logo.setText(QCoreApplication.translate("WidgetBody", u"Sinergia ...", None))
    # retranslateUi

