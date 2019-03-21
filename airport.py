from plane import Plane
from weather import Weather

class Airport:
    def __init__(self, city = 'london', weather = Weather()):
        self.city = city
        self.hangar = list()
        self.weather = weather

    def is_safe(self):
        return False if self.weather.is_stormy() else True

    def landing(self, plane):
        if self.is_safe():
            self.hangar.append(plane)
