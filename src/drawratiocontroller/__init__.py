from gi.repository import Gtk


class DrawRatioController(Gtk.DrawingArea):

    def __init__(self):
        super().__init__(
            vexpand=True,
            hexpand=True
        )

