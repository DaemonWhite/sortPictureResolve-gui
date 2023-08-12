from gi.repository import Adw, Gtk

@Gtk.Template(resource_path='/fr/daemonwhite/sortpictureresolve/ui/preferenceswindow.ui')
class PreferencesWindow(Adw.PreferencesWindow):
    __gtype_name__ = 'PreferencesWindow'
    def __init__(self, window):
        Adw.ApplicationWindow.__init__(self, title="Paramètres")
        self.show()


