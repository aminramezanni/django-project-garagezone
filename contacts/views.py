from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages



def inquiry(request):

    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        car_title = request.POST['car_title']
        car_id = request.POST['car_id']
        customer_request = request.POST['customer_request']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']

        contact = Contact(first_name = first_name,last_name= last_name,car_title= car_title,
        car_id=car_id,customer_request= customer_request,city= city,state= state,email= email,
        phone= phone,message= message,user_id= user_id,
        )

        contact.save()
        messages.success(request, 'your request has been submitted, we will get back to you soon')
        return redirect('/cars/'+car_id)
