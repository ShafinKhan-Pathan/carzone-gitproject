from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
# Here i am creating a function called thumbnail because i want an image on my admin panel and for that image we are passing an argument called object
# format_html is a function in which we can pass our html format tags as we have passed in this example
    def thumbnail(self , object):
        return format_html('<img src = "{}" width = "40" style="border-radius:10px"/ >'.format(object.photo.url))
# for the name in the header we are using short_description method and i named this as a Photo
    thumbnail.short_description = 'Photo'

    list_display = ('id' , 'thumbnail' ,  'first_name' , 'last_name' , 'designation' , 'created_date')
    list_display_links = ('id' , 'first_name' , 'thumbnail' , )
    search_fields = ('first_name' , 'last_name', 'designation')
    list_filter = ('designation' , )



admin.site.register(Team , TeamAdmin)
