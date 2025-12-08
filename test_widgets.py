import sys
from PySide6.QtWidgets import QApplication
# from ui.widget_playlist import WidgetPlaylist
# from ui.widget_volume import WidgetVolume
# from ui.widget_time import WidgetTime
# from ui.widget_buttons_bar import WidgetButtonsBar
# from ui.widget_player import WidgetPlayer
from sinergia_player import SinergiaPlayer


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # TEST PLAYLIST
    # playlist = WidgetPlaylist()
    # playlist.show()

    # TEST VOLUME
    # wvol = WidgetVolume()
    # wvol.show()

    # TEST TIME
    # wtime = WidgetTime()
    # wtime.show()

    # TEST BUTTONS BAR
    # wbbar = WidgetButtonsBar()
    # wbbar.show()

    # TEST PLAYER
    # wplayer = WidgetPlayer()
    # wplayer.show()

    # TEST SINERGIA PLAYER
    splayer = SinergiaPlayer()
    splayer.show()
    
    sys.exit(app.exec())
