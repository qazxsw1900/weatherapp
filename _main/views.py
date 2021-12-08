from django.shortcuts import render, HttpResponse
from django.contrib.gis.geoip2 import GeoIP2
import requests, json


# Create your views here.
def weather_page(request):
    ip = get_client_ip(request)
    g = GeoIP2()
    page_looks = [ip, g.city(ip)]
    return HttpResponse(get_weather(g.city(ip)))


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_weather(location):
    api_key = '2ef9d3f5c20c524d673f8c3ad0cab2bb'
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + location['city']
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        return " Temperature (in kelvin unit) = " + str(
            current_temperature) + "\n atmospheric pressure (in hPa unit) = " + str(
            current_pressure) + "\n humidity (in percentage) = " + str(current_humidity) + "\n description = " + str(
            weather_description)
    else:
        return "City Not Found "
