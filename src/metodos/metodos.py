from PyQt5.QtCore import Qt, QUrl, QAbstractListModel, QPoint, QSize, QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QIcon, QPixmap, QKeySequence
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QFileDialog, QSizeGrip, QShortcut, QDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtMultimediaWidgets import QVideoWidget
from src.interfaz.sg import Ui_Sinergia
from src.interfaz.config import Ui_Config
from pathlib import Path


class Tms:
    def lista(self, fm):
        ml = 1000
        if fm < 3600*ml:
            m = int(fm/(60*ml))
            s = int((fm - m*60*ml)/ml)
            li = [m, s]
        else:
            h = int((fm/(3600*ml)))
            m = int((fm - h*3600*ml)/(60*ml))
            s = int((fm - (h*3600*ml + m*60*ml))/ml)
            li = [h, m, s]
        return li
    
    def addZero(self, li):
        m, s = li[-2], li[-1]
        if s < 10: s = '0' + str(s)
        if m < 10: m = '0' + str(m)
        c = len(li)
        if c == 3: lista = [li[-3], m, s]
        else: lista = [m, s]
        return lista
    
    def texto(self, fm):
        li = self.addZero(self.lista(int(fm)))
        if len(li) < 3: txt = '{}:{}'.format(li[0], li[1])
        else: txt = '{}:{}:{}'.format(li[0], li[1], li[2])
        return txt
    
    def buscar(self, palabra, lista):
        pal = palabra.split(" ")
        lis = []
        for p in pal:
            for i, li in enumerate(lista):
                if p.upper() in li.upper():
                    lis += [(i, li)]
        return lis
    
    
class DialogoConfig(QDialog, Ui_Config):
    def __init__(self, parent=None):
        super(DialogoConfig, self).__init__()
        self.setupUi(self)
        
    def obtenValorSalto(self):
        valor = self.sp_avance.value()
        medida = self.rd_seg.isChecked()
        return valor, medida
    

