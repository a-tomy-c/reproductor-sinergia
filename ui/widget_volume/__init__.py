from PySide6.QtWidgets import QPushButton, QWidget
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from ui.widget_volume.ui_widget_volume import Ui_WidgetVolume
import ui.icons_sinergia


class WidgetVolume(QWidget, Ui_WidgetVolume):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.setupUi(self)
        self.__cnf_WidgetVolume()

    def __cnf_WidgetVolume(self):
        self.resize(400, 600)
        self._VOLUME = 0
        self.cnf_btn(self.btn_volume, 'sound-off')
        self.sld_volume.sliderMoved.connect(self._move_sld)
        self.init_volume(45)
        self.btn_volume.toggled.connect(self._mute)
        
    def cnf_btn(self, btn:QPushButton, icon_name:str, text:str='', w:int=None, szi:int=20):
        btn.setIconSize(QSize(szi, szi))
        btn.setIcon(QIcon(f':/a/{icon_name}.svg'))
        btn.setText(text)
        if w:
            btn.setMinimumWidth(w)
            btn.setMaximumWidth(w)

    def _move_sld(self, value:int, set_var:bool=True):
        if value > 50: name = 'sound-2'
        elif value > 10: name = 'sound-1'
        elif value > 0: name = 'sound-0'
        else: name = 'sound-off'
        
        self.lb_volume.setText(str(value))
        self.cnf_btn(self.btn_volume, name)
        if set_var:
            self._VOLUME = value

    def init_volume(self, value:int):
        self.sld_volume.setValue(value)
        self._move_sld(value)

    def set_muted(self, mute:bool=True):
        value = 0 if mute else self._VOLUME
        self._move_sld(value, set_var=False)
        self.sld_volume.setValue(value)

    def _mute(self, state:bool):
        self.set_muted(state)
          
