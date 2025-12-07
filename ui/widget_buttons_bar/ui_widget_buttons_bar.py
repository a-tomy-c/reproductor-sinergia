# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_buttons_bar.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import ui.icons_sinergia

class Ui_WidgetButtonsBar(object):
    def setupUi(self, WidgetButtonsBar):
        if not WidgetButtonsBar.objectName():
            WidgetButtonsBar.setObjectName(u"WidgetButtonsBar")
        WidgetButtonsBar.resize(547, 34)
        self.vly_buttons_bar = QVBoxLayout(WidgetButtonsBar)
        self.vly_buttons_bar.setSpacing(0)
        self.vly_buttons_bar.setObjectName(u"vly_buttons_bar")
        self.vly_buttons_bar.setContentsMargins(0, 0, 0, 0)
        self.hly_buttons_bar = QHBoxLayout()
        self.hly_buttons_bar.setSpacing(2)
        self.hly_buttons_bar.setObjectName(u"hly_buttons_bar")
        self.fr_left = QFrame(WidgetButtonsBar)
        self.fr_left.setObjectName(u"fr_left")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fr_left.sizePolicy().hasHeightForWidth())
        self.fr_left.setSizePolicy(sizePolicy)
        self.fr_left.setMaximumSize(QSize(16777215, 32))
        self.fr_left.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_left.setFrameShadow(QFrame.Shadow.Plain)
        self.fr_left.setLineWidth(0)
        self.vly_left = QVBoxLayout(self.fr_left)
        self.vly_left.setObjectName(u"vly_left")
        self.vly_left.setContentsMargins(2, 2, 2, 2)
        self.hly_left = QHBoxLayout()
        self.hly_left.setSpacing(2)
        self.hly_left.setObjectName(u"hly_left")

        self.vly_left.addLayout(self.hly_left)


        self.hly_buttons_bar.addWidget(self.fr_left)

        self.fr_mid = QFrame(WidgetButtonsBar)
        self.fr_mid.setObjectName(u"fr_mid")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.fr_mid.sizePolicy().hasHeightForWidth())
        self.fr_mid.setSizePolicy(sizePolicy1)
        self.fr_mid.setMinimumSize(QSize(0, 0))
        self.fr_mid.setMaximumSize(QSize(16777215, 32))
        self.fr_mid.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_mid.setFrameShadow(QFrame.Shadow.Plain)
        self.fr_mid.setLineWidth(0)
        self.vly_mid = QVBoxLayout(self.fr_mid)
        self.vly_mid.setObjectName(u"vly_mid")
        self.vly_mid.setContentsMargins(2, 2, 2, 2)
        self.hly_mid = QHBoxLayout()
        self.hly_mid.setSpacing(2)
        self.hly_mid.setObjectName(u"hly_mid")
        self.btn_toggle_playlist = QPushButton(self.fr_mid)
        self.btn_toggle_playlist.setObjectName(u"btn_toggle_playlist")
        self.btn_toggle_playlist.setMinimumSize(QSize(35, 30))
        self.btn_toggle_playlist.setMaximumSize(QSize(35, 30))
        self.btn_toggle_playlist.setIconSize(QSize(24, 24))
        self.btn_toggle_playlist.setCheckable(True)
        self.btn_toggle_playlist.setFlat(True)

        self.hly_mid.addWidget(self.btn_toggle_playlist)

        self.btn_fullscreen = QPushButton(self.fr_mid)
        self.btn_fullscreen.setObjectName(u"btn_fullscreen")
        self.btn_fullscreen.setMinimumSize(QSize(35, 30))
        self.btn_fullscreen.setMaximumSize(QSize(35, 30))
        self.btn_fullscreen.setIconSize(QSize(24, 24))
        self.btn_fullscreen.setCheckable(True)
        self.btn_fullscreen.setFlat(True)

        self.hly_mid.addWidget(self.btn_fullscreen)

        self.lb_info = QLabel(self.fr_mid)
        self.lb_info.setObjectName(u"lb_info")

        self.hly_mid.addWidget(self.lb_info)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hly_mid.addItem(self.horizontalSpacer)

        self.btn_play = QPushButton(self.fr_mid)
        self.btn_play.setObjectName(u"btn_play")
        self.btn_play.setMinimumSize(QSize(35, 30))
        self.btn_play.setMaximumSize(QSize(35, 30))
        self.btn_play.setIconSize(QSize(24, 24))
        self.btn_play.setCheckable(True)
        self.btn_play.setFlat(True)

        self.hly_mid.addWidget(self.btn_play)

        self.btn_stop = QPushButton(self.fr_mid)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setMinimumSize(QSize(35, 30))
        self.btn_stop.setMaximumSize(QSize(35, 30))
        self.btn_stop.setIconSize(QSize(24, 24))
        self.btn_stop.setFlat(True)

        self.hly_mid.addWidget(self.btn_stop)

        self.btn_backward = QPushButton(self.fr_mid)
        self.btn_backward.setObjectName(u"btn_backward")
        self.btn_backward.setMinimumSize(QSize(35, 30))
        self.btn_backward.setMaximumSize(QSize(35, 30))
        self.btn_backward.setIconSize(QSize(24, 24))
        self.btn_backward.setFlat(True)

        self.hly_mid.addWidget(self.btn_backward)

        self.btn_forward = QPushButton(self.fr_mid)
        self.btn_forward.setObjectName(u"btn_forward")
        self.btn_forward.setMinimumSize(QSize(35, 30))
        self.btn_forward.setMaximumSize(QSize(35, 30))
        self.btn_forward.setIconSize(QSize(24, 24))
        self.btn_forward.setFlat(True)

        self.hly_mid.addWidget(self.btn_forward)

        self.btn_previous = QPushButton(self.fr_mid)
        self.btn_previous.setObjectName(u"btn_previous")
        self.btn_previous.setMinimumSize(QSize(35, 30))
        self.btn_previous.setMaximumSize(QSize(35, 30))
        self.btn_previous.setIconSize(QSize(24, 24))
        self.btn_previous.setFlat(True)

        self.hly_mid.addWidget(self.btn_previous)

        self.btn_next = QPushButton(self.fr_mid)
        self.btn_next.setObjectName(u"btn_next")
        self.btn_next.setMinimumSize(QSize(35, 30))
        self.btn_next.setMaximumSize(QSize(35, 30))
        self.btn_next.setIconSize(QSize(24, 24))
        self.btn_next.setFlat(True)

        self.hly_mid.addWidget(self.btn_next)


        self.vly_mid.addLayout(self.hly_mid)


        self.hly_buttons_bar.addWidget(self.fr_mid)

        self.fr_right = QFrame(WidgetButtonsBar)
        self.fr_right.setObjectName(u"fr_right")
        sizePolicy.setHeightForWidth(self.fr_right.sizePolicy().hasHeightForWidth())
        self.fr_right.setSizePolicy(sizePolicy)
        self.fr_right.setMaximumSize(QSize(16777215, 32))
        self.fr_right.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_right.setFrameShadow(QFrame.Shadow.Plain)
        self.fr_right.setLineWidth(0)
        self.vly_right = QVBoxLayout(self.fr_right)
        self.vly_right.setObjectName(u"vly_right")
        self.vly_right.setContentsMargins(2, 2, 2, 2)
        self.hly_right = QHBoxLayout()
        self.hly_right.setSpacing(2)
        self.hly_right.setObjectName(u"hly_right")

        self.vly_right.addLayout(self.hly_right)


        self.hly_buttons_bar.addWidget(self.fr_right)


        self.vly_buttons_bar.addLayout(self.hly_buttons_bar)


        self.retranslateUi(WidgetButtonsBar)

        QMetaObject.connectSlotsByName(WidgetButtonsBar)
    # setupUi

    def retranslateUi(self, WidgetButtonsBar):
        WidgetButtonsBar.setWindowTitle(QCoreApplication.translate("WidgetButtonsBar", u"Form", None))
        self.btn_toggle_playlist.setText("")
        self.btn_fullscreen.setText("")
        self.lb_info.setText("")
        self.btn_play.setText("")
        self.btn_stop.setText("")
        self.btn_backward.setText("")
        self.btn_forward.setText("")
        self.btn_previous.setText("")
        self.btn_next.setText("")
    # retranslateUi

