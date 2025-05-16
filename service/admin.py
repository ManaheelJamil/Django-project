from django.contrib import admin
from service.models import Service
from service.models import About
from service.models import Contact

class ServiceAdmin(admin.ModelAdmin):
    list_display=('service_icon','service_title','service_des')

admin.site.register(Service, ServiceAdmin)    

class AboutAdmin(admin.ModelAdmin):
    list_display=('about_icon','about_title','about_des')

admin.site.register(About,AboutAdmin)  

class ContactAdmin(admin.ModelAdmin):
    list_display=('contact_text',)

admin.site.register(Contact,ContactAdmin)    