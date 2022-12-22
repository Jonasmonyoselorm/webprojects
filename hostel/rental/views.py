from django.shortcuts import render
from django.core.mail import send_mail #to allow you send mails

# Create your views here.

# Home page view
def index(request):
    return render(request, 'index.html', {})

# Contact Us page view

def contact_us(request):
    if request.method == "POST":
        client_name = request.POST['message-name']
        client_email = request.POST['message-email']
        client_phone = request.POST['message-phone']
        client_message = request.POST['message-text']

        # send an email
        send_mail(
            client_name, # client email subeject
            client_message, # client message
            client_email, # client email
            ['jonasmonyo@gmail.com'], # receiver's email

        )

        return render(request, 'contact.html', {
            'client_name': client_name
        }) # returning message

    else:
        return render(request, 'contact.html', {})
        


# About page view

def about_us(request):
    return render(request, 'about.html', {})

# CATEGORIES - 4-IN-ONE

def four_in_one(request):
    return render(request, 'four-in-one.html', {})


def three_in_one(request):
    return render(request, 'three-in-one.html', {})

