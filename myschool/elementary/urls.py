from django.urls import path
from . import views

urlpatterns = [
    # This 'name' must match the {% url 'elem_home' %} in base.html
    path('', views.index, name='elem_home'), 
    path('enroll/', views.enroll, name='elem_enroll'),
]