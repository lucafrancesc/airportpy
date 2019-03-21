from unittest.mock import patch
from mock import Mock
import unittest
from airport import Airport

class TestAirport(unittest.TestCase):
    def setUp(self):
        self.airport = Airport()
        self.plane = Mock()
        self.weather = Mock()

    # SAFE
    @patch('airport.Airport.is_safe', return_value = True)
    def test_is_safe_True(self, is_safe):
        self.assertTrue(self.airport.is_safe())

    # NOT SAFE
    @patch('airport.Airport.is_safe', return_value = False)
    def test_is_safe_False(self, is_safe):
        self.assertFalse(self.airport.is_safe())

    # SAFE TO LAND
    @patch('airport.Airport.is_safe', return_value = True)
    def test_is_safe_to_land_True(self, is_safe):
        self.airport.landing(self.plane)
        self.assertIn(self.plane, self.airport.hangar)

    # SAFE TO LAND BUT NO MORE SPACES
    @patch('airport.Airport.is_safe', return_value = True)
    def test_is_safe_to_land_but_no_more_space_True(self, is_safe):
        for i in range(0, 20):
            plane = Mock()
            self.airport.landing(plane)
        with self.assertRaisesRegexp(Exception, 'No more space avaialble!'):
            self.airport.landing(self.plane)

    # SAFE TO LAND BUT ALREADY LANDED
    @patch('airport.Airport.is_safe', return_value = True)
    def test_is_safe_to_land_but_landed(self, is_safe):
        self.airport.landing(self.plane)
        with self.assertRaisesRegexp(Exception, 'Plane already in the hangar'):
            self.airport.landing(self.plane)

    # NOT SAFE TO LAND
    @patch('airport.Airport.is_safe', return_value = False)
    def test_is_safe_to_land_False(self, is_safe):
        with self.assertRaisesRegexp(Exception, 'Too dangerous to land!'):
            self.airport.landing(self.plane)

    # SAFE TO TAKE OFF
    @patch('airport.Airport.is_safe', return_value = True)
    def test_is_safe_to_take_off_True(self, is_safe):
        self.airport.landing(self.plane)
        self.airport.take_off(self.plane)
        self.assertNotIn(self.plane, self.airport.hangar)

    # NOT SAFE TO TAKE OFF
    @patch('airport.Airport.is_safe', return_value = False)
    def test_is_safe_to_take_off_False(self, is_safe):
        with self.assertRaisesRegexp(Exception, 'Too dangerous to fly!'):
            self.airport.take_off(self.plane)


if __name__ == '__main__':
    unittest.main()
