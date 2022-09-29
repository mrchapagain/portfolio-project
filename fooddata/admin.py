from django.contrib import admin

from .models import Country_Name, Trendskeyword, TimeFrame

# Register your models here.
admin.site.register(Country_Name)
admin.site.register(Trendskeyword)
admin.site.register(TimeFrame)
