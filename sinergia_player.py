from PySide6.QtWidgets import QApplication, QHBoxLayout, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QResizeEvent
from shiboken6.Shiboken import delete
from widget_frameless import WidgetFrameless
from ui.widget_player import WidgetPlayer
from ui.widget_buttons_bar import WidgetButtonsBar
from ui.widget_playlist import WidgetPlaylist


class SinergiaPlayer(WidgetFrameless):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.__cnf_SinergiaPlayer()

    def __cnf_SinergiaPlayer(self):
        # self.resize(600, 430)
        # self.resize(900, 410)
        self.resize(800, 410)
        # self.fr_status_bar.setHidden(True)
        self.hly_body = QHBoxLayout(self)
        self.vly_body.addLayout(self.hly_body)
        self.wgp = WidgetPlayer()
        self.hly_body.addWidget(self.wgp)

        self.bbar = WidgetButtonsBar()
        self.hly_sb_mid.addWidget(self.bbar)
        self.fr_status_bar.setMaximumHeight(32)
        self.fr_status_bar.setMinimumHeight(32)
        self.fr_statusbar_left.setHidden(True)
        self.fr_statusbar_right.setHidden(True)
        self.hly_status_bar.removeItem(self.horizontalSpacer_sb0)
        self.hly_status_bar.removeItem(self.horizontalSpacer_sb1)
        self.lb_statusbar_left.setHidden(True)
        self.lb_statusbar_right.setHidden(True)
        # self.sw.setStyleSheet('background:blue;')
        # w = self.wgp.player.get_widget()
        # w.setStyleSheet('background:red;')
        self.wp = WidgetPlaylist()
        self.vly_right.addWidget(self.wp)
        # self.fr_right.setMinimumWidth(300)
        # self.fr_right.setMaximumWidth(300)
        self.fr_left.setHidden(True)
        
        self._test_set_video()
        self.bbar.btn_toggle_playlist.toggled.connect(self.toggle_playlist)

    def _test_set_video(self):
        v1 = "/home/tomy/Vídeos/Marea - Con la camisa rotaTrasegando (Directo).mp4"
        self.wgp.player.set_media(v1)
        self.bbar.btn_play.clicked.connect(self.wgp.player.play)
        self.bbar.btn_stop.clicked.connect(self.wgp.player.stop)

    def toggle_playlist(self, show:bool):
        # self.wgp.toggle_playlist(show)
        # self.wp.setHidden(show)
        gm = self.fr_right.geometry()
        w = 800 - gm.width()
        self.fr_right.setHidden(show)
        geo = self.geometry()
        h = geo.height()
        if show:
            self.resize(w, h)
        else:
            self.resize(w+gm.width(), h)
        
    def resizeEvent(self, event:QResizeEvent):
        self.updateGeometry()
