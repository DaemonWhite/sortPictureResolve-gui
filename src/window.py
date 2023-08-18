from threading import Thread
from gi.repository import (
    Adw,
    Gtk,
    Gdk,
    GLib,
    Gio
)

from .preferences_window import PreferencesWindow
from .configurationmanager import ConfigurationManager

from LibPictureSorter import Picture_sorter
from picturecardcontroller import PictureCardController


@Gtk.Template(resource_path='/fr/daemonwhite/sortpictureresolve/ui/window.ui')
class SortpictureresolveGuiWindow(Adw.ApplicationWindow, ConfigurationManager):
    __gtype_name__ = 'SortpictureresolveGuiWindow'

    APPID = "fr.daemonwhite.sortpictureresolve"
    main_box = Gtk.Template.Child("main_box")
    flow_picture_box = Gtk.Template.Child("flow_picture_box")
    controller_bar_box =  Gtk.Template.Child("controller_bar")

    search_images_button = Gtk.Template.Child("search_image")
    list_view_button = Gtk.Template.Child("list_view_button")
    sort_button = Gtk.Template.Child("sort_button")
    open_picture_folder = Gtk.Template.Child("open_picture_folder")

    wait_bar = Gtk.Template.Child("wait_bar")


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ConfigurationManager.__init__(self, APPID=self.APPID)
        self.__application = kwargs["application"]

        self.__FileDialog = Gtk.FileDialog.new()

        self.__ps = Picture_sorter()
        self.__ps.set_event_progress_move(self.sort_images)
        self.__ps.set_event_end_move(self.finish_sort_image)

        self.apply_settings()

        self.__pcc = PictureCardController(self)

        self.add_action()

        self.wait_bar.set_pulse_step(0.5)
        self.wait_bar.set_visible(False)

        self.update_pulse()

    def apply_settings(self):
        self.__ps.enabled_copie_mode(self.get_copy())
        self.__ps.enabled_recursif_mode(self.get_recursif())
        self.__ps.default_coef()
        try :
            self.__ps.remove_extention(".gif")
        except:
            print("impossible remove image")



    def update_pulse(self):
        self.wait_bar.pulse()
        return self.wait_bar.is_visible()

    def add_action(self):
        self.search_images_button.connect('clicked', self.on_search_images )
        self.sort_button.connect("clicked", self.on_sort_images)
        self.open_picture_folder.connect("clicked", self.on_choose_folder_button)
        self.__application.create_action('preferences', self.on_preferences_action)

    def thread_start_images(self):
        self.__ps.search_images()
        self.__ps.generate__list_sort_image()
        self.__ps.resolve()

        if  0 < self.__ps.get_max_image():
            path = self.__ps.get_picture_in_path()
            picture_search = self.__ps.get_resolve_image()
            self.__pcc.set_path(path)
            self.__pcc.set_config(picture_search)
            self.__pcc.generate()
            self.picture_view()
        else:
            self.reset_view()

        self.wait_bar.set_visible(False)

    def reset_view(self):
        self.main_box.set_orientation(Gtk.Orientation.HORIZONTAL)
        self.flow_picture_box.set_visible(False)
        self.controller_bar_box.set_visible(False)
        self.wait_bar.set_visible(False)
        self.search_images_button.set_visible(True)

    def loading_view(self):
        self.main_box.set_orientation(Gtk.Orientation.HORIZONTAL)
        self.flow_picture_box.set_visible(False)
        self.controller_bar_box.set_visible(False)
        self.search_images_button.set_visible(False)
        self.wait_bar.set_visible(True)

    def picture_view(self):
        self.main_box.set_orientation(Gtk.Orientation.VERTICAL)
        self.flow_picture_box.set_visible(True)
        self.controller_bar_box.set_visible(True)
        self.search_images_button.set_visible(False)
        self.wait_bar.set_visible(False)

    def reset_json_configuration(self):
        pc_old = [1800, 1200]
        phone = [1090, 1200]
        null = 0
        pc_standar = [2000, 1000]
        pc_large = [2960, 1040]
        ps = Picture_sorter()
        self.__cps.modify_path_in(ps.get_picture_in_path())
        self.__cps.modify_path_out(ps.get_picture_out_path())
        self.__cps.add_coefficient(
            "pc-stadart", pc_old[0], pc_old[1], pc_standar[0], pc_standar[1]
        )
        self.__cps.add_coefficient("pc-old", phone[0], phone[1], pc_old[0], pc_old[1])
        self.__cps.add_coefficient("phone", null, null, phone[0], phone[1])
        self.__cps.add_coefficient(
            "pc-large", pc_standar[0], pc_standar[1], pc_large[0], pc_large[1]
        )
        self.__cps.disable_default()
        self.__cps.save()
        del ps

    def finish_sort_image(self):
        self.reset_view()

    def sort_images(self):
        GLib.timeout_add(
            10,
            self.wait_bar.set_fraction,
            self.__ps.get_current_image() /
            self.__ps.get_max_image()
        )

    def set_path(self, _btn, _result):
        try:
            path = _btn.select_folder_finish(_result).get_path()
            self.__ps.set_picture_in_path(path)
            self.reset_view()
            self.__pcc.reset()
        except GLib.Error as error:
            print(f"Error opening folder: {error.message}")

    def on_preferences_action(self, widget, _):
        """Callback for the app.preferences action."""
        pw = PreferencesWindow(self)


    def on_choose_folder_button(self, _ptn):
        self.__FileDialog.select_folder(parent=self, callback=self.set_path)
        self.__ps.reset_search_images()

    def on_sort_images(self, _btn):
        self.wait_bar.set_fraction(0)
        sort = Thread(target=self.__ps.apply_resolve)
        self.loading_view()
        sort.start()


    def on_search_images(self, _btn):
        search = Thread(target=self.thread_start_images)
        self.loading_view()
        self.te = GLib.timeout_add(500, self.update_pulse)
        search.start()

    def on_startup(self):
        pass


