
class RectangleDraw(object):
    radius = float(6)
    count_rectangle = 0
    DEFAULT_OFSSET = 0
    def __init__(self,
            X_left,
            Y_left,
            X_rigth,
            Y_rigth,
        ):
        self.__rectangle_id = self.count_rectangle

        self.__X_left = X_left
        self.__Y_left = Y_left
        self.__X_rigth = X_rigth
        self.__Y_rigth = Y_rigth

        self.reset_offset()

        self.__enable_cursor_left = True
        self.__cursor_left = [
            self.__X_left - self.radius,
            self.__X_left + self.radius,
            self.__Y_left - self.radius,
            self.__Y_left + self.radius,
        ]

        self.__enable_cursor_rigth = True
        self.__cursor_rigth = [
            self.__X_left + self.__X_rigth - self.radius,
            self.__X_left + self.__X_rigth + self.radius,
            self.__Y_left + self.__Y_rigth - self.radius,
            self.__Y_left + self.__Y_rigth + self.radius,
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
        return (
            self.cursor_select(self.__cursor_left, x, y)
            and self.__enable_cursor_left
        )

    def cursor_rigth_is_select(self, x, y):
        return (
            self.cursor_select(self.__cursor_rigth, x, y)
            and self.__enable_cursor_rigth
        )

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

    def get_X_left(self):
        return self.__X_left + self.__X_left_offset

    def get_Y_left(self):
        return self.__Y_left + self.__Y_left_offset

    def get_X_rigth(self):
        return self.__X_rigth + self.__X_rigth_offset

    def get_Y_rigth(self):
        return self.__Y_rigth + self.__Y_rigth_offset

    def set_left_offset(self, x, y):
        self.__X_left_offset = x
        self.__Y_left_offset = y
        self.__X_rigth_offset = -x
        self.__Y_rigth_offset = -y

    def set_rigth_offset(self, x, y):
        self.__X_rigth_offset = x
        self.__Y_rigth_offset = y

    def apply_offset(self):
        self.__X_left += self.__X_left_offset
        self.__Y_left += self.__Y_left_offset
        self.__X_rigth += self.__X_rigth_offset
        self.__Y_rigth += self.__Y_rigth_offset
        self.define_drag_cursor()
        self.reset_offset()

    def reset_offset(self):
        self.__X_left_offset = self.DEFAULT_OFSSET
        self.__Y_left_offset = self.DEFAULT_OFSSET
        self.__X_rigth_offset = self.DEFAULT_OFSSET
        self.__Y_rigth_offset = self.DEFAULT_OFSSET

    def define_drag_cursor(self):
        self.__cursor_left = [
            self.__X_left - self.radius,
            self.__X_left + self.radius,
            self.__Y_left - self.radius,
            self.__Y_left + self.radius,
        ]

        self.__cursor_rigth = [
            self.__X_left + self.__X_rigth - self.radius,
            self.__X_left + self.__X_rigth + self.radius,
            self.__Y_left + self.__Y_rigth - self.radius,
            self.__Y_left + self.__Y_rigth + self.radius,
        ]
        
    def enable_cursor_left(self, activate = True):
        self.__enable_cursor_left = activate

    def enable_cursor_rigth(self, activate = True):
        self.__enable_cursor_rigth = activate
