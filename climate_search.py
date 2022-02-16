import requests
from pprint import pprint

API_Key = 'd557c4c4def5215f57852f4b4ea3f291'

# ask user to enter city they want to search
city = input("Enter a city: ")

# generate url to send request to
base_url = "https://api.openweathermap.org/data/2.5/weather?appid=" + API_Key + "&q=" + city

# receive respond in json format
weather_data = requests.get(base_url).json()

# print it to readable format
pprint(weather_data)

