from PySide6.QtWidgets import QApplication, QStyleFactory
from app import PlayerSinergia


if __name__ == "__main__":
    app = QApplication([])
    sr = PlayerSinergia()
    sr.show()
    sr.setMedia(file='/home/tomy/Vídeos/ARCADEA - Exodus of Gravity (Official Visualizer).mp4')

    # Obtener la lista de nombres de estilos disponibles
    # estilos_disponibles = QStyleFactory.keys()

    # print("Estilos disponibles en este sistema:")
    # print(estilos_disponibles)
    # ['windows11', 'windowsvista', 'Windows', 'Fusion']

    app.setStyle('windows11')
    app.exec()
