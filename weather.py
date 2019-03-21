from parse_api import Api
import re

class Weather:
    def __init__(self, strormy = False, api = Api()):
        self.strormy = strormy
        self.api = api

    def is_stormy(self, city = 'london'):
        if re.search('storm', Api(city).parsed_response()['weather'][0]['main']):
            self.strormy = True
        else:
            self.strormy = False

        return self.strormy
