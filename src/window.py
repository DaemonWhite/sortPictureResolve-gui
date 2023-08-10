
from gi.repository import Adw, Gtk, GLib

from LibPictureSorter import Picture_sorter
from sortpictureresolve_gui.picturecardcontroller import PictureCardController


@Gtk.Template(resource_path='/fr/daemonwhite/sortpictureresolve/window.ui')
class SortpictureresolveGuiWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'SortpictureresolveGuiWindow'

    main_box = Gtk.Template.Child("main_box")
    flow_picture_box = Gtk.Template.Child("flow_picture_box")
    search_images_button = Gtk.Template.Child("search_image")
    wait_bar = Gtk.Template.Child("wait_bar")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__ps = Picture_sorter()
        self.__ps.default_coef()
        self.__pcc = PictureCardController(self)
        self.add_action()
        self.wait_bar.set_pulse_step(0.5)
        self.wait_bar.set_visible(False)
        self.update_pulse()


    def update_pulse(self):
        self.wait_bar.pulse()
        return self.wait_bar.is_visible()

    def add_action(self):
        self.search_images_button.connect('clicked', self.on_search_image )

    def on_search_image(self, _btn):
        self.wait_bar.set_visible(True)
        self.search_images_button.set_visible(False)
        self.te = GLib.timeout_add(500, self.update_pulse)
        self.__ps.search_images()
        self.__ps.generate__list_sort_image()
        if  0 < self.__ps.get_max_image():
            self.flow_picture_box.set_visible(True)
            self.flow_picture_box.append(pc)
        else:
            self.search_images_button.set_visible(True)

        self.wait_bar.set_visible(False)



    def on_startup(self):
        pass
