from PySide6.QtWidgets import QApplication, QPushButton, QSplitter, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from ui.widget_player.ui_widget_player import Ui_WidgetPlayer
from ui.widget_time import WidgetTime
from ui.widget_volume import WidgetVolume
from ui.widget_buttons_bar import WidgetButtonsBar
from sinergia_core.player import Player
from ui.widget_playlist import WidgetPlaylist


class WidgetPlayer(QWidget, Ui_WidgetPlayer):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.setupUi(self)
        self.__cnf_WidgetPlayer()

    def __cnf_WidgetPlayer(self):
        self.resize(750, 350)
        self.wg_time = WidgetTime()
        self.wg_vol = WidgetVolume()
        self.fr_top.setMaximumHeight(32)
        self.hly_n.addWidget(self.wg_time)
        self.hly_n.addWidget(self.wg_vol)

        self.fr_bot.setMaximumHeight(32)
        self.bbar = WidgetButtonsBar(self.fr_s)
        self.hly_s.addWidget(self.bbar)

        self.split = QSplitter(orientation=Qt.Orientation.Horizontal)
        self.player = Player()
        self.playlist = WidgetPlaylist()
        self.split.addWidget(self.playlist)
        self.split.addWidget(self.player.get_widget())
        self.hly_center.addWidget(self.split)

        self.bbar.btn_toggle_playlist.toggled.connect(self.toggle_playlist)

    def toggle_playlist(self, show:bool):
        self.playlist.setHidden(show)
        

