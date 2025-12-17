# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'playerUi.ui'
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
    QLineEdit, QListView, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QWidget)
import icons.rc_icons

class Ui_Player(object):
    def setupUi(self, Player):
        if not Player.objectName():
            Player.setObjectName(u"Player")
        Player.resize(994, 657)
        self.centralWidget = QWidget(Player)
        self.centralWidget.setObjectName(u"centralWidget")
        self.gridCentral = QGridLayout(self.centralWidget)
        self.gridCentral.setObjectName(u"gridCentral")
        self.frBarra = QFrame(self.centralWidget)
        self.frBarra.setObjectName(u"frBarra")
        self.frBarra.setMinimumSize(QSize(0, 52))
        self.frBarra.setMaximumSize(QSize(16777215, 52))
        self.frBarra.setFrameShape(QFrame.Shape.StyledPanel)
        self.frBarra.setFrameShadow(QFrame.Shadow.Raised)
        self.gridBarra = QGridLayout(self.frBarra)
        self.gridBarra.setObjectName(u"gridBarra")
        self.gridBarra.setContentsMargins(4, 4, 4, 4)
        self.btPin = QPushButton(self.frBarra)
        self.btPin.setObjectName(u"btPin")
        self.btPin.setMinimumSize(QSize(42, 42))
        self.btPin.setMaximumSize(QSize(42, 42))
        self.btPin.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/pin-a.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btPin.setIcon(icon)
        self.btPin.setIconSize(QSize(27, 30))
        self.btPin.setAutoRepeatInterval(300)

        self.gridBarra.addWidget(self.btPin, 0, 2, 1, 1)

        self.btMax = QPushButton(self.frBarra)
        self.btMax.setObjectName(u"btMax")
        self.btMax.setMinimumSize(QSize(42, 42))
        self.btMax.setMaximumSize(QSize(42, 42))
        self.btMax.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/maximize.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btMax.setIcon(icon1)
        self.btMax.setIconSize(QSize(27, 30))

        self.gridBarra.addWidget(self.btMax, 0, 4, 1, 1)

        self.btSquare = QPushButton(self.frBarra)
        self.btSquare.setObjectName(u"btSquare")
        self.btSquare.setMinimumSize(QSize(42, 42))
        self.btSquare.setMaximumSize(QSize(42, 42))
        self.btSquare.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/square.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btSquare.setIcon(icon2)
        self.btSquare.setIconSize(QSize(27, 30))

        self.gridBarra.addWidget(self.btSquare, 0, 5, 1, 1)

        self.btMin = QPushButton(self.frBarra)
        self.btMin.setObjectName(u"btMin")
        self.btMin.setMinimumSize(QSize(42, 42))
        self.btMin.setMaximumSize(QSize(42, 42))
        self.btMin.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/minimize.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btMin.setIcon(icon3)
        self.btMin.setIconSize(QSize(27, 30))

        self.gridBarra.addWidget(self.btMin, 0, 3, 1, 1)

        self.lbNombreApp = QLabel(self.frBarra)
        self.lbNombreApp.setObjectName(u"lbNombreApp")
        self.lbNombreApp.setMinimumSize(QSize(120, 0))
        self.lbNombreApp.setMaximumSize(QSize(120, 16777215))
        self.lbNombreApp.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lbNombreApp.setTextFormat(Qt.TextFormat.AutoText)
        self.lbNombreApp.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridBarra.addWidget(self.lbNombreApp, 0, 0, 1, 1)

        self.btClose = QPushButton(self.frBarra)
        self.btClose.setObjectName(u"btClose")
        self.btClose.setMinimumSize(QSize(42, 42))
        self.btClose.setMaximumSize(QSize(42, 42))
        self.btClose.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/close.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btClose.setIcon(icon4)
        self.btClose.setIconSize(QSize(27, 30))

        self.gridBarra.addWidget(self.btClose, 0, 6, 1, 1)

        self.lbDatos = QLabel(self.frBarra)
        self.lbDatos.setObjectName(u"lbDatos")
        self.lbDatos.setMinimumSize(QSize(0, 0))
        self.lbDatos.setMaximumSize(QSize(16777215, 16777215))

        self.gridBarra.addWidget(self.lbDatos, 0, 1, 1, 1)


        self.gridCentral.addWidget(self.frBarra, 0, 0, 1, 2)

        self.frLista = QFrame(self.centralWidget)
        self.frLista.setObjectName(u"frLista")
        self.frLista.setMinimumSize(QSize(300, 0))
        self.frLista.setMaximumSize(QSize(370, 16777215))
        self.frLista.setFrameShape(QFrame.Shape.StyledPanel)
        self.frLista.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLista = QGridLayout(self.frLista)
        self.gridLista.setObjectName(u"gridLista")
        self.lnBuscar = QLineEdit(self.frLista)
        self.lnBuscar.setObjectName(u"lnBuscar")

        self.gridLista.addWidget(self.lnBuscar, 1, 0, 1, 7)

        self.btPrimero = QPushButton(self.frLista)
        self.btPrimero.setObjectName(u"btPrimero")
        self.btPrimero.setMinimumSize(QSize(30, 30))
        self.btPrimero.setMaximumSize(QSize(30, 30))
        icon5 = QIcon()
        icon5.addFile(u":/skip-up.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btPrimero.setIcon(icon5)
        self.btPrimero.setIconSize(QSize(13, 25))

        self.gridLista.addWidget(self.btPrimero, 2, 0, 1, 1)

        self.btSubir = QPushButton(self.frLista)
        self.btSubir.setObjectName(u"btSubir")
        self.btSubir.setMinimumSize(QSize(30, 30))
        self.btSubir.setMaximumSize(QSize(30, 30))
        icon6 = QIcon()
        icon6.addFile(u":/play-up.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btSubir.setIcon(icon6)
        self.btSubir.setIconSize(QSize(13, 25))

        self.gridLista.addWidget(self.btSubir, 2, 1, 1, 1)

        self.btBajar = QPushButton(self.frLista)
        self.btBajar.setObjectName(u"btBajar")
        self.btBajar.setMinimumSize(QSize(30, 30))
        self.btBajar.setMaximumSize(QSize(30, 30))
        icon7 = QIcon()
        icon7.addFile(u":/play-dow.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btBajar.setIcon(icon7)
        self.btBajar.setIconSize(QSize(13, 25))

        self.gridLista.addWidget(self.btBajar, 2, 2, 1, 1)

        self.btUltimo = QPushButton(self.frLista)
        self.btUltimo.setObjectName(u"btUltimo")
        self.btUltimo.setMinimumSize(QSize(30, 30))
        self.btUltimo.setMaximumSize(QSize(30, 30))
        icon8 = QIcon()
        icon8.addFile(u":/skip-dow.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btUltimo.setIcon(icon8)
        self.btUltimo.setIconSize(QSize(13, 25))

        self.gridLista.addWidget(self.btUltimo, 2, 3, 1, 1)

        self.btAgregar = QPushButton(self.frLista)
        self.btAgregar.setObjectName(u"btAgregar")
        self.btAgregar.setMinimumSize(QSize(0, 30))
        self.btAgregar.setMaximumSize(QSize(16777215, 30))

        self.gridLista.addWidget(self.btAgregar, 2, 4, 1, 1)

        self.btOrdenar = QPushButton(self.frLista)
        self.btOrdenar.setObjectName(u"btOrdenar")
        self.btOrdenar.setMinimumSize(QSize(0, 30))
        self.btOrdenar.setMaximumSize(QSize(16777215, 30))

        self.gridLista.addWidget(self.btOrdenar, 2, 5, 1, 1)

        self.btEliminar = QPushButton(self.frLista)
        self.btEliminar.setObjectName(u"btEliminar")
        self.btEliminar.setMinimumSize(QSize(0, 30))
        self.btEliminar.setMaximumSize(QSize(16777215, 30))

        self.gridLista.addWidget(self.btEliminar, 2, 6, 1, 1)

        self.ltLista = QListView(self.frLista)
        self.ltLista.setObjectName(u"ltLista")
        self.ltLista.setMinimumSize(QSize(0, 0))
        self.ltLista.setMaximumSize(QSize(16777215, 16777215))

        self.gridLista.addWidget(self.ltLista, 0, 0, 1, 7)


        self.gridCentral.addWidget(self.frLista, 1, 0, 1, 1)

        self.frPlayer = QFrame(self.centralWidget)
        self.frPlayer.setObjectName(u"frPlayer")
        self.frPlayer.setFrameShape(QFrame.Shape.StyledPanel)
        self.frPlayer.setFrameShadow(QFrame.Shadow.Raised)
        self.gridMarco = QGridLayout(self.frPlayer)
        self.gridMarco.setObjectName(u"gridMarco")
        self.gridPlayer = QGridLayout()
        self.gridPlayer.setObjectName(u"gridPlayer")

        self.gridMarco.addLayout(self.gridPlayer, 0, 0, 1, 1)


        self.gridCentral.addWidget(self.frPlayer, 1, 1, 1, 1)

        self.frSliders = QFrame(self.centralWidget)
        self.frSliders.setObjectName(u"frSliders")
        self.frSliders.setMinimumSize(QSize(0, 27))
        self.frSliders.setMaximumSize(QSize(16777215, 27))
        self.frSliders.setFrameShape(QFrame.Shape.StyledPanel)
        self.frSliders.setFrameShadow(QFrame.Shadow.Raised)
        self.gridSliders = QGridLayout(self.frSliders)
        self.gridSliders.setObjectName(u"gridSliders")
        self.gridSliders.setContentsMargins(0, 0, -1, 0)
        self.slVideo = QSlider(self.frSliders)
        self.slVideo.setObjectName(u"slVideo")
        self.slVideo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.slVideo.setOrientation(Qt.Orientation.Horizontal)

        self.gridSliders.addWidget(self.slVideo, 0, 0, 1, 1)

        self.btVolumen = QPushButton(self.frSliders)
        self.btVolumen.setObjectName(u"btVolumen")
        self.btVolumen.setMinimumSize(QSize(22, 22))
        self.btVolumen.setMaximumSize(QSize(22, 22))
        self.btVolumen.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon9 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.AudioVolumeMedium))
        self.btVolumen.setIcon(icon9)
        self.btVolumen.setIconSize(QSize(22, 22))
        self.btVolumen.setFlat(False)

        self.gridSliders.addWidget(self.btVolumen, 0, 1, 1, 1)

        self.slVolumen = QSlider(self.frSliders)
        self.slVolumen.setObjectName(u"slVolumen")
        self.slVolumen.setMinimumSize(QSize(120, 0))
        self.slVolumen.setMaximumSize(QSize(120, 16777215))
        self.slVolumen.setOrientation(Qt.Orientation.Horizontal)

        self.gridSliders.addWidget(self.slVolumen, 0, 2, 1, 1)


        self.gridCentral.addWidget(self.frSliders, 2, 0, 1, 2)

        self.frControles = QFrame(self.centralWidget)
        self.frControles.setObjectName(u"frControles")
        self.frControles.setMinimumSize(QSize(0, 40))
        self.frControles.setMaximumSize(QSize(16777215, 40))
        self.frControles.setFrameShape(QFrame.Shape.StyledPanel)
        self.frControles.setFrameShadow(QFrame.Shadow.Raised)
        self.gridControles = QGridLayout(self.frControles)
        self.gridControles.setObjectName(u"gridControles")
        self.gridControles.setContentsMargins(4, 0, 4, 0)
        self.btStop = QPushButton(self.frControles)
        self.btStop.setObjectName(u"btStop")
        self.btStop.setMinimumSize(QSize(35, 35))
        self.btStop.setMaximumSize(QSize(30, 35))
        self.btStop.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/stop.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btStop.setIcon(icon10)
        self.btStop.setIconSize(QSize(20, 30))

        self.gridControles.addWidget(self.btStop, 0, 2, 1, 1)

        self.lbInfoControls = QLabel(self.frControles)
        self.lbInfoControls.setObjectName(u"lbInfoControls")
        self.lbInfoControls.setMinimumSize(QSize(35, 35))
        self.lbInfoControls.setMaximumSize(QSize(16777215, 35))
        self.lbInfoControls.setIndent(7)

        self.gridControles.addWidget(self.lbInfoControls, 0, 7, 1, 1)

        self.btLista = QPushButton(self.frControles)
        self.btLista.setObjectName(u"btLista")
        self.btLista.setMinimumSize(QSize(35, 35))
        self.btLista.setMaximumSize(QSize(30, 35))
        self.btLista.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/menu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btLista.setIcon(icon11)
        self.btLista.setIconSize(QSize(20, 30))

        self.gridControles.addWidget(self.btLista, 0, 8, 1, 1)

        self.btEject = QPushButton(self.frControles)
        self.btEject.setObjectName(u"btEject")
        self.btEject.setMinimumSize(QSize(35, 35))
        self.btEject.setMaximumSize(QSize(30, 35))
        self.btEject.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/eject.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btEject.setIcon(icon12)
        self.btEject.setIconSize(QSize(20, 30))

        self.gridControles.addWidget(self.btEject, 0, 4, 1, 1)

        self.btBack = QPushButton(self.frControles)
        self.btBack.setObjectName(u"btBack")
        self.btBack.setMinimumSize(QSize(35, 35))
        self.btBack.setMaximumSize(QSize(30, 35))
        self.btBack.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u":/skip-back.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btBack.setIcon(icon13)
        self.btBack.setIconSize(QSize(20, 30))

        self.gridControles.addWidget(self.btBack, 0, 0, 1, 1)

        self.btRepeat = QPushButton(self.frControles)
        self.btRepeat.setObjectName(u"btRepeat")
        self.btRepeat.setMinimumSize(QSize(35, 35))
        self.btRepeat.setMaximumSize(QSize(30, 35))
        self.btRepeat.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon14 = QIcon()
        icon14.addFile(u":/repeat.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btRepeat.setIcon(icon14)
        self.btRepeat.setIconSize(QSize(20, 30))

        self.gridControles.addWidget(self.btRepeat, 0, 6, 1, 1)

        self.btShuffle = QPushButton(self.frControles)
        self.btShuffle.setObjectName(u"btShuffle")
        self.btShuffle.setMinimumSize(QSize(35, 35))
        self.btShuffle.setMaximumSize(QSize(30, 35))
        self.btShuffle.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon15 = QIcon()
        icon15.addFile(u":/shuffle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btShuffle.setIcon(icon15)
        self.btShuffle.setIconSize(QSize(20, 30))

        self.gridControles.addWidget(self.btShuffle, 0, 5, 1, 1)

        self.btForward = QPushButton(self.frControles)
        self.btForward.setObjectName(u"btForward")
        self.btForward.setMinimumSize(QSize(35, 35))
        self.btForward.setMaximumSize(QSize(30, 35))
        self.btForward.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon16 = QIcon()
        icon16.addFile(u":/skip-forward.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btForward.setIcon(icon16)
        self.btForward.setIconSize(QSize(20, 30))

        self.gridControles.addWidget(self.btForward, 0, 3, 1, 1)

        self.btPlay = QPushButton(self.frControles)
        self.btPlay.setObjectName(u"btPlay")
        self.btPlay.setMinimumSize(QSize(35, 35))
        self.btPlay.setMaximumSize(QSize(30, 35))
        self.btPlay.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon17 = QIcon()
        icon17.addFile(u":/play.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btPlay.setIcon(icon17)
        self.btPlay.setIconSize(QSize(22, 30))

        self.gridControles.addWidget(self.btPlay, 0, 1, 1, 1)

        self.btSetting = QPushButton(self.frControles)
        self.btSetting.setObjectName(u"btSetting")
        self.btSetting.setMinimumSize(QSize(35, 35))
        self.btSetting.setMaximumSize(QSize(30, 35))
        self.btSetting.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon18 = QIcon()
        icon18.addFile(u":/setting.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btSetting.setIcon(icon18)
        self.btSetting.setIconSize(QSize(20, 30))

        self.gridControles.addWidget(self.btSetting, 0, 9, 1, 1)


        self.gridCentral.addWidget(self.frControles, 3, 0, 1, 2)

        Player.setCentralWidget(self.centralWidget)

        self.retranslateUi(Player)

        QMetaObject.connectSlotsByName(Player)
    # setupUi

    def retranslateUi(self, Player):
        Player.setWindowTitle(QCoreApplication.translate("Player", u"MainWindow", None))
        self.btPin.setText("")
        self.btMax.setText("")
        self.btSquare.setText("")
        self.btMin.setText("")
        self.lbNombreApp.setText(QCoreApplication.translate("Player", u"Sinergia", None))
        self.btClose.setText("")
        self.lbDatos.setText(QCoreApplication.translate("Player", u"TextLabel", None))
        self.btPrimero.setText("")
        self.btSubir.setText("")
        self.btBajar.setText("")
        self.btUltimo.setText("")
        self.btAgregar.setText(QCoreApplication.translate("Player", u"A\u00f1adir", None))
        self.btOrdenar.setText(QCoreApplication.translate("Player", u"Ordenar", None))
        self.btEliminar.setText(QCoreApplication.translate("Player", u"Eliminar", None))
        self.btVolumen.setText("")
        self.btStop.setText("")
        self.lbInfoControls.setText(QCoreApplication.translate("Player", u"00:00:00/00:00:00", None))
        self.btEject.setText("")
        self.btBack.setText("")
        self.btRepeat.setText("")
        self.btShuffle.setText("")
        self.btForward.setText("")
        self.btPlay.setText("")
        self.btSetting.setText("")
    # retranslateUi

