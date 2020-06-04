from PyQt5.QtGui import QPixmap
import dataserver
import urllib.request
from PyQt5.QtGui import QPainter


class BingoMap(QPainter):

    def __init__(self, coordonnees, zoom):
        super().__init__()
        self.__latitude = coordonnees[0]
        self.__longitude = coordonnees[1]
        self.__zoom = zoom
        self.__buffer = QPixmap()
        self.__server = dataserver.DataServer('aerial')

    def get_zoom(self):
        return self.__zoom

    def get_coordonnees(self):
        return self.__latitude, self.__longitude

    def set_zoom(self, zoom):
        self.__zoom = zoom

    def set_coordonnees(self, coo):
        self.__latitude = coo[0]
        self.__longitude = coo[1]

    def update_buffer(self):
        url = self.__server.get_image_url((self.__latitude, self.__longitude), self.__zoom)
        image = urllib.request.urlopen(url).read()
        self.__buffer.loadFromData(image)


    def draw_map(self):
        self.update_buffer()
        self.drawPoint(10,10)

