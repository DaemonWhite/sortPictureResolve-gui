from gi.repository import Adw, Gtk, GLib

from drawratiocontroller import DrawRatioController

class RatioWindow(Gtk.Box):
    __gtype_name__ = "RatioWindow"

    draw_area = Gtk.Template.Child("draw_area")

    def __init__(self, close_callback, window):
        super().__init__(
            orientation=Gtk.Orientation.VERTICAL
        )
        self.__window = window

        self.__close_callback = close_callback
        self.__main_box = Gtk.Box()
        self.__tool_box = Gtk.Box()
        self.__tool_box.append(Gtk.Label(label="tu es beau"))
        self.__header_bar = Adw.HeaderBar()
        self.__close_button = Gtk.Button()

        self.__draw_area = DrawRatioController()
        self.__draw_area.set_vexpand(True)
        self.__draw_area.set_hexpand(True)

        self.__draw_area.set_draw_func(self.__draw_area.draw, None)

        coefficients = self.__window.get_all_coefficient()
        print(coefficients)
        for key in coefficients:
            self.__draw_area.add_rectangle(
                0,
                0,
                coefficients[key]["max_width"]/4,
                coefficients[key]["max_height"]/4,
                10
            )

        self.__header_bar.pack_start(self.__close_button)

        self.__main_box.append(self.__tool_box)
        self.__main_box.append(self.__draw_area)

        self.append(self.__header_bar)
        self.append(self.__main_box)

        self.add_action()

    def close(self, _btn= None):
        print("Fermeture")
        self.__close_callback()

    def add_action(self):
        self.__close_button.connect('clicked', self.close)




