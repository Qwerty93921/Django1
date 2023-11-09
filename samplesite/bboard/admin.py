from django.contrib import admin

from .models import Bb
# Register your models here.

class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'published')
    list_display_links = ('title',) # если в кортеже 1 переменная тогда запятая
    search_fields = ('title', 'content')

admin.site.register(Bb, BbAdmin)
