import requests

MyKey = "35b8ac511f6a10f73d057abd5f5d98cb"
response = requests.get(
    url=f"https://api.openweathermap.org/data/2.5/weather?lat=28.459497&lon=77.026634&appid={MyKey}"
)
print(response.status_code)
data = response.json()
print(data)
weather_ID = data["weather"]
Des = data["weather"]
print(weather_ID, Des)
# my_lat = 28.459497
# my_long = 77.026634
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()
# latitude = data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]
#
# coordinates = (latitude, longitude)
# print(coordinates)
# response = requests.get(
#     url="https://api.sunrise-sunset.org/json?lat=28.459497&lng=77.026634&formatted=0"
# )
#
# data = response.json()
# sunrise = data["results"]["sunrise"]
# sunset = data["results"]["sunset"]
#
# print(sunrise, sunset)
