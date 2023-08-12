import os
from gi.repository import Gtk, GdkPixbuf, Pango

#TODO Ajouter une fonction de trie dans FlowBox

#TODO Ajout du support des gif

class PictureCard(Gtk.FlowBoxChild):
    __gtype_name__ = 'PictureCard'
    default_width = 180
    default_heigth = 180
    max_length = 20
    main_input = str()

    def __init__(self, path, name):
        super().__init__(halign=Gtk.Align.CENTER, valign=Gtk.Align.CENTER)
        self.main_input = os.path.join(path, name)
        self.__box = Gtk.Box()
        self.__box.add_css_class("picture-card-box")
        self.__box.set_orientation(Gtk.Orientation.VERTICAL)
        self.__label = Gtk.Label()
        self.__label.add_css_class("te")
        self.__label.set_label(name)
        self.__label.set_lines(1)
        self.__label.set_wrap(True)
        self.__label.set_max_width_chars(0)
        self.__label.set_ellipsize(Pango.EllipsizeMode.MIDDLE)
        print(self.main_input)
        self.__pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(self.main_input, self.default_width, self.default_heigth)
        self.__picture = Gtk.Picture.new_for_pixbuf(self.__pixbuf)
        self.__picture.set_can_shrink(False)

        self.__box.append(self.__picture)
        self.__box.append(self.__label)
        self.set_child(self.__box)

    def limit_char_name(self, name):
        return  name[:self.max_length - 3]

    def set_default_with(self, width):
        self.default_width = width

    def set_default_heigth(self, height):
        self.default_heigth

    def set_main_input(self, path):
        self.main_input = path



