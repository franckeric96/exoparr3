from django.contrib import admin

from . import models
from django.utils.safestring import mark_safe



# Register your models here.
class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Presentation',{'fields': ['nom','image']}),
        ('Status', {'fields': ['status']})
        
    ]
    
    
    list_display = ('nom','date_add','status','image_views')
    list_filter = ('status',)
    search_fields = ('nom',)
    date_hierarchy = "date_add"
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    
    def image_views(self,obj):
        return mark_safe("<img src='{url}' width= 100px height=50px >".format(url=obj.image.url))

    
class AdmissionAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ('Presentation',{'fields': ['nom','prenom','email']}),
        ('Status',{'fields': ['numero','message','status']})
       
    ]
    
    list_display = ('nom','prenom','email','date_add','status')
    list_filter = ('status',)
    search_fields = ('nom',)
    date_hierarchy = "date_add"
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10



class CoursesAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ('Presentation',{'fields': ['titre']}),
        ('Status',{'fields': ['status']})
       
    ]
    
    list_display = ('titre','date_add','status','image_views')
    list_filter = ('status',)
    search_fields = ('titre',)
    date_hierarchy = "date_add"
    list_display_links = ['titre']
    ordering = ['titre']
    list_per_page = 10
    
    def image_views(self,obj):
        return mark_safe("<img src='{url}' width= 100px height=50px >".format(url=obj.image.url))

    
def _register(model,Admin_class):
    admin.site.register(model,Admin_class)

_register(models.Event, EventAdmin)  
_register(models.Courses, CoursesAdmin) 
_register(models.Admission, AdmissionAdmin) 
