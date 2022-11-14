from django.shortcuts import render,redirect
from .models import Team , SiteSettings
from cars.models import Car
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings


def home(request):
    teams = Team.objects.all()
    sitesettings = SiteSettings.objects.all()
    featured_car = Car.objects.order_by('-created_date').filter(is_featured=True)
    top_car = Car.objects.order_by('-price').filter(is_featured=True)[:3]  # this is for home-page header banner 
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
        'top_car' : top_car,
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
    if request.method == 'POST':

        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']
        
        subject = 'welcome to Garagezone'
        message = f'Hi {name}, thank you for contacting us we will get back to you soon.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )

        messages.success(request, 'Thank you for contacting us. We will get back to you shortly')
        return redirect('contact')

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
