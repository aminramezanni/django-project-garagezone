from django.shortcuts import render
from .models import Team , SiteSettings
from cars.models import Car

def home(request):
    teams = Team.objects.all()
    sitesettings = SiteSettings.objects.all()
    featured_car = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_car = Car.objects.order_by('-created_date')[:6]
    data = {
        'teams':teams,
        'sitesettings' : sitesettings,
        'featured_car' : featured_car,
        'all_car' : all_car,
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