class Metodos(QMainWindow, Ui_Sinergia):
    """docstring for Metodos."""
    def __init__(self, parent = None):
        super(Metodos, self).__init__(parent)

        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        

        self.setStyleSheet(open('src/temas/estilo.css', 'r', encoding='utf-8').read())
        self.cambiaIconos()

        self.lbTitulo.setText("Sinergia ::")
        self.enBuscar.addAction(QIcon('src/img/lupa.svg'), QLineEdit.LeadingPosition)
        
        self.btClx.clicked.connect(self.close)
        self.btMax.clicked.connect(self.btMax_Clicked)
        self.btMin.clicked.connect(lambda: self.showMinimized() if not self.isMinimized() else None)

        self.frFondo.mousePressEvent = self.barra_MousePressEvent
        self.frFondo.mouseReleaseEvent = self.barra_MouseReleaseEvent
        self.frFondo.mouseMoveEvent = self.barra_MouseMoveEvent
        
        self.configPlayer() 
        self.configPlaylist()
        self.configBusqueda()
        self.dialogoConfig()
        self.lbLogo.setVisible(False)
        QSizeGrip(self.frame)
        self.barraPresionado = False
        self.lbLogo.setMinimumSize(0, 0)
        self.frControles.setMinimumSize(0,0)
        
        self.btFix.setFlat(True)
        self.btFix.setCheckable(True)
        self.btVolumen.setCheckable(True)


    def btMax_Clicked(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def barra_MousePressEvent(self, event):
        self.barraClickInicial = event.pos()
        self.barraPresionado = True
        return

    def barra_MouseReleaseEvent(self, event):
        self.barraClickInicial = QPoint(-1, -1)
        self.barraPresionado = False
        return

    def barra_MouseMoveEvent(self, event):
        if self.barraPresionado:
            pos = self.mapToGlobal(event.pos() - self.barraClickInicial)
            self.move(pos)
        return
        
    # def mousePressEvent(self, event):
        # if event.button() == Qt.LeftButton:
            # self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            # event.accept()

    # def mouseMoveEvent(self, event):
        # if event.buttons() == Qt.LeftButton:
            # self.move(event.globalPos() - self.dragPosition)
            # event.accept()
            
    def cambiaIconos(self):
        self.btUltimo.setIcon(QIcon("src/img/ultimo.svg"))
        self.btUltimo.setText("")
        self.btPrimero.setIcon(QIcon("src/img/primero.svg"))
        self.btPrimero.setText("")
        self.btBajar.setIcon(QIcon("src/img/abajo.svg"))
        self.btBajar.setText("")
        self.btSubir.setIcon(QIcon("src/img/arriba.svg"))
        self.btSubir.setText("")
        
        self.lbDuracion.setText("00:00:00")
        self.lbTranscurrido.setText("00:00:00")
        self.lbDatos.setText("")
        
    def configPlayer(self):
        self.tms = Tms()
        self.repro = QVideoWidget(self)
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.repro)
        self.reproductor.addWidget(self.repro)
        self.iniciaVl()
        # self.lbLogo.setVisible(False)
        
        # self.redimensiona()
        self.accesos()
        
        self.player.durationChanged.connect(self.obtenTime)
        self.player.positionChanged.connect(self.obtenLugar)
        self.slTiempo.sliderMoved.connect(self.actualTime)
        self.slVolumen.sliderMoved.connect(self.regulaVl)
        self.btPlay.clicked.connect(self.pausaPlay)
        self.btParar.clicked.connect(self.player.stop)
        self.btCargar.clicked.connect(self.abreArchivo)
        self.btVolumen.clicked.connect(self.silenciar)
        self.btUltimo.clicked.connect(self.irUltimo)
        self.btPrimero.clicked.connect(self.irPrimero)
        self.btBajar.clicked.connect(lambda:self.playlist.next())
        self.btSubir.clicked.connect(lambda:self.playlist.previous())
        self.btEliminar.clicked.connect(self.borraUno)
        self.btAtras.clicked.connect(lambda:self.playlist.previous())
        self.btNext.clicked.connect(lambda:self.playlist.next())
        self.btFull.clicked.connect(self.pantallaFull)
        self.btFast.clicked.connect(self.adelantarVideo)
        self.btBack.clicked.connect(self.retrasaVideo)
        self.btFix.clicked.connect(self.fijar)
        self.btLista.clicked.connect(self.listaAnim)
        
        
    def reproduce(self, url, fm=0):
        self.player.setMedia(QMediaContent(QUrl(url)))
        self.player.setPosition(int(fm))
        self.player.play()
        # self.lbLogo.setVisible(False)
        
    def cambiaIcono(self, btn, ico, tam=25):
        icono = QIcon()
        icono.addPixmap(QPixmap(ico), QIcon.Normal, QIcon.Off)                     
        btn.setIcon(icono)
        btn.setIconSize(QSize(tam, tam))          
        
    def obtenTime(self, tmp):
        self.slTiempo.setRange(0, tmp)
        self.lbDuracion.setText(self.formatTm(tmp))
    
    def obtenLugar(self, tiempo):
        self.slTiempo.setValue(tiempo)
        self.lbTranscurrido.setText(self.formatTm(tiempo))
        
    def actualTime(self, tmp):
        self.player.setPosition(tmp)
        self.lbTranscurrido.setText(self.formatTm(tmp))
        
    def pausaPlay(self):
        icono = QIcon()
        if self.player.state() == 1:
            self.player.pause()
            # icono.addPixmap(QPixmap(":/Pause.svg"), QIcon.Normal, QIcon.Off)
            self.cambiaIcono(self.btPlay, ":/Pause.svg")
        else:
            self.player.play()
            self.cambiaIcono(self.btPlay, ":/Play.svg")
            # icono.addPixmap(QPixmap(":/Play.svg"), QIcon.Normal, QIcon.Off)                     
        # self.btPlay.setIcon(icono)
        # self.btPlay.setIconSize(QSize(25, 25))  
    
    def iniciaVl(self, vol=10):
        self.player.setVolume(vol)
        self.slVolumen.setRange(0, 100)
        self.slVolumen.setValue(vol)
        
    def regulaVl(self, vol):
        self.player.setVolume(vol)
   
        
    def abreArchivo(self):
        filtro = """Videos(*.mp4 *.flv *.mov *.mkv *.avi);;
        audio (*.mp3 *.flac *.wav)"""
        file, _ = QFileDialog.getOpenFileName(self, 'Abrir archivo', '.', filtro)
        if file != '':            
            self.playlist.addMedia(QMediaContent(QUrl(file)))
            if self.player.state() == 0 :
                self.player.setPlaylist(self.playlist)
                self.reproduce(file)
                self.lbDatos.setText(Path(file).name)
            self.modelo.layoutChanged.emit()            
            
    def configPlaylist(self):
        self.playlist = QMediaPlaylist()
        self.player.setPlaylist(self.playlist)
        self.modelo = ModeloPlaylist(self.playlist)
        self.ltLista.setModel(self.modelo)
        
        self.playlist.currentIndexChanged.connect(self.cambioLista)
        
        mdSeleccion = self.ltLista.selectionModel()
        mdSeleccion.selectionChanged.connect(self.selecPlaylist)
        self.setAcceptDrops(True)
        self.iniciaSalto()
        
    def accesos(self):
        dc = {Qt.Key_F:self.pantallaFull,
              Qt.Key_Right:self.adelantarVideo,
              Qt.Key_Left:self.retrasaVideo,
              Qt.Key_Up:self.subeVolumen,
              Qt.Key_Down:self.bajaVolumen,
              Qt.Key_Space:self.pausaPlay,
              Qt.Key_Return:self.pantallaFull,
              Qt.Key_PageDown:lambda:self.playlist.next(),
              Qt.Key_PageUp:lambda:self.playlist.previous(),
              Qt.Key_Escape:self.pantallaFull}
        for c, v in dc.items():
            QShortcut(QKeySequence(c), self, v, context=Qt.ApplicationShortcut)    
        
    def cambioLista(self, i):
        if i > -1:
            ix = self.modelo.index(i)
            self.ltLista.setCurrentIndex(ix)
    
    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.acceptProposedAction()

    def dropEvent(self, e):
        i = self.playlist.mediaCount()
        for url in e.mimeData().urls():
            self.playlist.addMedia(QMediaContent(url))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
        estado = self.player.state()
        
        if estado == 0 :
            self.player.setPlaylist(self.playlist)
            self.player.setMedia(self.playlist.media(i))
            self.player.play()         
        self.modelo.layoutChanged.emit()


    def selecPlaylist(self, ix):
        i = ix.indexes()[0].row()
        self.playlist.setCurrentIndex(i)
        video = self.playlist.media(i)
        if self.player.state()==0 or self.player.state()==1:
            self.player.setMedia(video)
            self.player.play()
            self.lbDatos.setText(video.canonicalUrl().fileName())
            
    def iniciaSalto(self, s=10, mdd="seg"):
        self.salto, self.mdd = s, mdd

    def silenciar(self):
        if self.player.isMuted():
            self.player.setMuted(False)
            self.cambiaIcono(self.btVolumen, ":Speaker.svg", 19)
        else:
            self.player.setMuted(True)
            self.cambiaIcono(self.btVolumen, ":SpeakerMuted.svg", 19)
        
    def irPrimero(self):
        n = self.playlist.mediaCount()
        if n!=0: self.playlist.setCurrentIndex(0)
    
    def irUltimo(self):
        n = self.playlist.mediaCount()
        if n!=0: self.playlist.setCurrentIndex(n-1)
        
    def borraUno(self):
        i = self.playlist.currentIndex()
        n = self.playlist.mediaCount()
        self.playlist.removeMedia(i)
        # if n == 1:
            # self.player.stop()
            
    def pantallaFull(self):
        rp = self.repro
        if rp.isFullScreen():rp.setFullScreen(False)
        else:rp.setFullScreen(True)
        
    def adelantarVideo(self):
        nv, tm = self.cambiaPos()
        if tm > 0:
            limite = self.player.duration()
            if nv <= limite:self.player.setPosition(nv)
            if nv > limite:self.player.setPosition(limite)
    
    def cambiaPos(self, op='+'):
        tm, mdd = self.dconfig.obtenValorSalto()
        mdd = "seg" if mdd else "min"
        ntm = 0
        # ntm, tm, mdd = 0, self.salto, self.mdd
        pos = self.player.position()
        estado = self.player.state()
        if estado == 1 or estado == 2:
            if op == "+":
                if mdd == "seg": ntm = (pos//1000)*1000 + tm*1000
                else: ntm = pos + tm*60000
            elif op == "-":
                if mdd == "seg": ntm = (pos//1000)*1000 - tm*1000
                else: ntm = pos - tm*60000
        return ntm, tm
    
    def retrasaVideo(self):
        nv, tm = self.cambiaPos('-')
        if tm > 0:
            if nv <= 0: self.player.setPosition(0)
            else: self.player.setPosition(nv)
            
    def bajaVolumen(self):
        v = self.player.volume()
        if v > 0:
            self.player.setVolume(v-5)
            self.slVolumen.setValue(v-5)
    
    def subeVolumen(self):
        v = self.player.volume()
        if v < 100:
            self.player.setVolume(v+5)
            self.slVolumen.setValue(v+5)
            
    def fijar(self):
        if self.btFix.isChecked():std = Qt.WindowStaysOnTopHint
        else: std = Qt.Window
        self.setWindowFlags( std | Qt.FramelessWindowHint)
        self.showNormal()
        
    def configBusqueda(self):
        self.enBuscar.setClearButtonEnabled(True)
        self.enBuscar.textChanged.connect(self.busqueda)
        
    def busqueda(self):
        c = self.modelo.rowCount(self.ltLista)
        pal = self.enBuscar.text()
        if c != 0:
            conte = []
            for x in range(c):
                video = self.playlist.media(x)
                nom = video.canonicalUrl().fileName()
                conte += [nom]
            res = self.tms.buscar(pal, conte)
            oculta = []
            for x in range(c):
                if pal != '':
                    for tu in res:
                        i = tu[0]
                        if x == i:
                            oculta += [x]
                    self.ltLista.setRowHidden(x, True)
                    for ix in oculta:
                        self.ltLista.setRowHidden(ix, False)
                else:
                    self.ltLista.setRowHidden(x, False)
                    
    def listaAnim(self):
        wi = self.frLista.width()
        if wi == 0: nwi = 340
        else: nwi = 0
        self.anim = QPropertyAnimation(self.frLista, b'maximumWidth')
        self.anim.setDuration(484)
        self.anim.setStartValue(wi)
        self.anim.setEndValue(nwi)
        self.anim.setEasingCurve(QEasingCurve.InOutQuart)
        self.anim.start()
        
    def wheelEvent(self, e):
        vol = e.angleDelta().y()
        if vol > 0: self.subeVolumen()
        else: self.bajaVolumen()    
        
    def formatTm(self, ms):
        h, r = divmod(ms, 3600000)
        m, r = divmod(r, 60000)
        s, _ = divmod(r, 1000)
        return ('%d:%02d:%02d' % (h,m,s)) if h else ('%d:%02d:%02d' % (0,m,s))
    
    def dialogoConfig(self):
        self.dconfig = DialogoConfig(self)
        # self.dconfig.setStyleSheet(open('src/temas/estilo.css', 'r', encoding='utf-8').read())
        self.dconfig.rd_seg.setChecked(True)
        self.dconfig.sp_avance.setValue(10)
        self.btMenu.clicked.connect(self.abreConfig)
        
    def abreConfig(self):
        self.dconfig.exec()
    
    
    #@pyqtSlot(str)
    # def arrastrarSoltar(self, archivo):
        # if archivo != '':
            # self.player.setMedia(QMediaContent(QUrl.fromLocalFile(archivo)))
            # self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(archivo)))
            # print("22")
            # if self.player.state() == 0:
                # self.player.play()
        # self.model.layoutChanged.emit()       
        
class ModeloPlaylist(QAbstractListModel):
    def __init__(self, plista, *args, **kwargs):
        super(ModeloPlaylist, self).__init__(*args, **kwargs)
        self.plista = plista
        
    def data(self, index, rol):
        if rol == Qt.DisplayRole:
            media = self.plista.media(index.row())
            return media.canonicalUrl().fileName()
        
    def rowCount(self, index):
        return self.plista.mediaCount()
            
 

# if __name__ == "__main__":
#     ap = QApplication([])
#     mt = Metodos()
#     mt.show()
#     # mt.setStyle('Windows')
#     ap.exec()