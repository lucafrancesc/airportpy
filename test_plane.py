import unittest
from plane import Plane

class TestPlane(unittest.TestCase):

    def setUp(self):
        self.plane = Plane()

    def test_status(self):
        self.assertTrue(self.plane.is_flying())

    def test_land(self):
        self.plane.land()
        self.assertFalse(self.plane.is_flying())

    def test_take_off(self):
        self.plane.land()
        self.plane.take_off()
        self.assertTrue(self.plane.is_flying())

    def test_cannot_take_off_if_flying(self):
        with self.assertRaisesRegexp(Exception, 'Plane is flying'):
            self.plane.take_off()

if __name__ == "__main__":
    unittest.main()
