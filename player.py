from PySide6.QtWidgets import QApplication, QStyleFactory
from app.pl_metodos import PlMetodos

import sys

if __name__ == "__main__":
    app = QApplication([])
    sr = PlMetodos()
    sr.show()

    # Obtener la lista de nombres de estilos disponibles
    # estilos_disponibles = QStyleFactory.keys()

    # print("Estilos disponibles en este sistema:")
    # print(estilos_disponibles)
    # ['windows11', 'windowsvista', 'Windows', 'Fusion']

    app.setStyle('windows11')
    app.exec()