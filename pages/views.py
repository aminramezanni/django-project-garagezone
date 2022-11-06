from django.shortcuts import render
from .models import Team , SiteSettings
from cars.models import Car

def home(request):
    teams = Team.objects.all()
    sitesettings = SiteSettings.objects.all()
    featured_car = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_car = Car.objects.order_by('-created_date')[:6]
    brand_search = Car.objects.values_list('brand',flat=True).distinct()
    model_search = Car.objects.values_list('model',flat=True).distinct()
    city_search = Car.objects.values_list('city',flat=True).distinct()
    year_search = Car.objects.values_list('year',flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style',flat=True).distinct()

    data = {
        'teams':teams,
        'sitesettings' : sitesettings,
        'featured_car' : featured_car,
        'all_car' : all_car,
        'brand_search' : brand_search,
        'model_search' : model_search,
        'city_search' : city_search,
        'year_search': year_search,
        'body_style_search' : body_style_search,
    }
    return render(request, 'pages/home.html',data)


def about(request):
    teams = Team.objects.all()
    data = {
        'teams':teams
    }
    return render(request, 'pages/about.html',data)


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    sitesettings = SiteSettings.objects.all()
    data = {
        'sitesettings' : sitesettings
    }
    return render(request, 'pages/contact.html',data)


def header(request):
    sitesettings = SiteSettings.objects.all()
    data = {
        'sitesettings' : sitesettings,
    }
    return render(request, 'includes/header.html',data)