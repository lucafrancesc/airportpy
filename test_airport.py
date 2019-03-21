from unittest.mock import patch
from mock import Mock
import unittest
from airport import Airport

class TestAirport(unittest.TestCase):
    def setUp(self):
        self.airport = Airport()
        self.plane = Mock()
        self.weather = Mock()

    @patch('airport.Airport.is_safe', return_value = True)
    def test_is_safe_true(self, is_safe):
        self.assertTrue(self.airport.is_safe())

    @patch('airport.Airport.is_safe', return_value = False)
    def test_is_safe_False(self, is_safe):
        self.assertFalse(self.airport.is_safe())




if __name__ == '__main__':
    unittest.main()
