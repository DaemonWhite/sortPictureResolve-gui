import os

from .PictureCard import PictureCard

class PictureCardController(object):

    def __init__(self, window):
        self.__window = window
        self.__card = list()
        self.__config = dict()
        self.__main_path = str()

    def set_path(self, path):
        self.__main_path = path

    def set_config(self, config: dict):
        self.__config = config.copy()

    def generate_card(self):
        for key in self.__config:
            path = os.path.join(self.__main_path, self.config)
            pc = PictureCard()
            self.__window.flow_picture_box.append(pc)

