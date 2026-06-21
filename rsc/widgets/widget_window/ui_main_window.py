# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import rsc.icons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(951, 644)
        font = QFont()
        font.setFamilies([u"Hack"])
        font.setPointSize(14)
        font.setItalic(True)
        MainWindow.setFont(font)
        self.widgetCentral = QWidget(MainWindow)
        self.widgetCentral.setObjectName(u"widgetCentral")
        self.grid_main = QGridLayout(self.widgetCentral)
        self.grid_main.setSpacing(4)
        self.grid_main.setObjectName(u"grid_main")
        self.grid_main.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.grid_main.setContentsMargins(4, 4, 4, 4)
        self.fr_content = QFrame(self.widgetCentral)
        self.fr_content.setObjectName(u"fr_content")
        self.fr_content.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_content.setFrameShadow(QFrame.Shadow.Plain)
        self.vly_fr_content = QVBoxLayout(self.fr_content)
        self.vly_fr_content.setSpacing(0)
        self.vly_fr_content.setObjectName(u"vly_fr_content")
        self.vly_fr_content.setContentsMargins(0, 0, 0, 0)
        self.vly_content = QVBoxLayout()
        self.vly_content.setSpacing(0)
        self.vly_content.setObjectName(u"vly_content")

        self.vly_fr_content.addLayout(self.vly_content)


        self.grid_main.addWidget(self.fr_content, 1, 0, 1, 1)

        self.widget_bar = QWidget(self.widgetCentral)
        self.widget_bar.setObjectName(u"widget_bar")
        self.widget_bar.setMinimumSize(QSize(0, 32))
        self.widget_bar.setMaximumSize(QSize(16777215, 32))
        self.widget_bar.setStyleSheet(u"")
        self.gridBarra = QGridLayout(self.widget_bar)
        self.gridBarra.setObjectName(u"gridBarra")
        self.gridBarra.setHorizontalSpacing(4)
        self.gridBarra.setVerticalSpacing(0)
        self.gridBarra.setContentsMargins(0, 0, 0, 0)
        self.btn_title = QPushButton(self.widget_bar)
        self.btn_title.setObjectName(u"btn_title")
        self.btn_title.setMaximumSize(QSize(90, 16777215))

        self.gridBarra.addWidget(self.btn_title, 0, 0, 1, 1)

        self.lb_text = QLabel(self.widget_bar)
        self.lb_text.setObjectName(u"lb_text")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_text.sizePolicy().hasHeightForWidth())
        self.lb_text.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Hack"])
        font1.setPointSize(12)
        font1.setItalic(False)
        self.lb_text.setFont(font1)
        self.lb_text.setMargin(2)
        self.lb_text.setIndent(6)

        self.gridBarra.addWidget(self.lb_text, 0, 2, 1, 1)

        self.bt_aux = QPushButton(self.widget_bar)
        self.bt_aux.setObjectName(u"bt_aux")
        self.bt_aux.setMinimumSize(QSize(30, 0))
        self.bt_aux.setMaximumSize(QSize(30, 16777215))
        self.bt_aux.setIconSize(QSize(24, 24))
        self.bt_aux.setCheckable(True)
        self.bt_aux.setFlat(False)

        self.gridBarra.addWidget(self.bt_aux, 0, 1, 1, 1)

        self.lb_suffix = QLabel(self.widget_bar)
        self.lb_suffix.setObjectName(u"lb_suffix")
        self.lb_suffix.setMinimumSize(QSize(50, 0))
        self.lb_suffix.setMaximumSize(QSize(50, 16777215))
        self.lb_suffix.setFont(font1)
        self.lb_suffix.setTextFormat(Qt.TextFormat.RichText)
        self.lb_suffix.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lb_suffix.setWordWrap(False)
        self.lb_suffix.setMargin(2)
        self.lb_suffix.setIndent(2)

        self.gridBarra.addWidget(self.lb_suffix, 0, 3, 1, 1)

        self.fr_btns_window = QFrame(self.widget_bar)
        self.fr_btns_window.setObjectName(u"fr_btns_window")
        self.fr_btns_window.setMaximumSize(QSize(168, 16777215))
        self.fr_btns_window.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_btns_window.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.fr_btns_window)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.hly_btns_window = QHBoxLayout()
        self.hly_btns_window.setSpacing(2)
        self.hly_btns_window.setObjectName(u"hly_btns_window")
        self.btn_pin = QPushButton(self.fr_btns_window)
        self.btn_pin.setObjectName(u"btn_pin")
        self.btn_pin.setMinimumSize(QSize(30, 0))
        self.btn_pin.setMaximumSize(QSize(30, 16777215))
        self.btn_pin.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/prefijoNuevo/assets/icons/pin-on.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_pin.setIcon(icon)
        self.btn_pin.setIconSize(QSize(24, 24))
        self.btn_pin.setCheckable(True)
        self.btn_pin.setFlat(False)

        self.hly_btns_window.addWidget(self.btn_pin)

        self.btn_full = QPushButton(self.fr_btns_window)
        self.btn_full.setObjectName(u"btn_full")
        self.btn_full.setMinimumSize(QSize(40, 0))
        self.btn_full.setMaximumSize(QSize(40, 16777215))
        self.btn_full.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/prefijoNuevo/assets/icons/square.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_full.setIcon(icon1)
        self.btn_full.setIconSize(QSize(24, 24))
        self.btn_full.setCheckable(True)
        self.btn_full.setFlat(False)

        self.hly_btns_window.addWidget(self.btn_full)

        self.btn_min = QPushButton(self.fr_btns_window)
        self.btn_min.setObjectName(u"btn_min")
        self.btn_min.setMinimumSize(QSize(30, 0))
        self.btn_min.setMaximumSize(QSize(30, 16777215))
        self.btn_min.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/prefijoNuevo/assets/icons/minimize.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_min.setIcon(icon2)
        self.btn_min.setIconSize(QSize(24, 24))
        self.btn_min.setCheckable(True)
        self.btn_min.setFlat(False)

        self.hly_btns_window.addWidget(self.btn_min)

        self.btn_max = QPushButton(self.fr_btns_window)
        self.btn_max.setObjectName(u"btn_max")
        self.btn_max.setMinimumSize(QSize(30, 0))
        self.btn_max.setMaximumSize(QSize(30, 16777215))
        self.btn_max.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/prefijoNuevo/assets/icons/maximize.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_max.setIcon(icon3)
        self.btn_max.setIconSize(QSize(24, 24))
        self.btn_max.setCheckable(True)
        self.btn_max.setFlat(False)

        self.hly_btns_window.addWidget(self.btn_max)

        self.btn_close = QPushButton(self.fr_btns_window)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(30, 0))
        self.btn_close.setMaximumSize(QSize(30, 16777215))
        self.btn_close.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/prefijoNuevo/assets/icons/close.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_close.setIcon(icon4)
        self.btn_close.setIconSize(QSize(24, 24))
        self.btn_close.setFlat(False)

        self.hly_btns_window.addWidget(self.btn_close)


        self.horizontalLayout_2.addLayout(self.hly_btns_window)


        self.gridBarra.addWidget(self.fr_btns_window, 0, 4, 1, 1)

        self.lb_suffix.raise_()
        self.lb_text.raise_()
        self.bt_aux.raise_()
        self.btn_title.raise_()
        self.fr_btns_window.raise_()

        self.grid_main.addWidget(self.widget_bar, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.widgetCentral)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_title.setText(QCoreApplication.translate("MainWindow", u"Sinergia", None))
        self.lb_text.setText("")
        self.lb_suffix.setText("")
        self.btn_pin.setText("")
        self.btn_full.setText("")
        self.btn_min.setText("")
        self.btn_max.setText("")
        self.btn_close.setText("")
    # retranslateUi

