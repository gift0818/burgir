from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='college_home'),
    path('enroll/', views.enroll, name='college_enroll'),
]