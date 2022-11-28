from django.contrib import admin
from .models import User

admin.site.register(User)


#from .models import Education
# Register your models here.

#class EducationAdmin(admin.ModelAdmin):
  #  list_display = ['firstname', 'lastname', 'geolocation']

#admin.site.register(Education, EducationAdmin)