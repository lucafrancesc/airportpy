import unittest
from plane import Plane

class TestPlane(unittest.TestCase):

    def setUp(self):
        self.plane = Plane()

    def test_status(self):
        self.assertTrue(self.plane.is_flying())

if __name__ == "__main__":
    unittest.main()
