from django.contrib import admin
from .models import Car
from django.utils.html import format_html


class CarAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius : 15px;" />'.format(object.car_photo.url))

        thumbnail.short_description = 'Car Image'
    
    list_display = ['id','thumbnail','car_title','color','model','city','body_style','fuel_type','is_featured']
    list_display_links = ['id','car_title']
    list_editable = ['is_featured']
    search_fields = ['id','car_title','year','body_style','fuel_type','city']
    list_filter = ['model','fuel_type','city','body_style']


admin.site.register(Car,CarAdmin)
