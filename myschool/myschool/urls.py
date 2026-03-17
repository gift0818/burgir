from django.contrib import admin
from django.urls import path, include

# myschool/urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('college/', include('college.urls')),
    path('highschool/', include('highschool.urls')),
    path('elementary/', include('elementary.urls')),
    
    # ADD THIS LINE BELOW TO FIX THE ERROR:
    path("__reload__/", include("django_browser_reload.urls")),
]