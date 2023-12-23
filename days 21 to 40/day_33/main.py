import requests
from datetime import datetime

# Rock City Chattanooga TN
MY_LAT = 34.975307
MY_LONG = -85.354826


def iss_visible():
    iss_json = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_json.raise_for_status()

    iss_lat = float(iss_json.json()["iss_position"]["latitude"])
    iss_long = float(iss_json.json()["iss_position"]["longitude"])
    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LONG - 5 <= iss_long <= MY_LONG + 5:
        return True
    else:
        return False


def is_night():
    sunrise_params = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    time_now = datetime.now()
    sunrise_json = requests.get(url=f"https://api.sunrise-sunset.org/json", params=sunrise_params)
    sunrise_json.raise_for_status()
    # reformat datetime (switch "T" with " ") and remove the milliseconds.  it is now parsable by datetime lib
    my_sunrise = datetime.fromisoformat(sunrise_json.json()["results"]["sunrise"].replace("T", " ").split("+")[0])
    # my_sunset = datetime.fromisoformat(sunrise_json.json()["results"]["sunset"].replace("T", " ").split("+")[0])
    if time_now.hour > my_sunrise.hour and time_now.minute > my_sunrise.minute:
        return True
    else:
        return False


if iss_visible() is True and is_night() is True:
    pass  # do stuff in this event, not implemented

# it would be interesting to change this to plot ISS progress on a globe.
