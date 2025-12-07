import sys
from PySide6.QtWidgets import QApplication
# from ui.widget_playlist import WidgetPlaylist
from ui.widget_volume import WidgetVolume


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # TEST PLAYLIST
    # playlist = WidgetPlaylist()
    # playlist.show()

    # TEST VOLUME
    wvol = WidgetVolume()
    wvol.show()
    sys.exit(app.exec())
