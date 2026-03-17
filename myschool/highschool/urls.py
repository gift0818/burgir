from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='hs_home'),
    path('enroll/', views.enroll, name='hs_enroll'),
]