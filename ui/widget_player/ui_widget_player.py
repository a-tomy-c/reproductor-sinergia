# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_player.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_WidgetPlayer(object):
    def setupUi(self, WidgetPlayer):
        if not WidgetPlayer.objectName():
            WidgetPlayer.setObjectName(u"WidgetPlayer")
        WidgetPlayer.resize(605, 389)
        self.vly_wp = QVBoxLayout(WidgetPlayer)
        self.vly_wp.setSpacing(2)
        self.vly_wp.setObjectName(u"vly_wp")
        self.vly_wp.setContentsMargins(0, 0, 0, 0)
        self.vly_main = QVBoxLayout()
        self.vly_main.setSpacing(0)
        self.vly_main.setObjectName(u"vly_main")
        self.fr_top = QFrame(WidgetPlayer)
        self.fr_top.setObjectName(u"fr_top")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fr_top.sizePolicy().hasHeightForWidth())
        self.fr_top.setSizePolicy(sizePolicy)
        self.fr_top.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_top.setFrameShadow(QFrame.Shadow.Plain)
        self.fr_top.setLineWidth(0)
        self.hly_top = QHBoxLayout(self.fr_top)
        self.hly_top.setSpacing(2)
        self.hly_top.setObjectName(u"hly_top")
        self.hly_top.setContentsMargins(0, 0, 0, 0)
        self.fr_no = QFrame(self.fr_top)
        self.fr_no.setObjectName(u"fr_no")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.fr_no.sizePolicy().hasHeightForWidth())
        self.fr_no.setSizePolicy(sizePolicy1)
        self.fr_no.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_no.setFrameShadow(QFrame.Shadow.Plain)
        self.fr_no.setLineWidth(0)
        self.vly_no = QVBoxLayout(self.fr_no)
        self.vly_no.setSpacing(2)
        self.vly_no.setObjectName(u"vly_no")
        self.vly_no.setContentsMargins(0, 0, 0, 0)
        self.hly_no = QHBoxLayout()
        self.hly_no.setSpacing(2)
        self.hly_no.setObjectName(u"hly_no")

        self.vly_no.addLayout(self.hly_no)


        self.hly_top.addWidget(self.fr_no)

        self.fr_n = QFrame(self.fr_top)
        self.fr_n.setObjectName(u"fr_n")
        sizePolicy.setHeightForWidth(self.fr_n.sizePolicy().hasHeightForWidth())
        self.fr_n.setSizePolicy(sizePolicy)
        self.fr_n.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_n.setFrameShadow(QFrame.Shadow.Plain)
        self.fr_n.setLineWidth(0)
        self.vly_n = QVBoxLayout(self.fr_n)
        self.vly_n.setSpacing(2)
        self.vly_n.setObjectName(u"vly_n")
        self.vly_n.setContentsMargins(0, 0, 0, 0)
        self.hly_n = QHBoxLayout()
        self.hly_n.setSpacing(2)
        self.hly_n.setObjectName(u"hly_n")

        self.vly_n.addLayout(self.hly_n)


        self.hly_top.addWidget(self.fr_n)

        self.fr_ne = QFrame(self.fr_top)
        self.fr_ne.setObjectName(u"fr_ne")
        sizePolicy1.setHeightForWidth(self.fr_ne.sizePolicy().hasHeightForWidth())
        self.fr_ne.setSizePolicy(sizePolicy1)
        self.fr_ne.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_ne.setFrameShadow(QFrame.Shadow.Plain)
        self.fr_ne.setLineWidth(0)
        self.vly_ne = QVBoxLayout(self.fr_ne)
        self.vly_ne.setSpacing(2)
        self.vly_ne.setObjectName(u"vly_ne")
        self.vly_ne.setContentsMargins(0, 0, 0, 0)
        self.hly_ne = QHBoxLayout()
        self.hly_ne.setSpacing(2)
        self.hly_ne.setObjectName(u"hly_ne")

        self.vly_ne.addLayout(self.hly_ne)


        self.hly_top.addWidget(self.fr_ne)

        self.hly_top.setStretch(1, 1)

        self.vly_main.addWidget(self.fr_top)

        self.fr_mid = QFrame(WidgetPlayer)
        self.fr_mid.setObjectName(u"fr_mid")
        self.fr_mid.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_mid.setFrameShadow(QFrame.Shadow.Plain)
        self.fr_mid.setLineWidth(0)
        self.hly_mid = QHBoxLayout(self.fr_mid)
        self.hly_mid.setSpacing(2)
        self.hly_mid.setObjectName(u"hly_mid")
        self.hly_mid.setContentsMargins(0, 0, 0, 0)
        self.fr_co = QFrame(self.fr_mid)
        self.fr_co.setObjectName(u"fr_co")
        sizePolicy.setHeightForWidth(self.fr_co.sizePolicy().hasHeightForWidth())
        self.fr_co.setSizePolicy(sizePolicy)
        self.fr_co.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_co.setFrameShadow(QFrame.Shadow.Plain)
        self.fr_co.setLineWidth(0)
        self.vly_co = QVBoxLayout(self.fr_co)
        self.vly_co.setSpacing(2)
        self.vly_co.setObjectName(u"vly_co")
        self.vly_co.setContentsMargins(0, 0, 0, 0)
        self.hly_co = QHBoxLayout()
        self.hly_co.setSpacing(2)
        self.hly_co.setObjectName(u"hly_co")

        self.vly_co.addLayout(self.hly_co)


        self.hly_mid.addWidget(self.fr_co)

        self.fr_center = QFrame(self.fr_mid)
        self.fr_center.setObjectName(u"fr_center")
        sizePolicy.setHeightForWidth(self.fr_center.sizePolicy().hasHeightForWidth())
        self.fr_center.setSizePolicy(sizePolicy)
        self.fr_center.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_center.setFrameShadow(QFrame.Shadow.Plain)
        self.fr_center.setLineWidth(0)
        self.vly_center = QVBoxLayout(self.fr_center)
        self.vly_center.setSpacing(2)
        self.vly_center.setObjectName(u"vly_center")
        self.vly_center.setContentsMargins(0, 0, 0, 0)
        self.hly_center = QHBoxLayout()
        self.hly_center.setSpacing(2)
        self.hly_center.setObjectName(u"hly_center")

        self.vly_center.addLayout(self.hly_center)


        self.hly_mid.addWidget(self.fr_center)

        self.fr_ce = QFrame(self.fr_mid)
        self.fr_ce.setObjectName(u"fr_ce")
        sizePolicy.setHeightForWidth(self.fr_ce.sizePolicy().hasHeightForWidth())
        self.fr_ce.setSizePolicy(sizePolicy)
        self.fr_ce.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_ce.setFrameShadow(QFrame.Shadow.Plain)
        self.fr_ce.setLineWidth(0)
        self.vly_ce = QVBoxLayout(self.fr_ce)
        self.vly_ce.setSpacing(2)
        self.vly_ce.setObjectName(u"vly_ce")
        self.vly_ce.setContentsMargins(0, 0, 0, 0)
        self.hly_ce = QHBoxLayout()
        self.hly_ce.setSpacing(2)
        self.hly_ce.setObjectName(u"hly_ce")

        self.vly_ce.addLayout(self.hly_ce)


        self.hly_mid.addWidget(self.fr_ce)

        self.hly_mid.setStretch(1, 1)

        self.vly_main.addWidget(self.fr_mid)

        self.fr_bot = QFrame(WidgetPlayer)
        self.fr_bot.setObjectName(u"fr_bot")
        sizePolicy.setHeightForWidth(self.fr_bot.sizePolicy().hasHeightForWidth())
        self.fr_bot.setSizePolicy(sizePolicy)
        self.fr_bot.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_bot.setFrameShadow(QFrame.Shadow.Plain)
        self.fr_bot.setLineWidth(0)
        self.hly_bot = QHBoxLayout(self.fr_bot)
        self.hly_bot.setSpacing(2)
        self.hly_bot.setObjectName(u"hly_bot")
        self.hly_bot.setContentsMargins(0, 0, 0, 0)
        self.fr_so = QFrame(self.fr_bot)
        self.fr_so.setObjectName(u"fr_so")
        sizePolicy1.setHeightForWidth(self.fr_so.sizePolicy().hasHeightForWidth())
        self.fr_so.setSizePolicy(sizePolicy1)
        self.fr_so.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_so.setFrameShadow(QFrame.Shadow.Plain)
        self.fr_so.setLineWidth(0)
        self.vly_so = QVBoxLayout(self.fr_so)
        self.vly_so.setSpacing(2)
        self.vly_so.setObjectName(u"vly_so")
        self.vly_so.setContentsMargins(0, 0, 0, 0)
        self.hly_so = QHBoxLayout()
        self.hly_so.setSpacing(2)
        self.hly_so.setObjectName(u"hly_so")

        self.vly_so.addLayout(self.hly_so)


        self.hly_bot.addWidget(self.fr_so)

        self.fr_s = QFrame(self.fr_bot)
        self.fr_s.setObjectName(u"fr_s")
        sizePolicy.setHeightForWidth(self.fr_s.sizePolicy().hasHeightForWidth())
        self.fr_s.setSizePolicy(sizePolicy)
        self.fr_s.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_s.setFrameShadow(QFrame.Shadow.Plain)
        self.fr_s.setLineWidth(0)
        self.vly_s = QVBoxLayout(self.fr_s)
        self.vly_s.setSpacing(2)
        self.vly_s.setObjectName(u"vly_s")
        self.vly_s.setContentsMargins(0, 0, 0, 0)
        self.hly_s = QHBoxLayout()
        self.hly_s.setSpacing(2)
        self.hly_s.setObjectName(u"hly_s")

        self.vly_s.addLayout(self.hly_s)


        self.hly_bot.addWidget(self.fr_s)

        self.fr_se = QFrame(self.fr_bot)
        self.fr_se.setObjectName(u"fr_se")
        sizePolicy1.setHeightForWidth(self.fr_se.sizePolicy().hasHeightForWidth())
        self.fr_se.setSizePolicy(sizePolicy1)
        self.fr_se.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_se.setFrameShadow(QFrame.Shadow.Plain)
        self.fr_se.setLineWidth(0)
        self.vly_se = QVBoxLayout(self.fr_se)
        self.vly_se.setSpacing(2)
        self.vly_se.setObjectName(u"vly_se")
        self.vly_se.setContentsMargins(0, 0, 0, 0)
        self.hly_se = QHBoxLayout()
        self.hly_se.setSpacing(2)
        self.hly_se.setObjectName(u"hly_se")

        self.vly_se.addLayout(self.hly_se)


        self.hly_bot.addWidget(self.fr_se)

        self.hly_bot.setStretch(1, 1)

        self.vly_main.addWidget(self.fr_bot)


        self.vly_wp.addLayout(self.vly_main)


        self.retranslateUi(WidgetPlayer)

        QMetaObject.connectSlotsByName(WidgetPlayer)
    # setupUi

    def retranslateUi(self, WidgetPlayer):
        WidgetPlayer.setWindowTitle(QCoreApplication.translate("WidgetPlayer", u"Form", None))
    # retranslateUi

