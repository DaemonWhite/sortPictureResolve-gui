from gi.repository import Gtk

#TODO Ajouter une fonction de trie dans FlowBox

class PictureCard(Gtk.FlowBoxChild):
    __gtype_name__ = 'PictureCard'
    default_width = 180
    default_heigth = 180
    main_input = str()

    def __init__(self, path):
        super().__init__(halign=Gtk.Align.CENTER, valign=Gtk.Align.CENTER)
        self.__picture = Gtk.Picture()
        self.__picture.set_can_shrink(False)
        self.__picture.new_for_paintable()

    def set_default_with(self, width):
        self.default_width = width

    def set_default_heigth(self, height):
        self.default_heigth

    def set_main_input(self, path):
        self.main_input = path



