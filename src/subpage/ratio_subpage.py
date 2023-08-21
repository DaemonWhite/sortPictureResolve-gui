from gi.repository import Adw, Gtk, GLib

from drawratiocontroller import DrawRatioController

class RatioWindow(Gtk.Box):
    __gtype_name__ = "RatioWindow"

    draw_area = Gtk.Template.Child("draw_area")

    def __init__(self, close_callback):
        super().__init__(
            orientation=Gtk.Orientation.VERTICAL
        )
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


    def draw(self, area, c, w, h, data):
        # c is a Cairo context

        # Fill background with a colour

        c.set_source_rgb(0, 0, 0)
        c.paint()

        # Draw a line
        c.set_source_rgb(0.5, 0.0, 0.5)
        c.set_line_width(3)
        c.move_to(10, 10)
        c.line_to(w - 10, h - 10)
        c.stroke()

        for x, y in self.blobs:
            c.arc(x, y, 10, 0, 2 * 3.1415926)
            c.fill()

        # Draw a rectangle
        c.set_source_rgb(0.8, 0.8, 0.0)
        c.rectangle(20, 20, 50, 20)
        c.fill()

        # Draw some text
        c.set_source_rgb(0.1, 0.1, 0.1)
        c.select_font_face("Sans")
        c.set_font_size(13)
        c.move_to(25, 35)
        c.show_text("Test")



