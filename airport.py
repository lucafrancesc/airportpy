from plane import Plane
from weather import Weather

class Airport:
    def __init__(self, city = 'london', capacity = 20, weather = Weather()):
        self.city = city
        self.hangar = list()
        self.capacity = capacity
        self.weather = weather

    def is_safe(self):
        return False if self.weather.is_stormy() else True

    def landing(self, plane):
        self._in_hangar(plane)
        self._full_hangar(plane)
        if self.is_safe():
            self._proceed_landing(plane)
        else:
            raise Exception('Too dangerous to land!')

    def _in_hangar(self, plane):
        if plane in self.hangar:
            raise Exception('Plane already in the hangar')

    def _full_hangar(self, plane):
        if len(self.hangar) >= self.capacity:
            raise Exception('No more space avaialble!')

    def _proceed_landing(self, plane):
        plane.land()
        self.hangar.append(plane)
        return self.hangar

    def take_off(self, plane):
        if not self.is_safe():
            raise Exception('Too dangerous to fly!')

        if plane in self.hangar:
            self._proceed_take_off(plane)
        else:
            raise Exception('Plane not in the hangar')

    def _proceed_take_off(self, plane):
        plane.take_off()
        self.hangar.remove(plane)
        return self.hangar
