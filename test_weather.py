from unittest.mock import patch
import unittest
from weather import Weather

class TestWeather(unittest.TestCase):

    def setUp(self):
        self.weather = Weather()


    @patch('weather.Weather.is_safe', return_value = True)
    def test_is_safe_true(self, is_safe):
        self.assertTrue(self.weather.is_safe())

    @patch('weather.Weather.is_safe', return_value = False)
    def test_is_safe_false(self, is_safe):
        self.assertFalse(self.weather.is_safe())



if __name__ == "__main__":
    unittest.main()
