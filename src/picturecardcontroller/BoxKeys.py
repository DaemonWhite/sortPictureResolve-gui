import concurrent.futures
import multiprocessing

from gi.repository import Gtk, GdkPixbuf, Pango

from .PictureCard import PictureCard

class BoxKey(Gtk.Box):
    LEN_CARD_DEFAULLT = int(0)
    def __init__(self, key):
        super().__init__(
            halign=Gtk.Align.FILL,
            valign=Gtk.Align.FILL,
            vexpand=True,
            hexpand=True,
            orientation=Gtk.Orientation.VERTICAL,
            visible=False
        )
        self.__core = multiprocessing.cpu_count()
        self.__len_card = self.LEN_CARD_DEFAULLT
        self.__key = key

        self.__path = ""
        self.__pictures = list()

        self.__title = Gtk.Box()
        self.__title.set_vexpand(True)
        self.__title.set_hexpand(True)
        self.__title.add_css_class("card")
        self.__title.add_css_class("title-1")


        self.__flow_box = Gtk.FlowBox()

        self.__label_tiltle = Gtk.Label()
        self.__label_tiltle.set_vexpand(True)
        self.__label_tiltle.set_hexpand(True)
        self.__label_tiltle.set_halign(Gtk.Align.FILL)
        self.__label_tiltle.set_valign(Gtk.Align.FILL)
        self.__label_tiltle.set_label(key)
        self.__title.append(self.__label_tiltle)
        self.__list_pc = list()
        self.append(self.__title)
        self.append(self.__flow_box)

    def get_key(self):
        return self.__key

    def get_len_card(self):
        return self.__len_card

    def thread_generate_card(self, step_list):

        for i in range(step_list[0], step_list[1]):
            pc = PictureCard(self.__path, self.__pictures[i])
            self.__list_pc.append(pc)
            self.__len_card += 1

    def place_card(self):
        for pc in self.__list_pc:
            self.__flow_box.append(pc)



    def generate_card(self, pictures, path):
        self.__path = path
        self.__pictures = pictures
        index = 0
        OFFSET = 1
        len_pictures = len(pictures)
        len_step_picture = int(len_pictures/self.__core)

        tasks = list()
        tasks_step_tmp = [0,1]
        for i in range(0, len_step_picture):
            tasks_step_tmp[0] = len_step_picture * index
            index+=1
            tasks_step_tmp[1] = len_step_picture * index - OFFSET
            tasks.append(tasks_step_tmp.copy())

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.__core) as pool:
            pool.map(self.thread_generate_card, tasks)
        print("Generation place")
        self.place_card()
        print("place Gerated")
        del self.__list_pc
        del self.__pictures