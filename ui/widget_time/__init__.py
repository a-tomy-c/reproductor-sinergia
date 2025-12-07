from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from ui.widget_time.ui_widget_time import Ui_WidgetTime


class WidgetTime(QWidget, Ui_WidgetTime):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.setupUi(self)
        self.__cnf_WidgetTime()

    def __cnf_WidgetTime(self):
        # self.resize(400, 600)
        ...
        

