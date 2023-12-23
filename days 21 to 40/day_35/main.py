import requests
from twilio.rest import Client
import apikey  # api keys in separate file (not in git)

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = apikey.openweather
account_sid = apikey.twilio_sid
auth_token = apikey.twilio_auth

# Rock City Chattanooga TN, it's a cool place to visit!
MY_LAT = 34.975307
MY_LONG = -85.354826

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today.",
        from_="111-111-1111",
        to="222-222-2222"
    )
    print(message.status)