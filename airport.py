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
            raise Exception('Too dangerous to fly!')

# x = Airport()
# w = Plane()
# x.landing(w)
# # print()
# print(x.hangar[0].is_flying())
