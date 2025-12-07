# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_volume.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSlider, QWidget)

class Ui_WidgetVolume(object):
    def setupUi(self, WidgetVolume):
        if not WidgetVolume.objectName():
            WidgetVolume.setObjectName(u"WidgetVolume")
        WidgetVolume.resize(120, 32)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WidgetVolume.sizePolicy().hasHeightForWidth())
        WidgetVolume.setSizePolicy(sizePolicy)
        WidgetVolume.setMinimumSize(QSize(120, 0))
        WidgetVolume.setMaximumSize(QSize(140, 32))
        self.horizontalLayout_2 = QHBoxLayout(WidgetVolume)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_volume = QPushButton(WidgetVolume)
        self.btn_volume.setObjectName(u"btn_volume")
        self.btn_volume.setMinimumSize(QSize(30, 30))
        self.btn_volume.setMaximumSize(QSize(30, 30))
        self.btn_volume.setIconSize(QSize(24, 24))
        self.btn_volume.setCheckable(True)
        self.btn_volume.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_volume)

        self.sld_volume = QSlider(WidgetVolume)
        self.sld_volume.setObjectName(u"sld_volume")
        self.sld_volume.setMaximum(100)
        self.sld_volume.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout.addWidget(self.sld_volume)

        self.lb_volume = QLabel(WidgetVolume)
        self.lb_volume.setObjectName(u"lb_volume")
        font = QFont()
        font.setPointSize(12)
        self.lb_volume.setFont(font)
        self.lb_volume.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_volume)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(WidgetVolume)

        QMetaObject.connectSlotsByName(WidgetVolume)
    # setupUi

    def retranslateUi(self, WidgetVolume):
        WidgetVolume.setWindowTitle(QCoreApplication.translate("WidgetVolume", u"Form", None))
        self.btn_volume.setText("")
        self.lb_volume.setText(QCoreApplication.translate("WidgetVolume", u"100", None))
    # retranslateUi

