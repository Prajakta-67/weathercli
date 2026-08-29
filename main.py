import requests



city = input("enter the city name:")
print(city)
params = {
    "lat": 15.36,
    "lon": 75.12,
    "appid": "b5767401f57ccbff71828175e6ae8f1d"


}


response = requests.get("https://api.openweathermap.org/data/2.5/weather", 
                    params=params)

data = response.json()
print(data["main"]["temp"])

print(response.json())