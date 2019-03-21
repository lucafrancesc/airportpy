class Plane:
    def __init__(self, flying = True):
        self.flying = flying

    def is_flying(self):
        if self.flying:
            return True
