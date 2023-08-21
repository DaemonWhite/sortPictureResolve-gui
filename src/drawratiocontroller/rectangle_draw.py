
class RectangleDraw(object):
    radius = float(0)
    count_rectagle = 0
    def __init__(self,
            x_left,
            y_left,
            x_rigth,
            y_rigth,
            radius
        ):
        self.radius = radius
        self.count_rectagle += 1

        self.__x_left = x_left
        self.__y_left = y_left
        self.__x_rigth = x_rigth
        self.__y_rigth = y_rigth

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

    def get_cursot_left(self):
        return self.__cursor_left.copy()

    def get_circle_color(self):
        return (0,255,0)

    def get_rectagle_color(self):
        return (0,0,0)

    def get_radius(self):
        return self.radius

    def get_x_left(self):
        return self.__x_left

    def get_y_left(self):
        return self.__y_left

    def get_x_rigth(self):
        return self.__x_rigth

    def get_y_rigth(self):
        return self.__y_rigth
