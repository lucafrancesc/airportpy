import json
import requests
from api_token import api_token

class Api:
    def __init__(self, city = 'london'):
        self.api_url = "http://api.openweathermap.org/data/2.5/weather?appid=%s&q=%s"%(api_token(), city)


    def api_response(self):
        return requests.get(self.api_url)

    def parsed_response(self):
        if self.api_response().ok:
            return json.loads(self.api_response().content.decode('utf-8'))
        else:
            return None
