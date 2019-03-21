from plane import Plane
from weather import Weather

class Airport:
    def __init__(self, city = 'london', weather = Weather(), capacity = 20):
        self.city = city
        self.hangar = list()
        self.capacity = capacity
        self.weather = weather

    def is_safe(self):
        return False if self.weather.is_stormy() else True

    def landing(self, plane):
        if plane in self.hangar:
            raise Exception('Plane already in the hangar')

        if self.is_safe() and len(self.hangar)<self.capacity:
            plane.land()
            self.hangar.append(plane)
            return self.hangar
        else:
            raise Exception('Too dangerous to land!')

    def take_off(self, plane):
        if not self.is_safe():
            raise Exception('Too dangerous to fly!')

        if plane in self.hangar:
            plane.take_off()
            self.hangar.remove(plane)
            return self.hangar
        else:
            raise Exception('Plane not in the hangar')



# x = Airport()
# w = Plane()
# x.landing(w)
# # print()
# print(x.hangar[0].is_flying())
