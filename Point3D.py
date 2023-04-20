from Point2D import Point2D

class Point3D(Point2D):
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self._z = z
        super().__init__(x, y)

    def get_z(self) -> float:
        return self._z

    def set_z(self, z):
        self._z = z

    def get_xyz(self) :
        return [self._x, self._y, self._z]

    def set_xyz(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def to_str(self) -> str:
        return f"Point3D [ {super().to_str() }"  f" z = {self._z } ]"

    def __add__(self, val3D):
        if type(val3D) == int:
            return Point3D(val3D + self._x,  val3D + self._y, val3D + self._z)
        else:
            return Point3D( val3D.get_x() + self._x,  val3D.get_y() + self._y, val3D.get_z() + self._z)


    def __eq__(self, other):
        return self._x == other.get_x() and self._y == other.get_y() and self._z == other.get_z()

    def __str__(self):
        return self.to_str()


    def __repr__(self):
        return self.to_str()

