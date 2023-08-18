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
        self.__len_card = self.LEN_CARD_DEFAULLT
        self.__key = key

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
        self.append(self.__title)
        self.append(self.__flow_box)

    def get_key(self):
        return self.__key

    def generate_card(self, config, path):
        for picture in config:
            try:
                pc = PictureCard(path, picture)
                self.__flow_box.prepend(pc)
                self.__len_card += 1
            except:
                print("Image non reconue")






