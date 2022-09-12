from django.contrib import admin
from .models import *

# Register your models here.

class AdminStudentUser(admin.ModelAdmin):
    list_display = ['user']

class AdminRecruiterUser(admin.ModelAdmin):
    list_display = ['company_name']

class AdminJobs(admin.ModelAdmin):
    list_display = ['title','company_name']



admin.site.register(StudentUser,AdminStudentUser)
admin.site.register(RecruiterUser,AdminRecruiterUser)
admin.site.register(Jobs,AdminJobs)
admin.site.register(Category)
admin.site.register(Apply)


