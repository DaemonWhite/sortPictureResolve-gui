from gi.repository import Adw, Gtk, GLib

@Gtk.Template(resource_path='/fr/daemonwhite/sortpictureresolve/ui/preferenceswindow.ui')
class PreferencesWindow(Adw.PreferencesWindow):
    __gtype_name__ = 'PreferencesWindow'
    # Localisation Page
    expander_path_in = Gtk.Template.Child("expander_path_in")

    label_path_out = Gtk.Template.Child("label_path_out")

    button_open_out = Gtk.Template.Child("open_out")
    button_open_in = Gtk.Template.Child("open_in")

    switch_recursif = Gtk.Template.Child("switch_recursif")
    switch_copy = Gtk.Template.Child("switch_copy")
    switch_terminal = Gtk.Template.Child("switch_terminal")
    # Ration page
    button_add = Gtk.Template.Child("button_add")


    def __init__(self, window):
        Adw.ApplicationWindow.__init__(self, title="Paramètres")
        self.__window = window
        self.__FileDialog = Gtk.FileDialog.new()
        self.load_settings()
        self.add_action()
        self.show()

    def on_event_add_path_out(self, _btn, _result):
        try:
            path = _btn.select_folder_finish(_result).get_path()
            self.__window.set_path_out(path)
            self.__window.apply_settings()
            self.label_path_out.set_label(path)
        except GLib.Error as error:
            print(f"Error opening folder: {error.message}")

    def on_add_path_out(self, _btn):
        self.__FileDialog.select_folder(parent=self, callback=self.on_event_add_path_out)

    def load_settings(self):
        path_in = Gtk.Label()
        path_in.set_label(self.__window.get_path_in())
        self.expander_path_in.add_row(path_in)
        self.label_path_out.set_label(self.__window.get_path_out())

        self.switch_copy.set_active(self.__window.get_copy())
        self.switch_recursif.set_active(self.__window.get_recursif())
        self.switch_terminal.set_active(self.__window.get_terminal())

    def toggle_copy(self, _sw):
        self.__window.toggle_copy()
        self.__window.apply_settings()

    def toggle_recursif(self, _sw):
        self.__window.toggle_recursif()
        self.__window.apply_settings()

    def toggle_terminal(self, _sw):
        self.__window.toggle_terminal()
        self.__window.apply_settings()

    def add_action(self):
        self.button_open_out.connect("clicked", self.on_add_path_out)
        self.switch_copy.connect('activate', self.toggle_copy)
        self.switch_recursif.connect('activate', self.toggle_recursif)
        self.switch_terminal.connect('activate', self.toggle_terminal)



