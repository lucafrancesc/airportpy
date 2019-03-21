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
    def test_is_safe_True(self, is_safe):
        self.assertTrue(self.airport.is_safe())

    @patch('airport.Airport.is_safe', return_value = True)
    def test_is_safe_to_land_True(self, is_safe):
        self.airport.landing(self.plane)
        self.assertIn(self.plane, self.airport.hangar)

    # @patch('airport.Airport.is_safe', return_value = True)
    # def test_landing_a_landed_plane(self, is_safe, is_flying):
    #     with self.assertRaisesRegexp(Exception, 'Plane has already landed'):
    #         self.airport.landing(self.plane)

    @patch('airport.Airport.is_safe', return_value = False)
    def test_is_safe_False(self, is_safe):
        self.assertFalse(self.airport.is_safe())

    @patch('airport.Airport.is_safe', return_value = False)
    def test_is_safe_to_land_False(self, is_safe):
        with self.assertRaisesRegexp(Exception, 'Too dangerous to fly!'):
            self.airport.landing(self.plane)






if __name__ == '__main__':
    unittest.main()
