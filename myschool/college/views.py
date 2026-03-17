from django.shortcuts import render
from .models import Enrollment
from django.db import IntegrityError 

# 1. The Home Page View
def index(request):
    return render(request, 'college/index.html')

# 2. The Enrollment Form View
def enroll(request):
    if request.method == 'POST':
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        email_addr = request.POST.get('email')

        try:
            Enrollment.objects.create(
                first_name=f_name,
                last_name=l_name,
                email=email_addr
            )
            return render(request, 'college/success.html', {'f_name': f_name})
            
        except IntegrityError:
            return render(request, 'college/enroll.html', {
                'error': "You have already enrolled with this email address!",
                'f_name': f_name,
                'l_name': l_name
            })

    return render(request, 'college/enroll.html')