
class RectangleDraw(object):
    radius = float(0)
    count_rectangle = 0
    DEFAULT_OFSSET = 0
    def __init__(self,
            x_left,
            y_left,
            x_rigth,
            y_rigth,
            radius
        ):
        self.__rectangle_id = self.count_rectangle
        self.radius = radius

        self.__x_left = x_left
        self.__y_left = y_left
        self.__x_rigth = x_rigth
        self.__y_rigth = y_rigth

        self.reset_offset()

        self.__cursor_left = [
            self.__x_left - self.radius,
            self.__x_left + self.radius,
            self.__y_left - self.radius,
            self.__y_left + self.radius,
        ]

        self.__cursor_rigth = [
            self.__x_left + self.__x_rigth - self.radius,
            self.__x_left + self.__x_rigth + self.radius,
            self.__y_left + self.__y_rigth - self.radius,
            self.__x_left + self.__y_rigth + self.radius,
        ]

    def cursor_select(self, array, x, y):
        selected=False
        if (
                array[0] < x
                and array[1] >= x
                and array[2] < y
                and array[3] >= y
            ):
            selected=True
        return selected

    def cursor_left_is_select(self, x, y):
        return self.cursor_select(self.__cursor_left, x, y)

    def cursor_rigth_is_select(self, x, y):
        return self.cursor_select(self.__cursor_rigth, x, y)

    def get_id(self):
        return self.__rectangle_id

    def get_cursot_left(self):
        return self.__cursor_left.copy()

    def get_circle_color(self):
        return (0,255,0)

    def get_rectagle_color(self):
        return (0,0,0)

    def get_radius(self):
        return self.radius

    def get_x_left(self):
        return self.__x_left + self.__x_left_offset

    def get_y_left(self):
        return self.__y_left + self.__y_left_offset

    def get_x_rigth(self):
        return self.__x_rigth + self.__x_rigth_offset

    def get_y_rigth(self):
        return self.__y_rigth + self.__y_rigth_offset

    def set_left_offset(self, x, y):
        self.__x_left_offset = x
        self.__y_left_offset = y
        self.__x_rigth_offset = -x
        self.__y_rigth_offset = -y

    def set_rigth_offset(self, x, y):
        self.__x_rigth_offset = x
        self.__y_rigth_offset = y

    def apply_offset(self):
        self.__x_left += self.__x_left_offset
        self.__y_left += self.__y_left_offset
        self.__x_rigth += self.__x_rigth_offset
        self.__y_rigth += self.__y_rigth_offset
        self.define_drag_cursor()
        self.reset_offset()

    def reset_offset(self):
        self.__x_left_offset = self.DEFAULT_OFSSET
        self.__y_left_offset = self.DEFAULT_OFSSET
        self.__x_rigth_offset = self.DEFAULT_OFSSET
        self.__y_rigth_offset = self.DEFAULT_OFSSET

    def define_drag_cursor(self):
        self.__cursor_left = [
            self.__x_left - self.radius,
            self.__x_left + self.radius,
            self.__y_left - self.radius,
            self.__y_left + self.radius,
        ]

        self.__cursor_rigth = [
            self.__x_left + self.__x_rigth - self.radius,
            self.__x_left + self.__x_rigth + self.radius,
            self.__y_left + self.__y_rigth - self.radius,
            self.__x_left + self.__y_rigth + self.radius,
        ]
        
