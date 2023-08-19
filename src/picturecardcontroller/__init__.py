from .BoxKeys import BoxKey
import time
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

        self.__time_generation = 0

        self.__list_box_key = dict()

    def set_path(self, path):
        self.__main_path = path

    def set_config(self, config: dict):
        self.__config = config.copy()

    def reset(self):
        for key in self.__list_box_key:
            self.__list_box_key[key].destroy()


        # print(self.__len_card)
        # for pc in range(self.LEN_CARD_DEFAULLT, self.__len_card):
        #     child = self.__window.flow_picture_box.get_child_at_index(0)
        #     print(child)
        #     self.__window.flow_picture_box.remove(child)
        # self.__len_card = self.LEN_CARD_DEFAULLT

    def generate(self):
        self.__time_generation = time.perf_counter()
        for key in self.__config:
            box_title = self.generate_box_key(key)

        self.__time_generation = time.perf_counter() - self.__time_generation
        print("temps d'execution", self.__time_generation)

    def visible_all_card(self):
        for key in self.__list_box_key:
            self.visible_card(key)

    def hiding_all_card(self):
        for key in self.__list_box_key:
            self.hiding_card(key)

    def visible_card(self, key):
        self.__list_box_key[key].set_visible(True)

    def hiding_card(self, key):
        self.__list_box_key[key].set_visible(False)

    def generate_box_key(self, key):
        self.__list_box_key[key] = BoxKey(key)
        self.__window.main_box.append(self.__list_box_key[key])
        self.__list_box_key[key].generate_card(self.__config[key].copy(), self.__main_path)


