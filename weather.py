import json
import requests
from api_token import api_token

city = 'london'


api_url = "http://api.openweathermap.org/data/2.5/weather?appid=%s&q=%s"%(api_token(), city)
print(api_url)
response = requests.get(api_url)
print(json.loads(response.content.decode('utf-8')))
