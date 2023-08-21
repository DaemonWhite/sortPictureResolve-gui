import math

from gi.repository import Gtk, Gdk
from .rectangle_draw import RectangleDraw

#TODO Ajouter la gestion des coulleur

#TODO Ajouter le depalcement des rectangles

class DrawRatioController(Gtk.DrawingArea):

    def __init__(self):
        super().__init__(
            vexpand=True,
            hexpand=True
        )
        self.__grab_cursor = Gdk.Cursor.new_from_name("grab", None)
        self.__default_cursor = Gdk.Cursor.new_from_name("default", None)

        drag = Gtk.GestureDrag.new()
        drag.connect("drag_begin", self.drag_begin)
        drag.connect("drag_update", self.drag_update)
        # self.connect("motion", self.mouse_update)
        #drag.connect("update", self.mouse_update)

        mouse = Gtk.EventControllerMotion.new()
        mouse.connect("motion", self.mouse_update)

        self.add_controller(drag)
        self.add_controller(mouse)
        self.__line = ""
        self.__rectangle_list = list()
        self.add_rectangle(3,3, 53,53)
        self.add_rectangle(60,60, 150,150)


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

    def mouse_update(self, motion,  x, y):
        for rc in self.__rectangle_list:
            if rc.cursor_left_is_select(x, y):
                self.set_cursor(self.__grab_cursor)
            elif rc.cursor_rigth_is_select(x, y):
                self.set_cursor(self.__grab_cursor)
            else:
                self.set_cursor(self.__default_cursor)



    def drag_update(self, gesture, x, y):
        print(x, y)
        self.queue_draw()

    def drag_begin(self, gesture, x, y):
        print(x,y)
        self.queue_draw()

    def circle(self, c, x, y, r):
        print(x,y)
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
            self.circle(c, left_X+rigth_X, left_X+rigth_X, radius)
            
