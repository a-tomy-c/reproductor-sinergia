from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon
from ui.widget_buttons_bar.ui_widget_buttons_bar import Ui_WidgetButtonsBar


class WidgetButtonsBar(QWidget, Ui_WidgetButtonsBar):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.setupUi(self)
        self.__cnf_WidgetButtonsBar()

    def __cnf_WidgetButtonsBar(self):
        # self.resize(400, 600)
        self._cnf_btn(self.btn_toggle_playlist, 'view-list')
        self._cnf_btn(self.btn_fullscreen, 'full-screen')
        self._cnf_btn(self.btn_play, 'play')
        self._cnf_btn(self.btn_stop, 'maximize')
        self._cnf_btn(self.btn_backward, 'backward', szi=28)
        self._cnf_btn(self.btn_forward, 'forward', szi=28)
        self._cnf_btn(self.btn_previous, 'prev')
        self._cnf_btn(self.btn_next, 'next')

    def _cnf_btn(self, btn:QPushButton, icon_name:str, text:str='', w:int=None, szi:int=20):
        btn.setIconSize(QSize(szi, szi))
        btn.setIcon(QIcon(f':/a/{icon_name}.svg'))
        btn.setText(text)
        if w:
            btn.setMinimumWidth(w)
            btn.setMaximumWidth(w)
        


