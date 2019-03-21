class Plane:
    def __init__(self, flying = True):
        self.flying = flying

    def is_flying(self):
        return True if self.flying else False

    def land(self):
        self.flying = False
