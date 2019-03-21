class Plane:
    def __init__(self, flying = True):
        self.flying = flying

    def is_flying(self):
        return True if self.flying else False

    def land(self):
        if self.is_flying():
            self.flying = False
        
    def take_off(self):
        if not self.is_flying():
            self.flying = True
        else:
            raise Exception('Plane is flying')
