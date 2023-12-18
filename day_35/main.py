import requests
from apikey import api_key  # actual API key will not be stashed in git

# Rock City Chattanooga TN
latitude = 34.975307
longitude = -85.354826
url = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key
}

weather_data = requests.get(url, params=parameters)

