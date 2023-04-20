class Point2D:

    def __init__(self, x: float = 0, y: float = 0):
        self._x = x
        self._y = y

    def get_x(self) -> float:
        return self._x

    def set_x(self, x):
        self._x = x

    def get_y(self) -> float:
        return self._y

    def set_y(self, y):
        self._y = y

    def get_xy(self):
        return [self._x, self._y]

    def set_xy(self, x, y):
        self._x = x
        self._y = y

    def to_str(self) -> str:
        return f"Point2D x = {self._x}, y = {self._y}"

    def __add__(self, val2D):
        c = Point2D()
        c.x = val2D.get_x() + self._x
        c.y = val2D.get_y() + self._y
        return c
