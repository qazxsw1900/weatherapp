from django.shortcuts import render, HttpResponse
from django.contrib.gis.geoip2 import GeoIP2


# Create your views here.
def weather_page(request):
    ip = get_client_ip(request)
    g = GeoIP2()
    g.city('72.14.207.99')
    page_looks = ip + '/n' + g.city(ip)
    return HttpResponse(ip)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip