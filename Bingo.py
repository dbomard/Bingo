import sys

from PyQt5.QtWidgets import QGridLayout, QLabel, QApplication, QWidget, QLineEdit, QSpinBox
from bingo_map import BingoMap


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.__cter_latitude = 48.858333  # latitude du centre de la carte
        self.__cter_longitude = 2.294444  # longitude du centre de la carte
        self.__zoom = 15

        # Zone de saisie de la latitude
        lbl_latitude = QLabel(self)
        lbl_latitude.setText('Latitude :')
        le_latitude = QLineEdit(self)
        le_latitude.setText(str(self.__cter_latitude))

        # Zone de saisie de la longitude
        lbl_longitude = QLabel(self)
        lbl_longitude.setText('Longitude :')
        le_longitude = QLineEdit(self)
        le_longitude.setText(str(self.__cter_longitude))

        # Saisie du zoom
        lbl_zoom = QLabel(self)
        lbl_zoom.setText('Zoom :')
        sb_zoom = QSpinBox(self)
        sb_zoom.setRange(1, 23)
        sb_zoom.setValue(self.__zoom)



        # zone où sera dessinée la carte
        lbl_map = QLabel(self)
        lbl_map.setMinimumWidth(256)
        lbl_map.setMinimumHeight(256)

        # Création du layout
        grid = QGridLayout()
        grid.setSpacing(5)
        grid.setColumnMinimumWidth(1, 80)
        grid.setColumnStretch(1,0)
        grid.setColumnMinimumWidth(2,256)
        grid.setColumnStretch(2,100)

        grid.addWidget(lbl_latitude,0,0)
        grid.addWidget(le_latitude, 0, 1)
        grid.addWidget(lbl_longitude,1,0)
        grid.addWidget(le_longitude, 1, 1)
        grid.addWidget(lbl_zoom,2,0)
        grid.addWidget(sb_zoom, 2, 1)
        grid.addWidget(lbl_map,0,2,10,5)

        self.setLayout(grid)

        self.map_zone = BingoMap((self.__cter_latitude, self.__cter_longitude), self.__zoom)
        self.map_zone.begin(lbl_map)
        self.map_zone.draw_map()
        self.map_zone.end()

        self.setGeometry(300, 300, 640, 480)
        self.setWindowTitle('Bingo')
        self.show()

    def paintEvent(self, event):
            self.map_zone.begin(self)
            self.map_zone.draw_map()
            self.map_zone.end()


def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
