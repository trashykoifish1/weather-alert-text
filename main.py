import requests
import os
from twilio.rest import Client
import text
import datetime

OWM_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "fb05169487165459fc615186e50bc32c"
account_sid = "AC25caf402de752473fc35af94d02467f8"
auth_token = "52ace47b1162df51171d16e46f8986cb"
my_phone_number = "+18559515104"
rain_list = []
LATITUDE = 33.435341
LONGITUDE = -112.349670
will_rain = False
number = "6023327563"
message = ""
provider = "T-Mobile"
sender_credentials = ("khoitest1508@gmail.com", "navmpaimbjyvehfp")



parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": api_key,
    "units": "metric",
    # "lang": "vi",
    "exclude": "current,minutely,daily",
}

response = requests.get(url=OWM_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()
hour_forecast_list = weather_data["hourly"][:12]
for hour_data in hour_forecast_list:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 600:
        rain_list.append(hour_data)
        will_rain = True
if will_rain:
    ## Using twillo api
    # client = Client(account_sid, auth_token)
    # message = client.messages \
    #     .create(
    #     body="It's going to rain today. Remember to bring an umbrella ☔☔",
    #     from_=my_phone_number,
    #     to="+16023327563"
    # )
    # print(message.status)
    ## Sending text via email
    for rain_hour_data in rain_list:
        time = datetime.datetime.fromtimestamp(float(rain_hour_data["dt"])).time()
        description = rain_hour_data["weather"][0]["description"]
        message = f"It's going to rain at {time}, condition: {description}"
        text.send_mms_via_email(number, message, provider, sender_credentials, subject="Weather Forecast from Khoi")
        now = datetime.datetime.now()
        print(f"{now}: Message sent successfully")



