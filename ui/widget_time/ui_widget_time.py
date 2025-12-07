# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_time.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QSlider, QWidget)

class Ui_WidgetTime(object):
    def setupUi(self, WidgetTime):
        if not WidgetTime.objectName():
            WidgetTime.setObjectName(u"WidgetTime")
        WidgetTime.resize(320, 32)
        self.horizontalLayout_2 = QHBoxLayout(WidgetTime)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sld_time = QSlider(WidgetTime)
        self.sld_time.setObjectName(u"sld_time")
        self.sld_time.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout.addWidget(self.sld_time)

        self.btn_timestamp = QPushButton(WidgetTime)
        self.btn_timestamp.setObjectName(u"btn_timestamp")
        self.btn_timestamp.setMinimumSize(QSize(78, 0))
        self.btn_timestamp.setMaximumSize(QSize(78, 30))
        font = QFont()
        font.setPointSize(12)
        self.btn_timestamp.setFont(font)
        self.btn_timestamp.setIconSize(QSize(24, 24))
        self.btn_timestamp.setCheckable(True)
        self.btn_timestamp.setChecked(False)
        self.btn_timestamp.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_timestamp)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(WidgetTime)

        QMetaObject.connectSlotsByName(WidgetTime)
    # setupUi

    def retranslateUi(self, WidgetTime):
        WidgetTime.setWindowTitle(QCoreApplication.translate("WidgetTime", u"Form", None))
        self.btn_timestamp.setText(QCoreApplication.translate("WidgetTime", u"-00:00:00", None))
    # retranslateUi

