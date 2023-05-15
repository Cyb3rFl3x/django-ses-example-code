from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string

from django.shortcuts import render

# Create your views here.

def index(request):
    send_mail("test", "test", "felix.lehner1@gmail.com", ["felix.lehner1@gmail.com"], fail_silently=False)
    return render(request, 'index.html')





