from PySide6.QtWidgets import QWidget, QLineEdit
from PySide6.QtGui import QIcon
from ui.widget_playlist.ui_playlist import Ui_Playlist
from ui.widget_playlist.playlist import Playlist
import ui.icons_sinergia


class WidgetPlaylist(QWidget, Ui_Playlist):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.setupUi(self)
        self.__cnf_WidgetPlaylist()

    def __cnf_WidgetPlaylist(self):
        self.resize(400, 460)
        self.playlist = Playlist()
        self.vly_playlist.addWidget(self.playlist)

        self.btn_up.clicked.connect(self.playlist.previous_item)
        self.btn_down.clicked.connect(self.playlist.next_item)
        self.btn_move_up.clicked.connect(self.playlist.move_up)
        self.btn_move_down.clicked.connect(self.playlist.move_down)
        self.btn_delete.clicked.connect(self.playlist.delete_item)
        self.le_search.textChanged.connect(self.search_item)
        self.le_search.addAction(QIcon(':/a/search.svg'), QLineEdit.LeadingPosition)

    def search_item(self, text:str):
        self.playlist.search_item(text)
