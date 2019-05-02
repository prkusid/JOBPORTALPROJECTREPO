from django.contrib import admin
from jobapp.models import CityJobs,Apply

# Register your models here.

class CityJobsAdmin(admin.ModelAdmin):
    list_display = ['city','date','company','slug','designation','email','address']
    search_fields = ('company','city')
    prepopulated_fields = {'slug':('company',)}

class ApplyAdmin(admin.ModelAdmin):
    list_display = ['user','name','age','email','degree','college','date','resume','company','designation','city',]


admin.site.register(CityJobs,CityJobsAdmin)
admin.site.register(Apply,ApplyAdmin)

# Register your models here.
