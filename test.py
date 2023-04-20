from Point3D import Point3D
import unittest

class TestPoint3D(unittest.TestCase):
    def test_add(self):
        a = Point3D(1.0)
        b = Point3D(2.0)
        c = Point3D
        c = a + b

        print(c.to_str())

        self.assertEqual(c, Point3D(3.0))

        c = 2 + c

        self.assertEqual(c, Point3D(5.0, 2, 2))

if __name__ == '__main__':
    unittest.main()


