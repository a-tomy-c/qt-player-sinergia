# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_control.ui'
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
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QVBoxLayout, QWidget)
import rsc.icons

class Ui_WidgetControl(object):
    def setupUi(self, WidgetControl):
        if not WidgetControl.objectName():
            WidgetControl.setObjectName(u"WidgetControl")
        WidgetControl.resize(767, 59)
        self.vly_margin = QVBoxLayout(WidgetControl)
        self.vly_margin.setSpacing(4)
        self.vly_margin.setObjectName(u"vly_margin")
        self.vly_margin.setContentsMargins(4, 4, 4, 4)
        self.vly = QVBoxLayout()
        self.vly.setSpacing(0)
        self.vly.setObjectName(u"vly")
        self.sld_time = QSlider(WidgetControl)
        self.sld_time.setObjectName(u"sld_time")
        self.sld_time.setOrientation(Qt.Orientation.Horizontal)

        self.vly.addWidget(self.sld_time)

        self.fr_btns = QFrame(WidgetControl)
        self.fr_btns.setObjectName(u"fr_btns")
        self.fr_btns.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_btns.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout = QVBoxLayout(self.fr_btns)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_toggle_playlist = QPushButton(self.fr_btns)
        self.btn_toggle_playlist.setObjectName(u"btn_toggle_playlist")
        self.btn_toggle_playlist.setMinimumSize(QSize(30, 0))
        self.btn_toggle_playlist.setMaximumSize(QSize(35, 16777215))
        icon = QIcon()
        icon.addFile(u":/prefijoNuevo/assets/icons/square-half.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_toggle_playlist.setIcon(icon)
        self.btn_toggle_playlist.setIconSize(QSize(26, 26))
        self.btn_toggle_playlist.setCheckable(True)

        self.horizontalLayout.addWidget(self.btn_toggle_playlist)

        self.btn_file = QPushButton(self.fr_btns)
        self.btn_file.setObjectName(u"btn_file")
        self.btn_file.setMinimumSize(QSize(30, 0))
        self.btn_file.setMaximumSize(QSize(35, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/prefijoNuevo/assets/icons/file-add.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_file.setIcon(icon1)
        self.btn_file.setIconSize(QSize(26, 26))

        self.horizontalLayout.addWidget(self.btn_file)

        self.btn_dir = QPushButton(self.fr_btns)
        self.btn_dir.setObjectName(u"btn_dir")
        self.btn_dir.setMinimumSize(QSize(30, 0))
        self.btn_dir.setMaximumSize(QSize(35, 16777215))
        icon2 = QIcon()
        icon2.addFile(u":/prefijoNuevo/assets/icons/add-folder.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_dir.setIcon(icon2)
        self.btn_dir.setIconSize(QSize(26, 26))

        self.horizontalLayout.addWidget(self.btn_dir)

        self.btn_skip_backward = QPushButton(self.fr_btns)
        self.btn_skip_backward.setObjectName(u"btn_skip_backward")
        self.btn_skip_backward.setMinimumSize(QSize(30, 0))
        self.btn_skip_backward.setMaximumSize(QSize(35, 16777215))
        icon3 = QIcon()
        icon3.addFile(u":/prefijoNuevo/assets/icons/skip-back.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_skip_backward.setIcon(icon3)
        self.btn_skip_backward.setIconSize(QSize(26, 26))

        self.horizontalLayout.addWidget(self.btn_skip_backward)

        self.btn_backward = QPushButton(self.fr_btns)
        self.btn_backward.setObjectName(u"btn_backward")
        self.btn_backward.setMinimumSize(QSize(30, 0))
        self.btn_backward.setMaximumSize(QSize(35, 16777215))
        icon4 = QIcon()
        icon4.addFile(u":/prefijoNuevo/assets/icons/backward.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_backward.setIcon(icon4)
        self.btn_backward.setIconSize(QSize(26, 26))

        self.horizontalLayout.addWidget(self.btn_backward)

        self.btn_play = QPushButton(self.fr_btns)
        self.btn_play.setObjectName(u"btn_play")
        self.btn_play.setMinimumSize(QSize(35, 0))
        self.btn_play.setMaximumSize(QSize(35, 16777215))
        icon5 = QIcon()
        icon5.addFile(u":/prefijoNuevo/assets/icons/play.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_play.setIcon(icon5)
        self.btn_play.setIconSize(QSize(26, 26))
        self.btn_play.setCheckable(True)

        self.horizontalLayout.addWidget(self.btn_play)

        self.btn_skip_forward = QPushButton(self.fr_btns)
        self.btn_skip_forward.setObjectName(u"btn_skip_forward")
        self.btn_skip_forward.setMinimumSize(QSize(30, 0))
        self.btn_skip_forward.setMaximumSize(QSize(35, 16777215))
        icon6 = QIcon()
        icon6.addFile(u":/prefijoNuevo/assets/icons/skip-forward.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_skip_forward.setIcon(icon6)
        self.btn_skip_forward.setIconSize(QSize(26, 26))

        self.horizontalLayout.addWidget(self.btn_skip_forward)

        self.btn_forward = QPushButton(self.fr_btns)
        self.btn_forward.setObjectName(u"btn_forward")
        self.btn_forward.setMinimumSize(QSize(30, 0))
        self.btn_forward.setMaximumSize(QSize(35, 16777215))
        icon7 = QIcon()
        icon7.addFile(u":/prefijoNuevo/assets/icons/forward.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_forward.setIcon(icon7)
        self.btn_forward.setIconSize(QSize(26, 26))

        self.horizontalLayout.addWidget(self.btn_forward)

        self.btn_stop = QPushButton(self.fr_btns)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setMinimumSize(QSize(30, 0))
        self.btn_stop.setMaximumSize(QSize(35, 16777215))
        icon8 = QIcon()
        icon8.addFile(u":/prefijoNuevo/assets/icons/stop.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_stop.setIcon(icon8)
        self.btn_stop.setIconSize(QSize(26, 26))

        self.horizontalLayout.addWidget(self.btn_stop)

        self.btn_shuffle = QPushButton(self.fr_btns)
        self.btn_shuffle.setObjectName(u"btn_shuffle")
        self.btn_shuffle.setMinimumSize(QSize(30, 0))
        self.btn_shuffle.setMaximumSize(QSize(35, 16777215))
        icon9 = QIcon()
        icon9.addFile(u":/prefijoNuevo/assets/icons/shuffle-on.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_shuffle.setIcon(icon9)
        self.btn_shuffle.setIconSize(QSize(26, 26))
        self.btn_shuffle.setCheckable(True)

        self.horizontalLayout.addWidget(self.btn_shuffle)

        self.btn_loop = QPushButton(self.fr_btns)
        self.btn_loop.setObjectName(u"btn_loop")
        self.btn_loop.setMinimumSize(QSize(30, 0))
        self.btn_loop.setMaximumSize(QSize(35, 16777215))
        icon10 = QIcon()
        icon10.addFile(u":/prefijoNuevo/assets/icons/repeat.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_loop.setIcon(icon10)
        self.btn_loop.setIconSize(QSize(26, 26))
        self.btn_loop.setCheckable(True)

        self.horizontalLayout.addWidget(self.btn_loop)

        self.lb_time = QLabel(self.fr_btns)
        self.lb_time.setObjectName(u"lb_time")
        self.lb_time.setMaximumSize(QSize(90, 16777215))
        font = QFont()
        font.setPointSize(16)
        self.lb_time.setFont(font)
        self.lb_time.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_time)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.lb_duration = QLabel(self.fr_btns)
        self.lb_duration.setObjectName(u"lb_duration")
        self.lb_duration.setMaximumSize(QSize(90, 16777215))
        self.lb_duration.setFont(font)
        self.lb_duration.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_duration)

        self.btn_volume = QPushButton(self.fr_btns)
        self.btn_volume.setObjectName(u"btn_volume")
        self.btn_volume.setMinimumSize(QSize(30, 0))
        self.btn_volume.setMaximumSize(QSize(35, 16777215))
        icon11 = QIcon()
        icon11.addFile(u":/prefijoNuevo/assets/icons/volume-low.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_volume.setIcon(icon11)
        self.btn_volume.setIconSize(QSize(26, 26))
        self.btn_volume.setCheckable(True)

        self.horizontalLayout.addWidget(self.btn_volume)

        self.sld_volume = QSlider(self.fr_btns)
        self.sld_volume.setObjectName(u"sld_volume")
        self.sld_volume.setMaximumSize(QSize(70, 16777215))
        self.sld_volume.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout.addWidget(self.sld_volume)

        self.btn_settings = QPushButton(self.fr_btns)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setMinimumSize(QSize(30, 0))
        self.btn_settings.setMaximumSize(QSize(35, 16777215))
        icon12 = QIcon()
        icon12.addFile(u":/prefijoNuevo/assets/icons/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_settings.setIcon(icon12)
        self.btn_settings.setIconSize(QSize(26, 26))
        self.btn_settings.setCheckable(True)

        self.horizontalLayout.addWidget(self.btn_settings)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.vly.addWidget(self.fr_btns)


        self.vly_margin.addLayout(self.vly)


        self.retranslateUi(WidgetControl)

        QMetaObject.connectSlotsByName(WidgetControl)
    # setupUi

    def retranslateUi(self, WidgetControl):
        WidgetControl.setWindowTitle(QCoreApplication.translate("WidgetControl", u"Form", None))
        self.btn_toggle_playlist.setText("")
        self.btn_file.setText("")
        self.btn_dir.setText("")
        self.btn_skip_backward.setText("")
        self.btn_backward.setText("")
        self.btn_play.setText("")
        self.btn_skip_forward.setText("")
        self.btn_forward.setText("")
        self.btn_stop.setText("")
        self.btn_shuffle.setText("")
        self.btn_loop.setText("")
        self.lb_time.setText(QCoreApplication.translate("WidgetControl", u"00:00:00", None))
        self.lb_duration.setText(QCoreApplication.translate("WidgetControl", u"00:00:00", None))
        self.btn_volume.setText("")
        self.btn_settings.setText("")
    # retranslateUi

