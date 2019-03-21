from parse_api import Api
import re

class Weather:
    def __init__(self, safe = True, api = Api()):
        self.safe = safe
        self.api = api

    def is_safe(self, city = 'london'):
        if re.search('storm', Api(city).parsed_response()['weather'][0]['main']):
            self.safe = False
        else:
            self.safe = True

        return self.safe
