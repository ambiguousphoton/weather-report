import requests
from pprint import pprint

API_key = ""

location = input("enter location")

weather_fetch = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid="
final = weather_fetch + API_key

weather_data = requests.get(final).json()

pprint(weather_data)
