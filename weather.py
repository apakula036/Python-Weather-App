from locale import format_string
from urllib import request, response
import requests
import config

API_KEY1 = config.API_KEY
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY1}&q={city}&units=imperial"

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    temperature = round(data["main"]["temp"])

    print("The weather is:", weather + ".")
    print("It is currently" , temperature , "degrees farenheit.")

    # print(data)
else:
    print("An error occurred.")