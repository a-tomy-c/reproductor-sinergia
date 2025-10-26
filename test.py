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
        self.volume_initial(80)
        vly_player = QVBoxLayout(self.ui.fm_player)
        vly_player.addWidget(self.player.get_widget())

        self.ui.btn_1.clicked.connect(self.test_setvideo)
        self.ui.btn_play.clicked.connect(self.player.toggle_playback)
        self.ui.btn_stop.clicked.connect(self.player.stop)
        self.player.durationChanged.connect(self._update_duration)
        self.player.positionChanged.connect(self._update_position)
        self.ui.sld_time.sliderMoved.connect(self.player.setPosition)
        self.ui.sld_volume.sliderMoved.connect(self._set_volume)

    def test_setvideo(self):
        video1 = "/home/tomy/Vídeos/BATMETAL.mp4"
        self.player.set_media(video1)
        self.player.play()

    def _update_duration(self, duration:int):
        ts = self.player.msec_to_ts(duration)
        self.ui.lb_info.setText(f'[DURACION] {duration}|{ts}')
        self.ui.sld_time.setRange(0, duration)

    def _update_position(self, position:int):
        self.ui.sld_time.setValue(position)
        self.ui.lb_time.setText(self.player.msec_to_ts(position))

    def closeEvent(self, event):
        self.player.stop()

    def volume_initial(self, volume:int):
        self.ui.sld_volume.setValue(volume)
        self._set_volume(value=volume)

    def _set_volume(self, value:int):
        self.player.set_volume(value)
        self.ui.lb_volume.setText(str(value))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    tv = TestVentana()
    tv.show()
    sys.exit(app.exec())