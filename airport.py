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
        plane.is_flying()
        if self.is_safe():
            plane.land()
            self.hangar.append(plane)
            return self.hangar
        else:
            raise Exception('Too dangerous to land!')

    def take_off(self, plane):
        # if plane.is_flying():
            # the plane is flying!
        if not self.is_safe():
            raise Exception('Too dangerous to fly!')

        if plane in self.hangar:
            plane.take_off()
            self.hangar.remove(plane)
            return self.hangar
        
