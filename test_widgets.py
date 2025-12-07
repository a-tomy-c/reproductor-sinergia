import sys
from PySide6.QtWidgets import QApplication, QWidget
from ui.widget_playlist import WidgetPlaylist

if __name__ == "__main__":
    app = QApplication(sys.argv)
    playlist = WidgetPlaylist()
    playlist.show()
    sys.exit(app.exec())
