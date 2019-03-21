from unittest.mock import patch
import unittest
from weather import Weather

class TestWeather(unittest.TestCase):

    def setUp(self):
        self.weather = Weather()

    def test_is_safe_true(self):
        self.assertTrue(self.weather.is_safe())

    # def test_is_safe_false(self):
    #     self.assertFalse(self.weather.is_safe())



if __name__ == "__main__":
    unittest.main()
