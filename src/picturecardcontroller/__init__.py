from .PictureCard import PictureCard

#TODO Support des erreur

#TODO Reset liste

#TODO Changer la vue
class PictureCardController(object):
    LEN_CARD_DEFAULLT = int(0)
    def __init__(self, window):
        self.__window = window
        self.__len_card = self.LEN_CARD_DEFAULLT
        self.__config = dict()
        self.__main_path = str()

    def set_path(self, path):
        self.__main_path = path

    def set_config(self, config: dict):
        self.__config = config.copy()

    def reset(self):
        print(self.__len_card)
        for pc in range(self.LEN_CARD_DEFAULLT, self.__len_card):
            child = self.__window.flow_picture_box.get_child_at_index(0)
            print(child)
            self.__window.flow_picture_box.remove(child)
        self.__len_card = self.LEN_CARD_DEFAULLT



    def generate_card(self):
        for key in self.__config:
            for picture in self.__config[key]:
                try:
                    pc = PictureCard(self.__main_path, picture)
                    self.__window.flow_picture_box.append(pc)
                    self.__len_card += 1
                except:
                    print('Image non reconue')
                print(self.__len_card)



