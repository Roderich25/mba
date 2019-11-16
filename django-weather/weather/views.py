import requests
from django.views.generic import ListView, CreateView
from django.views.generic.edit import FormMixin
from .models import City
from .forms import CityForm
from django.urls import reverse_lazy
import os


def get_weather(city_name):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={os.getenv("WEATHER")}'
    r = requests.get(url).json()
    if r['cod'] == 200:
        city_weather = {'city': city_name,
                        'temperature': r['main']['temp'],
                        'description': r['weather'][0]['description'],
                        'icon': r['weather'][0]['icon']}
        return city_weather


class IndexView(CreateView, ListView):
    template_name = 'weather/weather.html'
    context_object_name = 'weather_list'
    form_class = CityForm
    success_url = reverse_lazy('weather:index')

    def get_queryset(self):
        weather_list = []
        for city in City.objects.all().order_by('-id'):
            weather_list.append(get_weather(city.name))
        return weather_list

