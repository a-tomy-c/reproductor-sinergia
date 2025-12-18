from PySide6.QtWidgets import QMainWindow, QApplication, QMenu, QPushButton
from PySide6.QtCore import QTimer, Qt, QSize, QPoint 
from PySide6.QtGui import QAction, QCursor, QIcon, QScreen, QMouseEvent

from ui.ui_player import Ui_Player


class PlMetodos(QMainWindow, Ui_Player):
    """docstring for PlMetodos."""
    def __init__(self, parent = None):
        super().__init__(parent)


        self.setupUi(self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        # --- Atributos para el movimiento de la ventana sin marco ---
        self.old_pos = QPoint() # Almacena la posición anterior del ratón
        self.dragging = False   # Bandera para saber si estamos arrastrando la ventana

        self.icon_max = QIcon()
        self.icon_max.addFile(u":/maximize.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.icon_min = QIcon()
        self.icon_min.addFile(u":/minmax.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.btMax.clicked.connect(self.btMaxMin)
        self.btSquare.clicked.connect(self.toggleFullScreen)
        self.btClose.clicked.connect(self.close)
        self.btMin.clicked.connect(lambda: self.showMinimized() if not self.isMinimized() else None)

    # --- Métodos para el movimiento de la ventana sin marco ---
    def mousePressEvent(self, event: QMouseEvent):
        """
        Maneja el evento cuando se presiona un botón del ratón.
        Registra la posición inicial si es el clic izquierdo para iniciar el arrastre.
        """
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragging = True
            # Guarda la posición global (coordenadas de pantalla) del ratón
            self.old_pos = event.globalPosition().toPoint()
            event.accept() # Indica que el evento ha sido manejado
        else:
            super().mousePressEvent(event) # Llama a la implementación base para otros botones

    def mouseMoveEvent(self, event: QMouseEvent):
        """
        Maneja el evento cuando el ratón se mueve.
        Si estamos arrastrando, actualiza la posición de la ventana en función del movimiento del ratón.
        """
        if self.dragging:
            # Calcula el delta (cambio) desde la posición anterior del ratón
            delta_pos = event.globalPosition().toPoint() - self.old_pos
            
            # Mueve la ventana por el mismo delta
            self.move(self.pos() + delta_pos)
            
            # Actualiza la posición anterior del ratón para el siguiente cálculo de movimiento
            self.old_pos = event.globalPosition().toPoint()
            event.accept()
        else:
            super().mouseMoveEvent(event) # Llama a la implementación base si no estamos arrastrando

    def mouseReleaseEvent(self, event: QMouseEvent):
        """
        Maneja el evento cuando se suelta un botón del ratón.
        Detiene el arrastre si fue el clic izquierdo.
        """
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragging = False
            event.accept()
        else:
            super().mouseReleaseEvent(event)
    # --- Fin de métodos de movimiento ---

    def centerWindow(self):
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())

    def btMaxMin(self):
        if self.isMaximized():
            self.showNormal()
            self.btMax.setIcon(self.icon_max)
        else:
            self.showMaximized()
            self.btMax.setIcon(self.icon_min)

    def toggleFullScreen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()


