from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap
from temporal import TemporalSkin
from sinergia_core.player import Player


class TestVentana(QWidget):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self._cnf_testventana()

    def _cnf_testventana(self):
        self.resize(600, 400)
        vly = QVBoxLayout(self)
        self.ui = TemporalSkin()
        self.ui.splitter.setSizes([3,7])
        vly.addWidget(self.ui)

        self.player = Player()
        vly_player = QVBoxLayout(self.ui.fm_player)
        vly_player.addWidget(self.player.get_widget())

        self.ui.btn_1.clicked.connect(self.test_setvideo)
        self.ui.btn_play.clicked.connect(self.player.toggle_playback)

    def test_setvideo(self):
        video1 = "/home/tomy/Vídeos/BATMETAL.mp4"
        self.player.set_media(video1)
        self.player.play()

    def closeEvent(self, event):
        self.player.stop()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    tv = TestVentana()
    tv.show()
    sys.exit(app.exec())