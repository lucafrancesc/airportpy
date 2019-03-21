from unittest.mock import patch
import unittest
from weather import Weather

class TestWeather(unittest.TestCase):

    def setUp(self):
        self.weather = Weather()

    @patch('weather.Weather.is_stormy', return_value = True)
    def test_is_stormy_true(self, is_stormy):
        self.assertTrue(self.weather.is_stormy())

    @patch('weather.Weather.is_stormy', return_value = False)
    def test_is_stormy_false(self, is_stormy):
        self.assertFalse(self.weather.is_stormy())

if __name__ == "__main__":
    unittest.main()
