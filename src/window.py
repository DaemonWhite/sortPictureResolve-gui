from threading import Thread
from gi.repository import Adw, Gtk, GLib

from LibPictureSorter import Picture_sorter
from picturecardcontroller import PictureCardController


@Gtk.Template(resource_path='/fr/daemonwhite/sortpictureresolve/window.ui')
class SortpictureresolveGuiWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'SortpictureresolveGuiWindow'

    main_box = Gtk.Template.Child("main_box")
    flow_picture_box = Gtk.Template.Child("flow_picture_box")
    controller_bar_box =  Gtk.Template.Child("controller_bar")

    search_images_button = Gtk.Template.Child("search_image")
    list_view_button = Gtk.Template.Child("list_view_button")
    sort_button = Gtk.Template.Child("sort_button")

    wait_bar = Gtk.Template.Child("wait_bar")


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__ps = Picture_sorter()
        self.__ps.set_event_progrres_move(self.sort_images)
        self.__ps.enabled_copie_mode()
        self.__ps.default_coef()
        self.__ps.remove_extention(".gif")
        self.__ps.set_picture_in_path("/home/matheo/Images/Font d'écran/a trier/")
        self.__pcc = PictureCardController(self)
        self.add_action()
        self.wait_bar.set_pulse_step(0.5)
        self.wait_bar.set_visible(False)
        self.update_pulse()


    def update_pulse(self):
        self.wait_bar.pulse()
        return self.wait_bar.is_visible()

    def add_action(self):
        self.search_images_button.connect('clicked', self.on_search_images )
        self.sort_button.connect("clicked", self.on_sort_images)

    def thread_start_images(self):
        self.__ps.search_images()
        self.__ps.generate__list_sort_image()
        self.__ps.resolve()

        if  0 < self.__ps.get_max_image():
            path = self.__ps.get_picture_in_path()
            picture_search = self.__ps.get_resolve_image()
            self.__pcc.set_path(path)
            self.__pcc.set_config(picture_search)
            print(picture_search)
            self.__pcc.generate_card()
            self.picture_view()
        else:
            self.reset()

        self.wait_bar.set_visible(False)

    def reset_view(self):
        self.flow_picture_box.set_visible(False)
        self.controller_bar_box.set_visible(False)
        self.wait_bar.set_visible(False)
        self.search_images_button.set_visible(True)

    def loading_view(self):
        self.flow_picture_box.set_visible(False)
        self.controller_bar_box.set_visible(False)
        self.search_images_button.set_visible(False)
        self.wait_bar.set_visible(True)

    def picture_view(self):
        self.flow_picture_box.set_visible(True)
        self.controller_bar_box.set_visible(True)
        self.search_images_button.set_visible(False)
        self.wait_bar.set_visible(False)

    def sort_images(self):
        GLib.timeout_add(
            10,
            self.wait_bar.set_fraction,
            self.__ps.get_current_image() /
            self.__ps.get_max_image()
        )

    def on_sort_images(self, _btn):
        self.wait_bar.set_fraction(0)
        sort = Thread(target=self.__ps.apply_resolve)
        self.loading_view()
        sort.run()


    def on_search_images(self, _btn):
        search = Thread(target=self.thread_start_images)
        self.loading_view()
        self.te = GLib.timeout_add(500, self.update_pulse)
        search.start()



    def on_startup(self):
        pass

