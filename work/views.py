from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'work/index.html')

def contact(request):
    return render(request, 'work/contact.html')

def cleaning(request):
    return render(request, 'work/cleaning.html')

def recruitment(request):
    return render(request, 'work/recruitment.html')

def training(request):
    return render(request, 'work/training.html')

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        full_message = f"""
        New message from NewRealm Contact Form:

        Name: {name}
        Email: {email}
        Phone: {phone}

        Message:
        {message}
        """

        send_mail(
            subject=f"New Contact Form Submission from {name}",
            message=full_message,
            from_email='ibrahimsuleiman77@gmail.com',
            recipient_list=['ibrahimsuleiman77@gmail.com', 'newrealmmultibizresources1@gmail.com'],
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')  # Redirect back to the contact page

    return render(request, 'work/contact.html')
