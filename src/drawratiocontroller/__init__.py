import math

from gi.repository import Gtk, Gdk
from .rectangle_draw import RectangleDraw
from .ratio_object import Ratio

#TODO Ajouter la gestion des coulleur

#TODO Ajouter la non revesirité des rectangles

class DrawRatioController(Gtk.DrawingArea):

    def __init__(self):
        super().__init__(
            vexpand=True,
            hexpand=True
        )
        RectangleDraw.radius = 6

        self.__rectangle_selected = -1
        self.__is_drag = False
        self.__grab_cursor = Gdk.Cursor.new_from_name("grab", None)
        self.__default_cursor = Gdk.Cursor.new_from_name("default", None)

        drag = Gtk.GestureDrag.new()
        drag.connect("drag_begin", self.drag_begin)
        drag.connect("drag_update", self.drag_update)
        drag.connect("drag_end", self.drag_end)

        mouse = Gtk.EventControllerMotion.new()
        mouse.connect("motion", self.mouse_update)

        self.add_controller(drag)
        self.add_controller(mouse)
        self.__line = ""
        self.__rectangle_list = list()
        # self.add_rectangle(3,3, 53,53)
        # self.add_rectangle(80,80, 150,150)

    def add_coefficent(self, min_width, min_heigth, max_width, max_heigth):
        offset_windth = max_width - min_width
        offset_heigth = max_heigth - min_heigth
        self.add_rectangle(0,0, max_width, max_heigth)

    def add_rectangle(
            self,
            x_left,
            y_left,
            x_rigth,
            y_rigth,
            sub_rectangle
        ):
        self.__rectangle_list.append(
            Ratio (
                x_rigth,
                y_rigth,
            )
        )
        Ratio.count_rectangle += 1

    def mouse_update(self, motion,  x, y):
        for rc in self.__rectangle_list:
            if rc.cursor_left_is_select(x, y) or rc.cursor_rigth_is_select(x, y):
                self.set_cursor(self.__grab_cursor)
                break
            elif not self.__is_drag:
                self.set_cursor(self.__default_cursor)
                self.__rectangle_selected = -1

    def drag_end(self, gesture, x, y):
        print("end drag")
        selected = int(self.__rectangle_selected)
        self.__is_drag = False
        self.__rectangle_list[selected].apply_offset()
        self.__rectangle_selected = -1
        self.queue_draw()

    def drag_update(self, gesture, x, y):
        selected = int(self.__rectangle_selected)
        if self.__is_drag:
            if self.__rectangle_selected == (selected + 0.5):
                self.__rectangle_list[selected].set_rigth_offset(x, y)
            else:
                self.__rectangle_list[selected].set_left_offset(x, y)

        self.queue_draw()

    def drag_begin(self, gesture, x, y):
        if not self.__is_drag:
            for rc in self.__rectangle_list:
                if rc.cursor_left_is_select(x, y):
                    self.__rectangle_selected = rc.get_id()
                    self.__is_drag = True
                    break
                    print("left")
                elif rc.cursor_rigth_is_select(x, y) :
                    self.__rectangle_selected = rc.get_id() + 0.5
                    self.__is_drag = True
                    break
                    print("rigth")
                else:
                    self.__is_drag = False
        self.queue_draw()

    def draw(self, area, c, w, h, data):
        for rc in self.__rectangle_list:
            rc.draw(c, w, h)   
