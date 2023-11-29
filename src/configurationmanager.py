from gi.repository import Gio

from LibPictureSorter import ConfigPictureSorter, Picture_sorter

class ConfigurationManager(object):

    cps = ConfigPictureSorter()

    __CONFIGURATION_NAME_TERMINAL = "terminal-mode"
    __CONFIGURATION_NAME_COPY = "copy-mode"
    __CONFIGURATION_NAME_RECURSIF = "recursif-mode"
    __CONFIGURATION_NAME_FIRST_START = "first-start"
    __CONFIGURATION_NAME_PATH_IN = "path-in"
    __CONFIGURATION_NAME_PATH_OUT = "path-out"

    _copy_mode = False
    _recursif_mode = True
    _path_in = "~/"
    _path_out = "~/out"
    _terminal_mode = False

    def __init__(self, APPID):
        self._settings = Gio.Settings(APPID)
        self.cps.load()
        self.load_configuration()

    def get_path_in(self):
        return self._path_in

    def get_path_out(self):
        return self._path_out

    def get_recursif(self):
        return self._recursif_mode

    def get_all_coefficient(self):
        return self.__coefficient.copy()

    def get_copy(self):
        return self._copy_mode

    def get_terminal(self):
        return self._terminal_mode

    def set_path_in(self, path_in):
        self._path_in = path_in
        self.cps.modify_path_in(path_in)
        if self._terminal_mode:
            self.cps.modify_path_in(path_in)
            self.cps.save()
        self._settings.set_string(self.__CONFIGURATION_NAME_PATH_IN,path_in)

    def set_path_out(self, path_out):
        self._path_out = path_out
        self.cps.modify_path_out(path_out)
        if self._terminal_mode:
            self.cps.modify_path_out(path_out)
            self.cps.save()
        self._settings.set_string(self.__CONFIGURATION_NAME_PATH_OUT, path_out)

    def toggle_copy(self):
        self._copy_mode = not self._copy_mode

        if self._terminal_mode:
            self.cps.enabled_copy_mode(self._copy_mode)
            self.cps.save()

        self._settings.set_boolean(
            self.__CONFIGURATION_NAME_COPY,
            self._copy_mode
        )

    def toggle_terminal(self):
        self._terminal_mode = not self._terminal_mode
        self._settings.set_boolean(
            self.__CONFIGURATION_NAME_TERMINAL,
            self._terminal_mode
        )

    def toggle_recursif(self):
        self._recursif_mode = not self._recursif_mode
        self._settings.set_boolean(
            self.__CONFIGURATION_NAME_RECURSIF,
            self._recursif_mode
        )

    def load_json_configuration(self):
        self._copy_mode = self.cps.get_copy()

        self._path_in = self.cps.get_path_in()
        self._path_out = self.cps.get_path_out()

        # TODO Changer par la version terminal
        self._recursif_mode = self._settings.get_boolean("recursif-mode")

    def load_gschema_configuration(self):
        self._copy_mode = self._settings.get_boolean("copy-mode")
        self._recursif_mode = self._settings.get_boolean("recursif-mode")

        self._path_in = self._settings.get_string("path-in")
        self._path_out = self._settings.get_string("path-out")

    def load_configuration(self):
        self._terminal_mode = self._settings.get_boolean("terminal-mode")
        self.__coefficient = self.cps.get_all_coefficient()

        if self._settings.get_boolean("first-start"):
            if self.cps.get_default():
                self.reset_json_configuration()

        if self._terminal_mode:
            self.load_json_configuration()
        else:
            self.load_gschema_configuration()

    def reset_json_configuration(self):
        pc_old = [1800, 1200]
        phone = [1090, 1200]
        null = 0
        pc_standar = [2000, 1000]
        pc_large = [2960, 1040]
        ps = Picture_sorter()
        self.cps.modify_path_in(ps.get_picture_in_path())
        self.cps.modify_path_out(ps.get_picture_out_path())
        self.cps.add_coefficient(
            "pc-stadart", pc_old[0], pc_old[1], pc_standar[0], pc_standar[1]
        )
        self.cps.add_coefficient("pc-old", phone[0], phone[1], pc_old[0], pc_old[1])
        self.cps.add_coefficient("phone", null, null, phone[0], phone[1])
        self.cps.add_coefficient(
            "pc-large", pc_standar[0], pc_standar[1], pc_large[0], pc_large[1]
        )
        self.cps.disable_default()
        self.cps.save()
        del ps
