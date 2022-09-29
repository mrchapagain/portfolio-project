from django.contrib import admin

from .models import Googledf, Country_Name, Massage, Trendskeyword, Category, TimeFrame, SearchType

# Register your models here.
admin.site.register(Googledf)
admin.site.register(Country_Name)
admin.site.register(Massage)
admin.site.register(Trendskeyword)
admin.site.register(Category)
admin.site.register(TimeFrame)
admin.site.register(SearchType)
