import math

from gi.repository import Gtk, Gdk
from .rectangle_draw import RectangleDraw

#TODO Ajouter la gestion des coulleur

#TODO Ajouter la non revesirité des rectangles

class DrawRatioController(Gtk.DrawingArea):

    def __init__(self):
        super().__init__(
            vexpand=True,
            hexpand=True
        )
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
        self.add_rectangle(3,3, 53,53)
        self.add_rectangle(80,80, 150,150)


    def add_rectangle(
            self,
            x_left,
            y_left,
            x_rigth,
            y_rigth
        ):
        radius = 6
        self.__rectangle_list.append(
            RectangleDraw (
                x_left,
                y_left,
                x_rigth,
                y_rigth,
                radius
            )
        )
        RectangleDraw.count_rectangle += 1

    def mouse_update(self, motion,  x, y):
        for rc in self.__rectangle_list:
            if rc.cursor_left_is_select(x, y):
                self.__is_drag = True
                self.set_cursor(self.__grab_cursor)
                self.__rectangle_selected = rc.get_id()
            elif rc.cursor_rigth_is_select(x, y):
                self.__is_drag = True
                self.set_cursor(self.__grab_cursor)
                self.__rectangle_selected = rc.get_id() + 0.5
            elif not self.__is_drag:
                self.set_cursor(self.__default_cursor)
                self.__rectangle_selected = -1

    def drag_end(self, gesture, x, y):
        selected = int(self.__rectangle_selected)
        self.__rectangle_list[selected].apply_offset()
        self.__is_drag = False
        self.__rectangle_selected = -1

    def drag_update(self, gesture, x, y):
        selected = int(self.__rectangle_selected)
        if self.__is_drag:
            if self.__rectangle_selected == (selected + 0.5):
                self.__rectangle_list[selected].set_rigth_offset(x, y)
            else:
                self.__rectangle_list[selected].set_left_offset(x, y)

        self.queue_draw()

    def drag_begin(self, gesture, x, y):
        self.queue_draw()

    def circle(self, c, x, y, r):
        c.arc(x, y, r, 0, 2*math.pi)
        c.set_line_width(3)
        c.set_source_rgb(0,150,0)
        c.fill_preserve()
        c.stroke()

    def draw(self, area, c, w, h, data):
        for rc in self.__rectangle_list:
            left_X = rc.get_x_left()
            left_Y = rc.get_y_left()
            rigth_X = rc.get_x_rigth()
            rigth_Y = rc.get_y_rigth()
            radius = rc.get_radius()

            c.set_line_width(3)
            c.set_source_rgb(0,0,0)
            c.rectangle(
                left_X,
                left_Y,
                rigth_X,
                rigth_Y
            )
            c.stroke()
            self.circle(c, left_X, left_Y, radius)
            self.circle(c, left_X+rigth_X, left_Y+rigth_Y, radius)
            
