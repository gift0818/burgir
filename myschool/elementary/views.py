from django.shortcuts import render
from .models import Enrollment
from django.db import IntegrityError 

def index(request):
    return render(request, 'elementary/index.html') # Match your folder!

def enroll(request):
    if request.method == 'POST':
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        email_addr = request.POST.get('email')

        try:
            Enrollment.objects.create(
                first_name=f_name, last_name=l_name, email=email_addr
            )
            return render(request, 'elementary/success.html', {'f_name': f_name})
        except IntegrityError:
            return render(request, 'elementary/enroll.html', {
                'error': "You have already enrolled!",
                'f_name': f_name, 'l_name': l_name
            })

    return render(request, 'elementary/enroll.html')