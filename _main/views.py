from django.shortcuts import render, redirect
from django.contrib.gis.geoip2 import GeoIP2
import requests, urllib


class Weather:
    temperature = 0
    pressure = 0
    humidity = 0
    weather = ''
    icon = ''
    img_name = ''


def weather_page(request):
    ip = get_client_ip(request)
    g = GeoIP2()
    weather = get_weather(g.city(ip))
    return render(request, 'main/weather.html', {'weather': weather})


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    return ip


def get_weather(location):
    api_key = '2ef9d3f5c20c524d673f8c3ad0cab2bb'
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + location['city']
    response = requests.get(complete_url)
    x = response.json()
    weather = Weather()
    if x["cod"] != "404":
        y = x["main"]
        weather.temperature = round(y["temp"] - 273.15)
        weather.pressure = y["pressure"]
        weather.humidity = y["humidity"]
        z = x["weather"]
        weather.weather = z[0]["description"].title()
        weather.icon = z[0]["icon"]
        weather.img_name = z[0]["main"]
        return weather
    else:
        return None