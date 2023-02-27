from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {"test": "I am Tested"}
    return render(request, 'index.html', context)
    # return HttpResponse("This is home page")

def about(request):
    context = {"test": "I am Tested"}
    return render(request, 'about.html', context)

def services(request):
    context = {"test": "I am Tested"}
    return render(request, 'services.html', context)

def contact(request):
    context = {"test": "I am Tested"}
    if request.method == "POST":
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact = Contact(email=email, phone=phone, date=datetime.today())
        contact.save()
        messages.success(request, 'Saved Successfully!')
    return render(request, 'contact.html', context)
