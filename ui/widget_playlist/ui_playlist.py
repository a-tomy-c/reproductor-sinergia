# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_playlist.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import ui.icons_sinergia

class Ui_Playlist(object):
    def setupUi(self, Playlist):
        if not Playlist.objectName():
            Playlist.setObjectName(u"Playlist")
        Playlist.resize(340, 460)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Playlist.sizePolicy().hasHeightForWidth())
        Playlist.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(Playlist)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fr_playlist = QFrame(Playlist)
        self.fr_playlist.setObjectName(u"fr_playlist")
        self.fr_playlist.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_playlist.setFrameShadow(QFrame.Shadow.Plain)
        self.fr_playlist.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.fr_playlist)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.vly_playlist = QVBoxLayout()
        self.vly_playlist.setSpacing(2)
        self.vly_playlist.setObjectName(u"vly_playlist")

        self.verticalLayout_4.addLayout(self.vly_playlist)


        self.verticalLayout.addWidget(self.fr_playlist)

        self.fr_bot = QFrame(Playlist)
        self.fr_bot.setObjectName(u"fr_bot")
        self.fr_bot.setMinimumSize(QSize(0, 32))
        self.fr_bot.setMaximumSize(QSize(16777215, 32))
        self.fr_bot.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_bot.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.fr_bot)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_up = QPushButton(self.fr_bot)
        self.btn_up.setObjectName(u"btn_up")
        self.btn_up.setMinimumSize(QSize(35, 30))
        self.btn_up.setMaximumSize(QSize(35, 30))
        icon = QIcon()
        icon.addFile(u":/a/arrow-up-2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_up.setIcon(icon)
        self.btn_up.setIconSize(QSize(24, 24))
        self.btn_up.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_up)

        self.btn_down = QPushButton(self.fr_bot)
        self.btn_down.setObjectName(u"btn_down")
        self.btn_down.setMinimumSize(QSize(35, 30))
        self.btn_down.setMaximumSize(QSize(35, 30))
        icon1 = QIcon()
        icon1.addFile(u":/a/arrow-down-2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_down.setIcon(icon1)
        self.btn_down.setIconSize(QSize(24, 24))
        self.btn_down.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_down)

        self.le_search = QLineEdit(self.fr_bot)
        self.le_search.setObjectName(u"le_search")
        self.le_search.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.le_search)

        self.btn_move_up = QPushButton(self.fr_bot)
        self.btn_move_up.setObjectName(u"btn_move_up")
        self.btn_move_up.setMinimumSize(QSize(35, 30))
        self.btn_move_up.setMaximumSize(QSize(35, 30))
        icon2 = QIcon()
        icon2.addFile(u":/a/line-up.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_move_up.setIcon(icon2)
        self.btn_move_up.setIconSize(QSize(24, 24))
        self.btn_move_up.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_move_up)

        self.btn_move_down = QPushButton(self.fr_bot)
        self.btn_move_down.setObjectName(u"btn_move_down")
        self.btn_move_down.setMinimumSize(QSize(35, 30))
        self.btn_move_down.setMaximumSize(QSize(35, 30))
        icon3 = QIcon()
        icon3.addFile(u":/a/line-down.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_move_down.setIcon(icon3)
        self.btn_move_down.setIconSize(QSize(24, 24))
        self.btn_move_down.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_move_down)

        self.btn_delete = QPushButton(self.fr_bot)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setMinimumSize(QSize(35, 30))
        self.btn_delete.setMaximumSize(QSize(35, 30))
        icon4 = QIcon()
        icon4.addFile(u":/a/backspace.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_delete.setIcon(icon4)
        self.btn_delete.setIconSize(QSize(24, 24))
        self.btn_delete.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_delete)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.fr_bot)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Playlist)

        QMetaObject.connectSlotsByName(Playlist)
    # setupUi

    def retranslateUi(self, Playlist):
        Playlist.setWindowTitle(QCoreApplication.translate("Playlist", u"Form", None))
#if QT_CONFIG(tooltip)
        self.btn_up.setToolTip(QCoreApplication.translate("Playlist", u"selecciona el anterior item", None))
#endif // QT_CONFIG(tooltip)
        self.btn_up.setText("")
#if QT_CONFIG(tooltip)
        self.btn_down.setToolTip(QCoreApplication.translate("Playlist", u"selecciona el siguiente item", None))
#endif // QT_CONFIG(tooltip)
        self.btn_down.setText("")
#if QT_CONFIG(tooltip)
        self.btn_move_up.setToolTip(QCoreApplication.translate("Playlist", u"mueve el item arriba", None))
#endif // QT_CONFIG(tooltip)
        self.btn_move_up.setText("")
#if QT_CONFIG(tooltip)
        self.btn_move_down.setToolTip(QCoreApplication.translate("Playlist", u"mueve el item abajo", None))
#endif // QT_CONFIG(tooltip)
        self.btn_move_down.setText("")
#if QT_CONFIG(tooltip)
        self.btn_delete.setToolTip(QCoreApplication.translate("Playlist", u"borra el item seleccionado de la playlist", None))
#endif // QT_CONFIG(tooltip)
        self.btn_delete.setText("")
    # retranslateUi

