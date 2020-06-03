import sys

from PyQt5.QtWidgets import QLabel, QApplication, QWidget, QLineEdit, QSpinBox

import bingo_map


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.__cter_latitude = 48.858333  # latitude du centre de la carte
        self.__cter_longitude = 2.294444  # longitude du centre de la carte
        self.__zoom = 15

        # Création des zones de saisies de la latitude et de la longitude et du zoom

        self.label_latitude = QLabel(self)
        self.label_longitude = QLabel(self)
        self.label_zoom = QLabel(self)
        self.linedit_latitude = QLineEdit(self)
        self.linedit_longitude = QLineEdit(self)
        self.spinbox_zoom = QSpinBox(self)
        self.spinbox_zoom.setValue(self.__zoom)

        self.linedit_latitude.setText(str(self.__cter_latitude))
        self.linedit_longitude.setText(str(self.__cter_longitude))
        self.spinbox_zoom.setRange(1, 23)
        self.label_latitude.setText('Latitude :')
        self.label_longitude.setText('Longitude :')
        self.label_zoom.setText('Zoom :')

        self.label_latitude.setGeometry(10, 10, 50, 20)
        self.linedit_latitude.setGeometry(60, 10, 80, 20)
        self.label_longitude.setGeometry(10, 40, 50, 20)
        self.linedit_longitude.setGeometry(60, 40, 80, 20)
        self.label_zoom.setGeometry(10, 70, 50, 20)
        self.spinbox_zoom.setGeometry(60, 70, 40, 20)

        # Zone de dessin de la carte:
        self.label_map = QLabel(self)
        self.label_map.setGeometry(150, 10, 256, 256)
        self.buffer_map = bingo_map.BingoMap((self.__cter_latitude, self.__cter_longitude), self.__zoom)
        self.label_map.setPixmap(self.buffer_map.update_buffer())
        # TODO : Create a function to draw the map

        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('Bingo')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
