from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage),
    path('reset/',views.reset,name='resetbtn'),
    path('forecast/',views.weatherforecast,name='forecast')
]