import requests


response = requests.get(
    url="https://api.open-meteo.com/v1/forecast",
    params={"latitude": 35.6895, "longitude": 139.6917, "current": "temperature_2m"},
)
print(response.json())
