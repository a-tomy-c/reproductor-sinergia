from ast import Try
from pathlib import Path
from PySide6.QtGui import QDragEnterEvent, QDropEvent
from PySide6.QtWidgets import QAbstractItemView, QWidget, QApplication, QListWidget, QListWidgetItem, QPushButton, QVBoxLayout, QHBoxLayout, QFrame
from PySide6.QtCore import Qt


class Playlist(QListWidget):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.__cnf_WidgetPlaylist()

    def __cnf_WidgetPlaylist(self):
        self.resize(400, 450)
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDragDropMode(QAbstractItemView.InternalMove)

        # TEST
        self._fill_items()
        self.itemDoubleClicked.connect(self.select_item)

    def set_media(self, media_path:str):
        """asignar un archivo de video"""
        name = Path(media_path).name
        item = QListWidgetItem(name)
        item.setData(Qt.UserRole, Path(media_path).as_posix())
        self.addItem(item)

    #def dragEnterEvent(self, event:QDragEnterEvent):
    #    if event.mimeData().hasUrls():
    #        event.acceptProposedAction()
#
#    def dropEvent(self, event:QDropEvent):
#        for url in event.mimeData().urls():
#            media = url.toLocalFile()
#            self.set_media(media)

    def dragEnterEvent(self, event:QDragEnterEvent):
        if event.mimeData().hasUrls():
            # Si son archivos externos, aceptar
            event.acceptProposedAction()
        else:
            # Si es arrastre interno, dejar que QListWidget lo maneje
            super().dragEnterEvent(event)

    def dropEvent(self, event:QDropEvent):
        if event.mimeData().hasUrls():
            # Si son archivos externos, procesarlos
            for url in event.mimeData().urls():
                media = url.toLocalFile()
                self.set_media(media)
        else:
            # Si es arrastre interno, dejar que QListWidget lo maneje
            super().dropEvent(event)

    def _fill_items(self):
        def read_txt(txt_path:str):
            with open(txt_path, 'r') as f:
                return [l.strip('\n') for l in f.readlines() if l.strip('\n')]
        
        videos = read_txt('lista-videos.txt')
        for media in videos:
            self.set_media(media)

    def select_item(self, item:QListWidgetItem):
        data = item.data(Qt.UserRole)
        print(data)


class WidgetPlaylist(QWidget):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.__cnf_WidgetPlaylist()

    def __cnf_WidgetPlaylist(self):
        self.resize(400, 450)
        self.playlist = Playlist()
        self.__set_widgets()
        self.setAcceptDrops(True)

        self.btn_first.clicked.connect(self.to_first_item)
        self.btn_last.clicked.connect(self.to_last_item)

    def __set_widgets(self):
        fm_btn = QFrame()
        vly = QVBoxLayout(self)
        vly.addWidget(self.playlist)
        vly.addWidget(fm_btn)

        self.btn_down = QPushButton("UP")
        self.btn_up = QPushButton("DW")
        self.btn_first = QPushButton("Fi")
        self.btn_last = QPushButton("Li")
        self.btn_delete = QPushButton("D")
        hly = QHBoxLayout(fm_btn)
        hly.addWidget(self.btn_down)
        hly.addWidget(self.btn_up)
        hly.addWidget(self.btn_first)
        hly.addWidget(self.btn_last)
        hly.addWidget(self.btn_delete)
        
    def to_first_item(self):
        self.playlist.setCurrentRow(0)

    def to_last_item(self):
        self.playlist.setCurrentRow(self.playlist.count() - 1)



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    # playlist = Playlist()
    # playlist.show()
    wp = WidgetPlaylist()
    wp.show()
    
    sys.exit(app.exec())
