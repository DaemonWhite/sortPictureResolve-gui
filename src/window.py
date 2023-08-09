
from gi.repository import Adw
from gi.repository import Gtk

from LibPictureSorter import Picture_sorter

@Gtk.Template(resource_path='/fr/daemonwhite/sortpictureresolve/window.ui')
class SortpictureresolveGuiWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'SortpictureresolveGuiWindow'

    label = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
