from Point2D import Point2D


class Point3D(Point2D):
    def __init__(self, x: float, y: float, z: float):
        self._z = z
        super().__init__(x, y)

    def get_z(self) -> float:
        return self._z

    def set_z(self, z):
        self._z = z

    def get_xyz(self, x, y, z):  #TODO fix this, there is not need for parameters in getter
        return [self._x, self._y, self._z]
    def set_xyz(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def to_str(self) -> str: #TODO fix this string
        return f"Point3D [{super().to_str()}", z={self._z}]"