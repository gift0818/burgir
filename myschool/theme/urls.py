from django.urls import path
from . import views # This imports from theme/views.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('college/', include('college.urls')),
    path('highschool/', include('highschool.urls')),
    # V--- Check that 'elementary/' includes 'elementary.urls' ---V
    path('elementary/', include('elementary.urls')), 
]