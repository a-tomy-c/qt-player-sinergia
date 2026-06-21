# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_playlist.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSplitter, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)
import rsc.icons

class Ui_WidgetPlaylist(object):
    def setupUi(self, WidgetPlaylist):
        if not WidgetPlaylist.objectName():
            WidgetPlaylist.setObjectName(u"WidgetPlaylist")
        WidgetPlaylist.resize(326, 528)
        self.vly_margin = QVBoxLayout(WidgetPlaylist)
        self.vly_margin.setSpacing(4)
        self.vly_margin.setObjectName(u"vly_margin")
        self.vly_margin.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.sw = QStackedWidget(WidgetPlaylist)
        self.sw.setObjectName(u"sw")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.vly_margin_page1 = QVBoxLayout(self.page_1)
        self.vly_margin_page1.setSpacing(0)
        self.vly_margin_page1.setObjectName(u"vly_margin_page1")
        self.vly_margin_page1.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tw = QTableWidget(self.page_1)
        self.tw.setObjectName(u"tw")
        self.tw.setFrameShape(QFrame.Shape.NoFrame)
        self.tw.setFrameShadow(QFrame.Shadow.Plain)
        self.tw.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tw.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.tw)

        self.le_search = QLineEdit(self.page_1)
        self.le_search.setObjectName(u"le_search")
        self.le_search.setClearButtonEnabled(True)

        self.verticalLayout_3.addWidget(self.le_search)

        self.fr_1 = QFrame(self.page_1)
        self.fr_1.setObjectName(u"fr_1")
        self.fr_1.setMinimumSize(QSize(0, 26))
        self.fr_1.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_1.setFrameShadow(QFrame.Shadow.Plain)
        self.vly_fr_1 = QVBoxLayout(self.fr_1)
        self.vly_fr_1.setSpacing(0)
        self.vly_fr_1.setObjectName(u"vly_fr_1")
        self.vly_fr_1.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_first = QPushButton(self.fr_1)
        self.btn_first.setObjectName(u"btn_first")
        icon = QIcon()
        icon.addFile(u":/prefijoNuevo/assets/icons/skip-up.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_first.setIcon(icon)
        self.btn_first.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_first)

        self.btn_last = QPushButton(self.fr_1)
        self.btn_last.setObjectName(u"btn_last")
        icon1 = QIcon()
        icon1.addFile(u":/prefijoNuevo/assets/icons/skip-down.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_last.setIcon(icon1)
        self.btn_last.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_last)


        self.vly_fr_1.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.fr_1)


        self.vly_margin_page1.addLayout(self.verticalLayout_3)

        self.sw.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.vly_margin_page2 = QVBoxLayout(self.page_2)
        self.vly_margin_page2.setSpacing(0)
        self.vly_margin_page2.setObjectName(u"vly_margin_page2")
        self.vly_margin_page2.setContentsMargins(0, 0, 0, 0)
        self.split_info = QSplitter(self.page_2)
        self.split_info.setObjectName(u"split_info")
        self.split_info.setOrientation(Qt.Orientation.Vertical)
        self.split_info.setHandleWidth(2)
        self.fr_image = QFrame(self.split_info)
        self.fr_image.setObjectName(u"fr_image")
        self.fr_image.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_image.setFrameShadow(QFrame.Shadow.Plain)
        self.vly_margin_viewer = QVBoxLayout(self.fr_image)
        self.vly_margin_viewer.setSpacing(2)
        self.vly_margin_viewer.setObjectName(u"vly_margin_viewer")
        self.vly_margin_viewer.setContentsMargins(2, 2, 2, 2)
        self.vly_viewer = QVBoxLayout()
        self.vly_viewer.setSpacing(4)
        self.vly_viewer.setObjectName(u"vly_viewer")

        self.vly_margin_viewer.addLayout(self.vly_viewer)

        self.split_info.addWidget(self.fr_image)
        self.te_info_media = QTextEdit(self.split_info)
        self.te_info_media.setObjectName(u"te_info_media")
        self.te_info_media.setFrameShape(QFrame.Shape.NoFrame)
        self.te_info_media.setFrameShadow(QFrame.Shadow.Plain)
        self.split_info.addWidget(self.te_info_media)

        self.vly_margin_page2.addWidget(self.split_info)

        self.sw.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.sw)

        self.fr_2 = QFrame(WidgetPlaylist)
        self.fr_2.setObjectName(u"fr_2")
        self.fr_2.setMinimumSize(QSize(0, 26))
        self.fr_2.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_2.setFrameShadow(QFrame.Shadow.Plain)
        self.vly_fr_2 = QVBoxLayout(self.fr_2)
        self.vly_fr_2.setSpacing(4)
        self.vly_fr_2.setObjectName(u"vly_fr_2")
        self.vly_fr_2.setContentsMargins(0, 0, 0, 0)
        self.hly_fr2 = QHBoxLayout()
        self.hly_fr2.setSpacing(2)
        self.hly_fr2.setObjectName(u"hly_fr2")
        self.btn_add = QPushButton(self.fr_2)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setMaximumSize(QSize(30, 16777215))
        icon2 = QIcon()
        icon2.addFile(u":/prefijoNuevo/assets/icons/plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_add.setIcon(icon2)
        self.btn_add.setIconSize(QSize(20, 20))

        self.hly_fr2.addWidget(self.btn_add)

        self.btn_delete = QPushButton(self.fr_2)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setMaximumSize(QSize(30, 16777215))
        icon3 = QIcon()
        icon3.addFile(u":/prefijoNuevo/assets/icons/minus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_delete.setIcon(icon3)
        self.btn_delete.setIconSize(QSize(20, 20))

        self.hly_fr2.addWidget(self.btn_delete)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hly_fr2.addItem(self.horizontalSpacer)

        self.btn_up = QPushButton(self.fr_2)
        self.btn_up.setObjectName(u"btn_up")
        self.btn_up.setMaximumSize(QSize(35, 16777215))
        icon4 = QIcon()
        icon4.addFile(u":/prefijoNuevo/assets/icons/up-arrow.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_up.setIcon(icon4)
        self.btn_up.setIconSize(QSize(20, 20))

        self.hly_fr2.addWidget(self.btn_up)

        self.btn_down = QPushButton(self.fr_2)
        self.btn_down.setObjectName(u"btn_down")
        self.btn_down.setMaximumSize(QSize(35, 16777215))
        icon5 = QIcon()
        icon5.addFile(u":/prefijoNuevo/assets/icons/down-arrow.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_down.setIcon(icon5)
        self.btn_down.setIconSize(QSize(20, 20))

        self.hly_fr2.addWidget(self.btn_down)

        self.btn_sort = QPushButton(self.fr_2)
        self.btn_sort.setObjectName(u"btn_sort")
        self.btn_sort.setMaximumSize(QSize(30, 16777215))
        icon6 = QIcon()
        icon6.addFile(u":/prefijoNuevo/assets/icons/order-az.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_sort.setIcon(icon6)
        self.btn_sort.setIconSize(QSize(20, 20))

        self.hly_fr2.addWidget(self.btn_sort)

        self.btn_aux = QPushButton(self.fr_2)
        self.btn_aux.setObjectName(u"btn_aux")
        self.btn_aux.setMaximumSize(QSize(30, 16777215))
        self.btn_aux.setIconSize(QSize(20, 20))

        self.hly_fr2.addWidget(self.btn_aux)


        self.vly_fr_2.addLayout(self.hly_fr2)


        self.verticalLayout.addWidget(self.fr_2)


        self.vly_margin.addLayout(self.verticalLayout)


        self.retranslateUi(WidgetPlaylist)

        self.sw.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(WidgetPlaylist)
    # setupUi

    def retranslateUi(self, WidgetPlaylist):
        WidgetPlaylist.setWindowTitle(QCoreApplication.translate("WidgetPlaylist", u"Form", None))
        self.le_search.setPlaceholderText(QCoreApplication.translate("WidgetPlaylist", u"Search ...", None))
        self.btn_first.setText("")
        self.btn_last.setText("")
        self.btn_add.setText("")
        self.btn_delete.setText("")
        self.btn_up.setText("")
        self.btn_down.setText("")
        self.btn_sort.setText("")
        self.btn_aux.setText("")
    # retranslateUi

