from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self , object):
        return format_html('<img src = "{}" width="40" style="border-radius:50px" />'.format(object.car_photo.url))

    thumbnail.short_description = "Car Image"

    list_display = ('id','car_title','thumbnail','city','engine','price','year','body_style','color','is_featured')
    list_editable = ('is_featured',)
    list_display_links = ('id','car_title' , 'thumbnail',)
    search_fields = ('id', 'car_title' , 'model', 'body_style', 'year' , 'price')
    list_filter = ('state' , 'car_title' ,)




admin.site.register(Car,CarAdmin)
