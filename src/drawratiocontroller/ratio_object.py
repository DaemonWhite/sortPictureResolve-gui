import math
from .rectangle_draw import RectangleDraw

class Ratio(object):
    count_rectangle = 0
    def __init__(self, width, heigth):
        self.__rectangle_id = self.count_rectangle
        self.__rectangle = RectangleDraw(0,0, width, heigth)
        self.__sub_rectangle = RectangleDraw(0,0, width, heigth)
        self.__ratio = float(width/heigth)
        self.__divi = float(1)

    def get_id(self):
        return self.__rectangle_id

    def set_divi(self, divi):
        pass

    def set_rectangle_(self, width,heigth):
        pass

    def set_subrectangle(self, width, heigth):
        pass

    def set_color(self, color):
        pass

    def set_name(self, name):
        pass

    def set_left_offset(self, x, y):
        self.__rectangle.set_left_offset(x, y)

    def set_rigth_offset(self, x, y):
        self.__rectangle.set_rigth_offset(x, y)

    def cursor_left_is_select(self, x, y):
        return self.__rectangle.cursor_left_is_select( x, y)

    def cursor_rigth_is_select(self, x, y):
        return self.__rectangle.cursor_rigth_is_select( x, y)

    def apply_offset(self):
        self.__rectangle.apply_offset()

    def get_ratio(self):
        pass

    def circle(self, c, x, y, r):
        c.arc(x, y, r, 0, 2*math.pi)
        c.set_line_width(3)
        c.set_source_rgb(0,150,0)
        c.fill_preserve()
        c.stroke()

    def draw(self, c, w, h):
        left_X = self.__rectangle.get_X_left()
        left_Y = self.__rectangle.get_Y_left()
        rigth_X = self.__rectangle.get_X_rigth()
        rigth_Y = self.__rectangle.get_Y_rigth()
        radius = self.__rectangle.get_radius()


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



