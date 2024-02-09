from django.shortcuts import render, HttpResponse
import datetime
import requests
def homepage(request):
    return render(request,'index.html')

def reset(request):
    information={'weatherdesc':"",
                'weathericon':"",
                'temperature':"",
                'date':"",
                'city':"",
                'weatherimage':""
    }
    return render(request,'index.html',information)

def weatherforecast(request):
    city=''

    if city in request.POST:
        city=request.POST.get('city')
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=c23b4bb2589021fb996bb7129259f5ca'
    PARAMS= {'units':'metrics'}

    data=requests.get(url,PARAMS).json()
    print(data)
    description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']

    temperature = round(temperature/10,3)

    weatherimage = "http://openweathermap.org/img/w/"+icon+".png"

    day = datetime.date.today()

    information = {'weatherdesc':description,
                    'weathericon':icon,
                    'temperature':temperature,
                    'date':day,
                    'city':city,
                    'weatherimage':weatherimage,
                    'humidity':humidity
                    }
    return render(request,'index.html',information)