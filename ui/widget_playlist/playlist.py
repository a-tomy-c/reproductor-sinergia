from pathlib import Path
from random import randint
from PySide6.QtGui import QDragEnterEvent, QDropEvent
from PySide6.QtWidgets import QAbstractItemView, QListWidget, QListWidgetItem
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

    def dragEnterEvent(self, event:QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super().dragEnterEvent(event)

    def dropEvent(self, event:QDropEvent):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                media = url.toLocalFile()
                self.set_media(media)
        else:
            super().dropEvent(event)

    def _fill_items(self):
        def read_txt(txt_path:str):
            with open(txt_path, 'r') as f:
                return [l.strip('\n') for l in f.readlines() if l.strip('\n')]
        
        videos = read_txt('lista-videos.txt')
        for media in videos:
            self.set_media(media)

    def select_item(self, item:QListWidgetItem):
        return item.data(Qt.UserRole)

    def to_first_item(self):
        self.setCurrentRow(0)

    def to_last_item(self):
        self.setCurrentRow(self.count() - 1)

    def next_item(self):
        current_row = self.currentRow()
        if current_row == -1:
            self.to_first_item()
        else:
            self.setCurrentRow((current_row+1) % self.count())

    def previous_item(self):
        current_row = self.currentRow()
        if current_row == 0:
            self.to_last_item()
        else:
            self.setCurrentRow(current_row-1)
        
    def _move_item(self, i:int):
        current_row = self.currentRow()
        if current_row == -1:
            return

        new_row = current_row + i
        if not (0 <= new_row < self.count()):
            return

        item_save = self.takeItem(current_row)
        self.insertItem(new_row, item_save)
        self.setCurrentRow(new_row)

    def move_up(self):
        self._move_item(-1)

    def move_down(self):
        self._move_item(1)

    def delete_item(self):
        current_row = self.currentRow()
        if current_row != -1:
            self.takeItem(current_row)
            if self.count() > 0:
                self.setCurrentRow(min(current_row, self.count()-1))
            else:
                self.setCurrentRow(-1)

    def random_item(self):
        index = randint(0, self.count()-1)
        self.setCurrentRow(index)

    def search_item(self, text:str):
        text = text.lower()
        for index in range(self.count()):
            item = self.item(index)
            name = item.text().lower()
            b = True if text and text not in name else False
            item.setHidden(b)

