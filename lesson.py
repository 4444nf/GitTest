class Point2D:

    def __int__(self, x: float, y: float):
        self._x = x
        self._y = y

    def __int__(self):
        pass

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
        return f"Point2D [x = {self._x}, y = {self._y}]"


class Point3D(Point2D):
    def __init__(self, x: float, y: float, z: float):
        self._z = z
        super().__init__(x, y)

    def get_z(self) -> float:
        return self._z

    def set_z(self, z):
        self._z = z

    def get_xyz(self, x, y, z):
        return [self._x, self._y, self._z]
    def set_xyz(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def to_str(self) -> str:
        return f"Point3D [{super().to_str()}", z={self._z}]"



