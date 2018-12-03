from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contact(request):
    if request.method == 'POST':
        name = request.POST['mytype1']
        email = request.POST['mytype2']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contact(name=name, email=email, phone=phone, message=message)

        contact.save()

        messages.success(request, ' Will get back to you as soon as I reach my database!')

        return redirect('/#contact')
