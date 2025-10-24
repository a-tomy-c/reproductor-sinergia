from PyQt5.QtWidgets import QApplication
from src.metodos.metodos import Metodos


if __name__ == "__main__":
    ap = QApplication([])
    sg = Metodos()
    sg.show()
    ap.setStyle('Fusion')
    ap.exec()