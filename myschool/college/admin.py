from django.contrib import admin
from .models import Enrollment

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    # This shows these columns in the list view
    list_display = ('first_name', 'last_name', 'email', 'created_at')
    
    # This adds a search bar to find students by name or email
    search_fields = ('first_name', 'last_name', 'email')
    
    # This adds a filter on the right side by date
    list_filter = ('created_at',)