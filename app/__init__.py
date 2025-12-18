from app.pl_metodos import PlMetodos
from app.sinergia_core import SinergiaCore



class PlayerSinergia(PlMetodos):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.__cnf_SinergiaCore()

    def __cnf_SinergiaCore(self):
        self._init_player()
        self.btPlay.clicked.connect(self.player.togglePlayback)
        self.btStop.clicked.connect(self.player.stop)
        self.slVolumen.sliderMoved.connect(self.player.setVolume)
        self.btBack.clicked.connect(self.player.backward)
        self.btForward.clicked.connect(self.player.fordward)
        self.btLista.clicked.connect(self.togglePlaylist)
        
        self.reloadConfig()

    def _init_player(self):
        self.player = SinergiaCore()
        self.gridPlayer.addWidget(self.player.getWidget())
        self.frLista.setMinimumWidth(0)
        self.gridCentral.setColumnStretch(0, 4)
        self.gridCentral.setColumnStretch(1, 6)

    def setVolume(self, value:int):
        self.player.setVolume(value)
        self.slVolumen.setValue(value)

    def reloadConfig(self):
        self.setVolume(60)

    def closeEvent(self, _):
        self.player.stop()

    def showPlaylist(self, show:bool=True):
        self.frLista.setHidden(not show)

    def togglePlaylist(self):
        show = True if self.frLista.isHidden() else False
        self.lbDatos.setText(str(show))
        self.showPlaylist(show)

    def setMedia(self, file:str):
        """asigna un archivo"""
        self.player.setMedia(file)

